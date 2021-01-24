---
title: 'browser tip'
---

### 防止浏览器自动填充密码

浏览器会识别 <input type="password" /> 并将其上方的input作为用户名。

```html
<!-- display: none; 不会生效 -->
<div style="height:0;opacity:0;">
  <input type="text" />
  <input type="password" />
</div>
```


### JS 设置 CSS 变量

``` js
document.documentElement.style.setProperty('--vh', vh + 'px')
```

## 复制到剪切板

```js
const selection = document.getSelection()
  selection.removeAllRanges()
  document.activeElement.blur()
  const range = document.createRange()
  const span = document.createElement('span')
  span.textContent = textToCopy
  span.style.all = 'unset'
  span.style.position = 'fixed'
  span.style.top = 0
  span.style.clip = 'rect(0, 0, 0, 0)'
  span.style.whiteSpace = 'pre'

  document.body.appendChild(span)
  range.selectNode(span)
  selection.addRange(range)
  try {
    if (!document.execCommand('copy')) {
      throw new Error(t('Not successful'))
    }
  } catch (err) {
    window.alert(t('Sorry, your browser does not support copying. Use Ctrl / Cmd + C!')) // eslint-disable-line
  }

  document.body.removeChild(span)
  if (selection.removeRange) {
    selection.removeRange(range)
  } else {
    selection.removeAllRanges()
  }
```
### zip 打包并下载

- [前端JS zip打包文件并下](https://www.zhangxinxu.com/wordpress/2019/08/js-zip-download/)