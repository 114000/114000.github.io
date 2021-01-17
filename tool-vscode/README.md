# VSCode 快捷功能

2020-05-04

## 快捷键

Note: 
- `*` 使用频率较高
- `~` 与其他平台快捷键相同

**定义**

<div style="font-size: 12px">

|功能|Mac|Windows|备注|
|:---|:---|:---|:---|
|**定义**||||
|`*`查找定义|`F12`|`~`|`⌘/ctrl` + 左键|
|`*`查看引用|`shift` + `F12`|`~`||
|查找此定义的所有引用|`shift + alt + f12`|`~`|在列表界面使用 `f4` 下移, `shift + f4` 上移|
|弹出窗编辑定义|`⌘` + `shift` + `F12`|`ctrl` + `shift` + `F12`||
|跳转定义从新窗口打开|`⌘` + `option` + 左键 | `ctrl` + `alt` + 左键||
|从定义返回| ctrl + - | alt + left||
|返回上一次跳转定义 | ctrl + shift + - | alt + right ||
|**光标**||||
|跳转到词首或词尾|`option` + `←`|`ctrl` + `←`||
|跳转到`{` 或 `}`| `⌘` + `shift` + `\`| `ctrl` + `shift` + `\`|也作用于其他代码块 `<div></div>`|
|跳转到行首或行尾|`⌘` + `←` /`ctrl` + `a` / `⌘` + `→` |`Home` / `End` ||
|跳转到页首或页尾| `⌘` + `↑/↓` | `ctrl` + `Home/End` ||
|光标返回上一次所在位置|`⌘` + `u`|`ctrl` + `u` / `alt` + `←` ||
|创建多光标|`⌘` + `option` + `↑/↓`|`ctrl` + `alt` + `↑/↓`||
|创建多光标(鼠标)| `option` + 左键 / `option` + `shift` + 左键拖拽 / 鼠标中间拖拽 | `option` -> `alt` ||
|选中多行后,生成多光标|`option` + `shift` + `i`|`alt` + `shift` + `i`||
|跳过后面内容新起一行|`⌘` + `enter`|`ctrl` + `enter`||
|跳过后面内容插入一行| `⌘` + `shift` + `enter` | `ctrl` + `shift` + `enter` ||
|跳转到行号|`ctrl` + `g`| `~`||
|符号跳转|`⌘` + `shift` + `o`| `ctrl` + `shift` + `o`|`@:` 给所有符号分类|
|多文件符号跳转|`ctrl` + `t`| `~`||
|**注释**||||
|注释选中行| `⌘` + `/`| `ctrl` + `/`||
|光标处添加一个新注释| `option` + `shift` + `a` | `alt` + `shift` + `a`||
|**选择**||||
|普通选择| `shift` + `←` |`~`||
|选择词| `⌘` + `d` | `ctrl` + `d` | 在此按下选择相同单词 |
|选中所有相同单词| `⌘` + `shift` + `l` |  `ctrl` + `shift` + `l` |小写L|
|选择`{}` 中的内容(包括`{}`)| `> Select to Bracket` | `~` ||
|选中当前||`alt` + `shift` + `→`|1.移动光标; 2.选中单词; 3.选中当前行; 4.选中整个文档(也是鼠标点击次数)|
|鼠标拖拽行号选中多行||||
|**复制**||||
|复制当前行|`option` + `shift` + `↑/↓`|`alt` + `shift` + `↑/↓`||
|复制当前行|`⌘` + `c`|`ctrl` + `c`|光标无选中内容时|
|复制多行|选中多行 `option` + `shift` + `↑/↓`|选中多行`alt` + `shift` + `↑/↓`||
|复制选中内容|鼠标拖拽内容时, 按 `option`|鼠标拖拽内容时, 按 `ctrl`||
|**删除**||||
|删除前一个| `delete`|`Backspace`||
|删除后一个| `ctrl` + `delete` / `ctrl` + `d`|`Del`||
|删除到行首| `⌘` + `delete`|||
|删除到行尾| `fn` + `⌘` + `delete`|||
|删除到词首| `option` + `delete`|||
|删除到词尾| `fn` + `option` + `delete`|||
|删除行| `⌘` + `shift` + `k` ||光标选中多行,则删除多行|
|剪切行| `⌘` + `x`||有选中剪切选中,没有选中剪切行|
|**移动**||||
|向上/下移动一行|`option` + `↑/↓`|`alt` + `↑/↓`||
|鼠标拖拽选中内容进行移动||||
|**内置终端**||||
|唤起/收回终端窗口|`ctrl` + \` | `ctrl` + `j`||
|创建新窗口|`ctrl` + `shift` + \`|`~`||
|切分终端窗口|`⌘` + `\` |`ctrl` + `shift` + `5`||
|清除终端内容|`⌘` + `k` |`ctrl` + `k`||
|**设置**||||
|自定义快捷键|`⌘` + `k`, `⌘` + `s` |`ctrl` + `k`, `ctrl` + `s`||
|**折叠/展开**||||
|折叠/展开代码|`⌘` + `option` + `[/]`|`ctrl` + `shift` + `[/]`||
|折叠所有代码|`⌘` + `k`, `⌘` + `0`(级别 `1`,`2`)|`ctrl` + `k`, `ctrl` + `0`(级别 `1`,`2`)||
|展开所有代码|`⌘` + `k`, `⌘` + `j`|`ctrl` + `k`, `ctrl` + `j`||
|**Markdown**||||
|预览|`⌘` + `shift` + `v`|`ctrl` + `shift` + `v`||
|右侧预览|`⌘` + `k`, `v`|`ctrl` + `k`, `v`|`> Markdown: Open Preview to the Side`|
|配置预览样式|||`{ "markdown.styles": ["style.css"] }`|
|**搜索**||||
|单文件搜索|`⌘` + `f`|`ctrl` + `f`|光标在搜索框|
|单文件搜索|`⌘` + `g` / `f3`|`ctrl` + `g` / `f3`|光标在编辑器|
|多文件搜索| `⌘` + `shift` + `f` |`ctrl` + `shift` + `f` |唤醒 explorer |
|选中内容中搜索|`⌘` + `option` + `l` | `alt` + `l`|1. 选中内容 2. `⌘(ctrk)` + `f` 3. 使用这个命令|
|搜索时匹配大小写(case)| `⌘` + `option` + `c` | `alt` + `c` |
|搜索时匹配字符长度(word)| `⌘` + `option` + `w` | `alt` + `w` |
|搜索时正则匹配(regular)| `⌘` + `option` + `r` | `alt` + `r` |
|**视窗**||||
|打开/关闭 Explorer| `⌘` + `b` |`ctrl` + `b`|| 
|主视窗与编辑视窗互相切换|`⌘` + `shift` + `e` |`ctrl` + `shift` + `e` |win 下与搜狗冲突，高级-系统快捷键设置|
|打开全局搜索视窗|`⌘` + `shift` + `f` |`ctrl` + `shift` + `f` |如果有选中文字，则全局搜索选中文字，不能切换视窗焦点|
|主视窗与git视窗互相切换|`⌘` + `shift` + `g` |`ctrl` + `shift` + `g` ||
|主视窗与debug视窗互相切换|`⌘` + `shift` + `d` |`ctrl` + `shift` + `d` ||
|主视窗与插件视窗互相切换|`⌘` + `shift` + `x` |`ctrl` + `shift` + `x` ||
|切换错误与警告|`⌘` + `shift` + `m` |`ctrl` + `shift` + `m` ||
|关闭整个窗口|`⌘` + `shift` + `w`|`ctrl` + `shift` + `w`||
|关闭当前tab|`⌘` + `w`| `ctrl` + `w`||
|切换tab|`ctrl` + `tab` / `ctrl` + `[order_number]`|`~` / `alt` + `[order_number]`|加`shift`反方向切换|
|切换到第n个视窗组|`⌘` + `1/2/3`|`ctrl` + `1/2/3`||
|新建视窗组|`⌘` + `/`|`ctrl` + `/`||
|切换项目||`ctrl` + `r`|- 当前窗口切换项目: `enter` <br> - 新窗口打开项目: `⌘(ctrl)` + `enter` <br>|
|切换文件`*`|`⌘` + `p`|`ctrl` + `p` |`enter`: 直接打开, `⌘` + `enter` 新 group 打开 |
|**代码**||||
|格式化代码|`option` + `shift` + `f`|`alt` + `shift` + `f`|`> Format Document`|
|格式化选中代码|`⌘` + `k`, `⌘` + `f`|`ctrl` + `k`, `ctrl` + `f`||
|重构代码(需要语言支持)|`⌘` + `.`|`ctrl` + `.`|- 快速修复 <br>- 将代码封装为函数 <br>- 将代码移到新文件: 包括引用 <br>|

</div>

## 指令

`ctrl` + `p`

<div style="font-size: 12px">

|功能|内容|备注|
|:---|:---|:---|
|查找工作区文件|输入`文件名`|也可根据路径搜索|
|查找工作区符号|输入`#符号`|快捷键 `ctrl` + `t` 输入符号|
|跳转到行|输入`:行号`|快捷键 `ctrl` + `g` 输入行号|

