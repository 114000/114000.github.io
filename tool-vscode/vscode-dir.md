# .vscode/ 项目配置


``` bash
/.vscode/
|- settings.json  # 自定义设置
|- launch.json    # 如何调试当前文件夹下的代码
|- tasks.json     # 自定义任务
```





## 配置文件 settings.json

> 优先级: .vscode/settings.json > user settings.json > editor settings

### 常见配置

|field|description|version|
|:---|:---|:---|
|`workbench.editor.showTabs`|`true(default)`/`false` 显示/隐藏编辑窗口上方的 tabs||
|`workbench.editor.highlightModifiedTabs`|`true`/`false(default)` 新增的修改区域的左侧会出现边框|[1.29.1](https://code.visualstudio.com/updates/v1_29#_highlight-modified-tabs)|
|`window.nativeFullScreen`|`true`/`false` macOS 全屏特性| [1.29.1](https://code.visualstudio.com/updates/v1_29#_macos-full-screen-support)|
|`breadcrumbs.symbolSortOrder`| `position` - 文件位置 (default) <br> `name` - 字母顺序 <br> `type` - 符号类型 <br> 控制“导航路径”大纲视图中符号的排序方式。 | [1.29.1](https://code.visualstudio.com/updates/v1_29#_symbol-order-in-breadcrumbs)|

---

[VSCode 变量引用](https://code.visualstudio.com/docs/editor/variables-reference)

---

## 任务设置 tasks.json

<https://code.visualstudio.com/docs/editor/tasks#vscode>

- 执行 task: 命令面板 -> `Run Task` -> 选择 Task 
- 配置任务: 命令面板 -> `Configure Task`

``` js
// shell 类型任务
{
  "tasks": [
    {
      // 任务描述
      "label": "echo",
      "type": "shell",
      "command": "echo Hello"
      "group": "test"  // => >Run Test Task => 选择 Task
      
      "group": "build" // => >Run Build Task => 选择 Task
      
      "group": {       // => >Run Test Task 直接执行, Run Build Task => `⌘(ctrl)` + `shift` + `b`
        "kind": "test",
        "isDefault": true
      }

      "presentation":{
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": true,
        "clear": false
      }
    }
  ]
}

// process 类型任务
{
  "tasks": [ 
    { 
      "label": "chrome", 
      "type": "process", 
      "command": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
      "windows": { "command": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" }, "linux": { "command": "/usr/bin/google-chrome" }
    }
  ]
}

// 多任务
{
  "label": "compile", 
  "dependsOn": [ "frontend", "backend" ], 
  "group": { "kind": "build", "isDefault": true }
}
```


## 调试设置 launch.json










## VSCode Debug

#### 单文件 debug

- 点击行号前方空白添加断点 / `F9`
-  `⌘(ctrl)` + `shift` + `d`

#### 工作区 debug (/.vscode/launch.json)


``` js
{
  "configurations": [
    { 
      "type": "node",      // 调试插件类型
      "request": "launch", // launch 启动并调试, attach 调试已经启动的程序
      "name": "Gulp task",
      "program": "${workspaceFolder}/node_modules/gulp/bin/gulp.js", 
      "args": [ "task" ]
    }
  ]


  "compounds": [ { "name": “All”, "configurations": [“frontend”, “backend”] }]
}


```

通用参数

- program 一般用于指定将要调试的文件。
- stopOnEntry，当调试器启动后，是否在第一行代码处暂停代码的执行。这个属性非常方便，如果没有设置断点而代码执行非常快的话，我们就会像文章的最开头那样，代码调试一闪而过，而没有办法在代码执行的过程中暂停了。而设置了 stopOnEntry 后，代码会自动在第一行停下来，然后我们就可以继续我们的代码调试了。
- args 参数。相信你应该记得在前面任务系统配置的文章里，我已经说明了可以使用 args 来控制传入任务脚本的参数，同样的，我们也可以通过 args 来把参数传给将要被调试的代码。
- env 环境变量。大部分调试器都使用它来控制调试进程的特殊环境变量。
- cwd 控制调试程序的工作目录。
- port 是调试时使用的端口。

- sourceMaps，这样 JavaScript 的调试器就知道去阅读 sourcemap 文件了。
- sourceMapPathOverrides, 原因是 webpack 自己的特殊的 sourcemap 生成方式跟 VS Code 不兼容。要解决这个问题，我们既可以通过配置 webpack，也可以通过 “sourceMapPathOverrides”这个属性来修复。