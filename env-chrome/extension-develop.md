---
title: '[译]创建一个简单的 Chrome 扩展插件'
date: 2018-10-17
---

[原文链接](https://www.thepolyglotdeveloper.com/2018/09/creating-basic-chrome-extension/)

Chrome 的扩展插件已经出现很长一段时间了，我觉得它是一个没有被充分挖掘的技术 - 如果你是一个传统的web开发者，
掌握 Chrome 扩展这项技术会有一个很平滑的学习曲线。因为 Chrome 扩展包含 HTML、CSS、JavaScript。而且你不需要考虑
浏览器的兼容问题，只会在Chrome中运行。（虽然Firefox正在变得对扩展程序友好，但不包括仅限Chrome的前端功能可能是一个好主意）

让我们开始吧，首先，需要有一个文件夹包含以下基本文件：

- manifest.json
- popup.html
- popup.js


### manifest.json

这个文件是拓展的声明文件，它包含里一些基本信息如：名字，版本，描述，图标，脚本，行为类型。我们的用例如下：

``` json
{
  "manifest_version": 2,
  "name": "Code Checker",
  "version": "1.0.6",
  "description": "This extension verifies the code exists somewhere on this page",
  "icons": {
 
  },
  "browser_action": {
    "default_icon": {
        
    },
    "default_popup": "popup.html",
    "default_title": "Check to see if our code is on this page"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "run_at": "document_end"
  }]
}
```

声明文件指定了 `popup.html` 作为默认页面，这个HTML是用户点击拓展图标弹出的页面，它包含弹出页面要显示的内容。
请注意，这个文件不能包含任何 JavaScript, 只能通过引用的方式链接到 `.js` 文件（CSS是被允许的，所以我们写在行内以保证项目结构简单）

### popup.html

``` html
<!doctype html>
<html>
  <head>
    <title>Tag Assistant</title>
    <script src="popup.js"></script>
  </head>
  <body style="background-color:#0F0;width:160px;height:90px;">
    <div id="status">
      <button id="getResults">Get Results</button>
      <h4 id="results"></h4>
    </div>
  </body>
</html>
```


### popup.js

``` js
// 声明事件处理器
document.addEventListener('DOMContentLoaded', function (event) {
  var resultsButton = document.getElementById('getResults')
  resultsButton.onclick = getResults
})

function getResults () { alert('Hello World') }
```

我们要实现一个检测当前页面是否包含某个脚本(script)的扩展。


但首先，让我们在本地部署一个只是弹出 “Hello World” 的拓展，来检查我们是否拥有了一个合法的拓展。
打开 Chrome，在地址栏中输入 `chrome:\\extensions` 并进入（确保右上角的 开发者模式开启）。点击`加载已解压的扩展程序`，找到并选中我们的项目。
这样就可以了！你会在拓展栏看到一个新的拓展。

很简单对吗？我们只花费了大概5分钟的时间就做出了一个 Chrome 拓展。

而现在，我们只能在 `popup.html` 里进行操作。 让我们看一下如何访问当前活动选项卡里的内容。
为此我们要用 `chrome.tabs.query` 找到当前选项卡：

``` js
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  // ...
})
```

在我们获取选项卡的回调里，我们要调用一个函数并将结果传递给它

``` js
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  chrome.tabs.sendMessage(tabs[0].id, { action: "checkForWord" }, function (response) {
    showResults(response.results)
  })
})
```

现在 popup.js 的完整代码如下：

```js
document.addEventListener('DOMContentLoaded', function (event) {
  var resultsButton = document.getElementById('getResults')
  resultsButton.onclick = getResults
})

function getResults () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'checkForWord' }, function (response) {
      showResults(response)
    })
  })
}

function showResults (results) {
  var resultsElement = document.getElementById('results')
  resultsElement.innerHTML = results ? 'this page uses jQuery' : 'This page does NOT use jQuery'
}
```

此时并没有可以调用的名为 'checkForWord' 的函数，我们如何注入呢？此时就需要介绍内容脚本了，
我们在 `manifest.json` 文件中更新 `content_scripts` 代码块：

``` json
"content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"],
    "run_at": "document_end"
}]
```

现在我们需要在项目添加一个 `content.js` 文件，他会操作外部页面，并将我们需要的信息返回给我们。

``` js
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'checkForWord') {
    checkForWord(request, sender, sendResponse)
    return true
  }
})


function checkForWord (request, sender, sendResponse) {
  var scripts = document.getElementsByTagName('script')
  for (var i = 0; i < scripts.length; i++) {
    if (scripts[i].src.toLowerCase().indexOf('jquery') > -1) {
      return sendResponse(true)
    }
  }

  return sendResponse(false)
}
```

至此，我们就有了一个完整功能的 Chrome 拓展，它可以用来检测页面是否使用了 jquery 


如果你需要在开发者工具中进行 debug, 你可以像debug其他网页那样，右键点击弹出页，并选择`检查`

![](https://www.thepolyglotdeveloper.com/uploads/2018/09/ChromeExtensionWalkthrough_01.png)


弹出的开发者工具可以让你对 popup.js 进行分步调试（你还可以在控制台手动调用 `location.reload()` 重载拓展程序,
这样可以避免总是需要重新打开拓展和开发工具）

对 content.js 进行分步调试会有一点不同 - 要记得，我们已经将其注入了实际的网页中。你可以打开这个页面的开发者工具实例，
但是你还是没法在通常的位置处找到我们的 content.js, 而是在 Sources 选项卡下。`Page` 是 `Sources` 下的默认子选项卡，
你向右看会有一个 `Content Script` 选项卡。当你一次展开下方的 `Top` - `Code Checker` 项就能找到 content.js


![](https://www.thepolyglotdeveloper.com/uploads/2018/09/ChromeExtensionWalkthrough_02.png)


关于 `Content Scripts` 最后需要注意的一点，这些脚本是运行在 Chrome 拓展中“独立世界”的模式中，这意味着它们在虽然可以访问选项卡页面中的 DOM，但却不能访问到该页面中任何 JavaScript 对象。

这是一个非常简单的Chrome扩展，尝试去探索更多的特性吧 - 这是你工具包中的又一个优秀且独特的工具！