</div>

<hr />

快捷键 
- `f1` 
- `ctrl` + `shift` + `p` 
- `ctrl` + `p` 输入 `>`

<div style="font-size: 12px">


|功能|内容|备注|
|:---|:---|:---|
|大小写转换| 输入 `Uppercase` / `Lowercase` / `Title Case`||
|调整缩进| 输入 `Reindent Lines` / `Reindent Selected Lines`||
|排序行| 输入 `Sort Lines Ascending` / `Sort Lines Descending`||
|跳转到定义|`Go to Definition`||
|折叠代码|`Fold`| - `Fold` <br> - `Fold All` <br> - `Fold Level`|
|自定义快捷键| 输入 `Open Keyboard Shortcuts(JSON)` 一种用UI配置, 一种用JSON 配置||
|Markdown|`Markdown:`| - `Markdown: Open Preview to the Side` 右侧预览 <br> - `Markdown: Open Locked Preview to the Side`锁定某个 Markdown 右侧预览 |
|显示/隐藏界面功能|`View: toggle` |- `Breadcramb` 编辑窗口上方面包屑路径 <br>- `Minimap` 编辑窗口缩略图 <br>- `Status Bar` 窗口下方状态栏 <br>- `Activity Bar` 窗口左侧导航栏 <br> |
|Wrokspaces|`Wrokspaces:`|- `Add Folder to Workspace` 添加一个项目到工作区 <br>- `Close Wrokspace` <br>- `Open Wrokspace ...` <br>- `Remove Folder from Workspace ...` <br>- `Save Wrokspace As...` 保存工作区<br>- `Duplicate Workspace in New Window`<br>|
|Emmet|`Emmet:`|- `Remove Tag `: 删除对应的标签 <br>- `Wrap with Attretiation `: 包裹选中标签 <br>- `Wrap Individual Line with Attretiation `: <br>- `Go to Matching Pair`: 跳转到相对应的开始标签或结束标签 <br>|
|Git|`Git:`|- `Checkout to ...` 切换分支 <br>- `Create Tag` 创建Tag <br>|
|Developer|`Developer:`|- `Inspect Editor Tokens and Spaces` 查看当前**代码**在VSCode中的信息，用于编辑器的配置|

