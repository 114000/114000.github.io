# Node 将网页转为 PDF

> 主要思路是通过使用 `puppeteer` 模拟浏览器的 `ctrl + p` 的打印功能来生成pdf. 但是由于浏览器对打印标准支持的不好. 前端很难准确控制住pdf的样式展现, 所以还是需要后端做大量细节处理.


## 总览

- 前端使用媒体查询 `@media print { ... }` 来单独控制打印样式
- 前端的可以使用 `break-after: page;` css样式控制分页
- 后端使用 `puppeteer` + `pdf-lib` 处理 pdf: 
  - `puppeteer.launch().newPage().pdf(PdfOption)` 进行截图
  - `puppeteer` 通过设置 `page.pdf.option` 来分页**封面**和**内容** 添加**页头**和**页脚**
  - `pdf-lib` 来组合**封面**和**内容**

- 一些注意事项
  - 前端不能添加页头页脚, `position: fixed`. 这种方式很容易遮挡页面内容, 而且无法得到**页数**
  - 前端不能通过 `@page { margin: 0 }` 来单独处理**封面**的边距, 这会影响后续页面的排版. 所以在服务端分别截取封面和内容
  - 服务器上可能没有中文字体, 所以有些中文会变成乱码, 前端需要把字体文件包含到项目中. `css: font-face`.但就算包含字体, 由于页头,页脚并不包含在文档流中. 所以任何样式都不起作用. 
  - 修改页头,页脚的注意: 
    1. 样式一般使用 inline css
    2. 图片无法使用 url 加载, 但可以使用 base64 `<img src="base64" />` 
    3. 页数和日期格式非常固定, 如果修改需要服务端进行插值. `'<span class="date"></span>'.replace('2021-03-15')`. `2021/03/15` -> `2021-03-15`
  - `puppeteer` 可以获取网页上**最初**的内容. 但如果是动态内容. 需要确保后端调用 pdf 前动态内容已经修改.
  比如使用网页的 `document.title` 作为pdf的文件名
  - 页眉页脚中的特殊变量由CSS类特殊定义 
    - `<span class="date"></span>` => `<span>2021/03/15<span>`
    - `<span class="pageNumber"></span>` => `<span>1<span>`
    - `<span class="totalPages"></span>` => `<span>10<span>`
- 还没解决的问题
  - echarts 的文字(axisLabel)没有使用前端项目的字体



## 前端部分

前端针对打印唯一稳定的控制只有分页功能. 

``` css
@media print {
  .page-container
  .page-divider {
    /* 打印的特有样式, 没有媒体查询也没关系 */
    break-after: page;
  }
}
```


## 后端部分

1. 浏览器打开需要打印的网页

``` js
const puppeteer = require('puppeteer')

function loadPage (url, wait = 1000) {

  return new Promise(async (resolve, reject) => {

    const browser = await puppeteer.launch({ 
      // for centOS
      // https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md
      headless: true,
      args: ["--no-sandbox"], 
    })

    const page = await browser.newPage()

    // 全部网络链接完成后
    // http://puppeteerjs.com/#?product=Puppeteer&version=v8.0.0&show=api-pagegotourl-options
    await page.goto(url, { waitUntil: 'networkidle0' })
      
    setTimeout(() => resolve({ page, browser }), wait)
  })
}

```

2. 打印封面和内容

``` js

function pageToPdf (page, options = []) {
  // http://puppeteerjs.com/#?product=Puppeteer&version=v8.0.0&show=api-pagepdfoptions
  const defaultOption = {
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: false,
  }

  return Promise.all(options.map(opt => 
    page.pdf(Object.assign({}, defaultOption, opt))
  ))
}

```


3. 合并pdf

``` js
const { PDFDocument } = require('pdf-lib')

async function combinePdf (pdfs, config = {}) {
  
  const doc = await PDFDocument.create()

  // [pdf, pdf] => 
  // [[page1], [page2, page3 ...]] 
  const pagesCollPromises = pdfs.map(async (pdf) => {
    
    const pdfDoc = await PDFDocument.load(toArrayBuffer(pdf))
    return doc.copyPages(pdfDoc, pdfDoc.getPageIndices())
  })

  const pagesCollections = await Promise.all(pagesPromises)

  // [[page1], [page2, page3 ...]] => 
  // [page1, page2, page3, ...]
  const pages = pagesCollections.reduce((flat, pc) => flat.concat(pc), [])
  
  // [page1, page2, page3, ...] => 
  // doc
  pages.forEach((p) => doc.addPage(p))

  await doc.setTitle(config.title ? config.title : await page.title())

  // doc => arrayBuffer
  const docBytes = await doc.save()

  // arrayBuffer => buffer
  return Buffer.from(docBytes) //.toString('base64')
}

```

4. 调用 


``` js
const { page, browser } = await loadPage('http://demo.com')

const pdfs = await pageToPdf(page, [{
  pageRanges: '1'
}, {
  displayHeaderFooter: true,
  // only for content page 
  footerTemplate,
  headerTemplate,
  // page.2+
  pageRanges: '2-', 
  // content margin
  margin: {
    top: '2cm',
    left: '0.72cm',
    right: '0.72cm',
    bottom: '1cm',
  }
}])

await browser.close()

const pdfBuffer = await combinePdf(pdfs, { title: 'pdf-file-title' })

response.set({ 'Content-Type': 'application/pdf', 'Content-Length': pdfBuffer.length })
response.send(pdfBuffer)

```


## E.X.

1. <http://puppeteerjs.com/>
2. <https://pdf-lib.js.org/>
3. Buffer to ArrayBuffer

``` js
function toArrayBuffer(buf) {
	var ab = new ArrayBuffer(buf.length)
	var view = new Uint8Array(ab)
	for (var i = 0; i < buf.length; ++i) {
		view[i] = buf[i]
	}	
	return ab
}
```