</div>

## VSCode Extension

- Import Cost: 显示npm包的大小
- Rest Client: 在空白页输入RESTful API, 按 cmd/ctrl + alt + r 发送请求
- Live Share: 结对编程时，分享代码
- Pigment: 颜色显示在代码下方
- Git Graph: Vscode Git GUI


## snippet

1. `> Preferences: Configure User Snippets`
2. 选择(输入)语言 `typescriptreact.json`

``` json
{
  "create sfc component": {
		"prefix": "import_sfc",
		"body": [
			"import React, { FC } from 'react'",
			"",
			"export interface I$1Props {}",
			"export const $1: FC<I$1Props> = (",
			"",
			") => {",
			"",
			"  return (",
			"    ${2:null}",
			"  )",
			"}"
		],
		"description": "sfc template"
	}
}
```

- `prefix` 用来在代码中唤醒提示, 
- `body` 在编辑器中插入的内容
- `$1` 代表变量, 预设变量的值可以使用 `${1:hello}`, `${1:$CLIPBOARD}`, [更多预设变量](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variables)


### 开启 markdown snippets

**setting.json**


``` json
{
  "[markdown]": {
    "editor.quickSuggestions": {
      "other": true,
      "comments": false,
      "strings": false
    }
  }
}
```


## 自定义快捷键

1. 通过 JSON 编辑 `> Open Keyboard Shortcuts(JSON)`

``` json
[
  {
    "key": "ctrl+n",
    "command": "explorer.newFile",
    "when": "filesExplorerFocus && !inputFocus"
  }
]
```

## .vscode

```
/.vscode/
|- setting.json
|- launch.json    如何调试当前文件夹下的代码
|- tasks.json
```

### setting.json 

- 隐藏编辑窗口上方的 tabs `workbench.editor.showTabs: false`
- `workbench.editor.highlightModifiedTabs` [1.29.1](https://code.visualstudio.com/updates/v1_29#_highlight-modified-tabs)  true 新增的修改区域的左侧会出现边框
- `window.nativeFullScreen`: [1.29.1](https://code.visualstudio.com/updates/v1_29#_macos-full-screen-support) macOS 全屏特性

- `breadcrumbs.symbolSortOrder` [1.29.1](https://code.visualstudio.com/updates/v1_29#_symbol-order-in-breadcrumbs) 控制“导航路径”大纲视图中符号的排序方式。
  - position - 文件位置 (default)
  - name - 字母顺序
  - type - 符号类型

### tasks.json

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

## VSCode Debug

#### 单文件 debug

- 点击行号前方空白添加断点 / `F9`
-  `⌘(ctrl)` + `shift` + `d`

#### 工作区 debug (/.vscode/launch.json)

[Visual Studio Code Variables Reference](https://code.visualstudio.com/docs/editor/variables-reference)

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

## 附录

#### 常用语言折叠声明语法

- <https://code.visualstudio.com/docs/editor/codebasics#_folding>

|Language|Start region|End region|
|:---|:---|:---|
|C#|`#region`|`#endregion`|
|C/C++|`#pragma region`|`#pragma endregion`|
|CSS/Less/SCSS|`/*#region*/`|`/*#endregion*/`|
|Coffeescript|`#region`|`#endregion`|
|F#|`#region` or `(#_region)`|`//#endregion` or `(#_endregion)`|
|Java|`//#region` or `//<editor-fold>`|`// #endregion` or `//</editor-fold>`|
|PHP|`#region`|`#endregion`|
|PowerShell|`#region`|`#endregion`|
|Python|#region or # region|#endregion or # endregion|
|TypeScript/JavaScript|//#region or //region|//#endregion or //endregion|
|Visual Basic|#Region|#End Region|
|Bat|::#region|::#endregion|
|Markdown|`<!-- #region -->`|`<!-- #endregion -->`|


#### VSCode 命令行

打开文件并跳转到某一行: `code -r -g [file_path]:[file_line]` e.g. `code -r -g package.json:128`
比较两个文件: `code -r -d [file_path_A] [file_path_B]` e.g. `code -r -d a.txt b.txt`
将命令的结果显示在 VSCode 中: `[cmd] | code -` e.g. `ls | code -`, `ifconfig | code -`


#### 在Unity3D 中使用 VSCode 

2017-02-07

[官方参考](http://code.visualstudio.com/Docs/runtimes/unity) 

1. startup
  - windows 需要安装
    - [Microsoft .NET Core](https://www.microsoft.com/net/download/core)
    - [Microsoft .NET Framework 3.5 SP1](https://www.microsoft.com/net/download/framework)
    - ps:  `.NET Framework 3.5`  安装时需要保证 window update 开启。否则更新不成功。window10 下开启 window update 方法：按 `WIN + r` 打开运行，输入 `services.msc` 回车。找到 “Windows update”。

 - OSX 需要安装
    - [Mono](http://www.mono-project.com/download/#download-mac) 跨平台的 .NET 框架。
    - homebrew: 打开终端执行 `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` 
    - [dotnet cli](https://github.com/dotnet/cli)

2. configure

使用 VSCode 写 Unity 时，需要为 **每一个** unity 项目单独配置一下，在项目的 `Assets` 目录下新建 `Plugins/Editor` 文件夹，将下载的 [VSCode.cs](https://raw.githubusercontent.com/dotBunny/VSCode/master/Plugins/Editor/VSCode.cs) 脚本文件放到这个目录下。重启一下 Unity。在 `Preferences...` 中（OSX 下的 Unity 选项卡，Windows 下的Edit选项卡）。
![Z5(`{E9{L%WLRPE(85}0V_E.png](http://upload-images.jianshu.io/upload_images/711226-db6535159d5adae6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

勾选六项。再次开启 unity 时就会自动启动 VSCode。根据 VSCode 控制台的（报错）信息  。去下载上方提到的几种前置。

3. 支持 .lua.txt

- 安装 lua 扩展
- 在设置中添加配置项

``` javascript
// 首选项 - 设置 - settings.json
{
  // ...
  "files.associations": {
    "*.lua.txt": "lua"
  }
}
```

windows 如果双击文件不打开 vscode，尝试勾选掉 Unity Preferences/VSCode 中的 enable Integration

- 插件
  - C#：VSCode 下的 C# 语法支持
  - Unity Snippets: 提供一些语法片段
  - C# Extensions: 语法快捷扩展

- settings.json

``` json
{
  "editor.fontSize": 18,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "editor.minimap.enabled": true,
  "editor.rulers": [ 80, 100 ],
  // "editor.renderWhitespace": "boundary",

  "files.autoGuessEncoding": true,
  "files.autoSave": "onWindowChange",
  "files.defaultLanguage": "zh-cn",

  "markdown.preview.fontSize": 18,
  "extensions.autoUpdate": true,

  "workbench.colorTheme": "Material Theme",
  "workbench.iconTheme": "vs-seti"
}
```

- 异常问题
  1. 编辑器启动报错：OmniSharp.MSBuild.ProjectFile.ProjectFileInfo The reference assemblies for framework ".NETFramework,Version=v2.0" were not found.
    - 原因电脑中包含多个版本的 mono
    - 解决方案：`brew unlink mono; brew link mono`，
    - 惨嚎链接：https://github.com/OmniSharp/omnisharp-vscode/issues/1004


#### Rmote + VSCode 修改远程服务器文件

**Note:**不能打开文件夹

> foo/ is a directory and rmate is unable to handle directories.

参考
- https://www.cnblogs.com/learn21cn/p/6189023.html
- https://raw.githubusercontent.com/aurora/rmate

- 本机
  1. vscode 安装 Remote VSCode 插件
  2. 安装完后 `command + p` 输入 `> remote` 点击 `Remote Start Server`
  3. 打开终端执行 `ssh -R 52698:localhost:52698 [远程主机用户]@[远程主机IP]` 
    - 这里的端口改不了，好像写死在 shell 脚本里了
    - windows 可以使用 [Cmder](http://cmder.net/) 代替终端 

- 远程服务器

```
$ wget https://raw.githubusercontent.com/aurora/rmate/master/rmate
$ chmod +x ./rmate
$ mv ./rmate /usr/local/bin/

$ touch ~/foo.txt
$ rmate ~/foo.txt
```



#### lib

- [VS Code 能做到 - 该网站收集 VS Code 能够实现的各种高级功能教程，目前已经有36个](https://www.vscodecandothat.com/)
- 合并行: `ctrl` + `j`
- 切换窗口(工作区): `ctrl` + `w`
- 切换 tab: `⌘(ctrl)` + `option` + `←` / `→`
- 代码提示: `ctrl` + `enter`
- 强制 js 进行 ts 检查 `// @ts-check`


### 插件

||||
|:---|:---|:---|
|React Icons|这个 VSCode 插件可以让你在编辑器中直接搜索并使用 SVG 格式的图标，共支持 20 多个图标库||
