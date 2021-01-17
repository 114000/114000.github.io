---
title: 【归档】新的开始，使用 atom 编辑器
date: 2016-01-04
tag: Outdated
---

::: danger
2019-12-16: 现在都用 VSCode，这篇文章只是存档
:::

---

这款编辑器不太适合日常代码体积很大的人员使用, 没办法因为是用的 node-webkit, 性能跟网页差不多，
但是颜值比较高，就这一点就足够了吧 ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

<!-- more -->

<!-- toc -->

---

### 安装 atom

[atom github release](https://github.com/atom/atom/releases)
[atom 国内镜像](http://cnpmjs.org/mirrors/atom) 下的慢可以来这里😄

**ps**:
  windows 用户最好下载 `AtomSetup.exe`，会自动添加命令行功能 `atom`，`apm`。或者在安装完成后
  在菜单栏中选择 `Install Shell Commands`

[atom 中文社区](https://atom-china.org/)

打开项目可以使用命令

``` bash
$ atom <project path>
```

<!-- more -->

### 简介

#### 树状图 - 方便的文件管理

* 隐藏树形视图 `command + \` / `ctrl + \`
* 聚焦树形视图 `control + 0` / `ctrl + 0`
* 添加文件 `a` (可以包含路径，如果这个路径文件夹不存在，则会创建出来)
* 添加文件夹 `shift + a` (同样会创建不存在的路径文件夹)
* 重命名文件/移动文件 `m`
* 复制文件/移动文件 `d`
* 向上移动 `🔼` `k`
* 向下移动 `🔽` `j`
* 移动到顶部 `command + 🔼` / `home`
* 移动到顶部 `command + 🔽` / `end`
* 展开当前文件夹 `enter` `control + ]` / `enter` `ctrl + ]`
* 收起当前文件夹 `enter` `control + [` / `enter` `ctrl + [`
* 递归展开文件夹 `control + option + ]` / `ctrl + alt + ]`
* 递归收起文件夹 `control + option + [` / `ctrl + alt + [`


#### 自定义外观 - 外协会员

* 我们可以更改编辑器的主题，和语法高亮的主题

  打开设置面板 `command + ,` / `ctrl + ,`

  `Themes` 选项卡中可以设置主题
  `Install` 选项卡中可以安装主题

* 自定义主题样式

  `Atom` -> `open your stylesheet`（`.less` 文件）
  `View` -> `Developer` -> `Toggle Developer Tools`
  或者（`command + option + i` / `ctrl + alt + i`）查找对应元素的 css 样式覆盖即可



#### 包管理工具 apm - atom package manager

以下， 需要在命令行工具里运行

* 搜索 - `search`

  ``` bash
  $ apm search <key>
  ```

* 安装 - `install`

  ``` bash
  $ apm install <package name>
  ```

  **ps**：安装完包之后需要重启编辑器才能生效 `control + option + command + l` / `alt + ctrl + r`

* 列出安装了的包 - `list`

  ``` bash
  $ apm list
  ```
  **ps**: 上面部分是编辑器自带的包， 下面是我们自己安装的包

* 卸载 - `uninstall`

  ``` bash
  $ apm uninstall <package name>
  ```

* 列出命令列表

  ``` bash
  $ apm
  ```

* 打开项目首页（默认浏览器）

  ``` bash
  $ apm home <package name>
  ```

* 查看命令帮助

  ``` bash
  $ apm help <command name>
  ```

* **常用的包包**：

  - `emmet`: 有html句法
  - `autocomplete-paths`: 自动补全路径
  - `pigments`: 显示代码代表的颜色
  - `language-babel`: es6 语法高亮
  - `local-server-express`: 起一个服务器环境，监听8000端口
  - `minimap`: 代码缩略图


#### 自定义代码段 - snippets

`Atom` -> `open your snippets`

举一个比较没用但是很贴切的例子。

``` coffee
# snippets.cson

'.source.css':
  'css3 browser prefix':
    'prefix': 'css3.prefix'
    'body': """
      ${1:STYLE_NAME};
      -webkit-${1:STYLE_NAME};
      -moz-${1:STYLE_NAME};
      -ms-${1:STYLE_NAME};
      -o-${1:STYLE_NAME};
    """
  'other css snippets':
    ...
```

保存之后在css文件中输入 `css3.prefix` 小条中会有提示：
![atom01](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-25-atom01.png)

回车之后：
![atom02](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-25-atom02.png)


**ps**:
 这里的 `${1:STYLE_NAME}` 代表第一次聚焦的时候光标的位置（可以是多个），依次地，`$2` 代表第二次聚焦的地方，按 `tab` 键可以切换。`STYLE_NAME` 代表着提示的文字。如果没有可以用 `$1` 代替。
可以在 `.js` 文件中输入 `fun` 就一目了然了

在 .css 文件中输入 `css3.prefix`

#### 快速编辑文件

1. 文件操作

- 跳转到页首: `command + 🔼` / `ctrl + home`
- 跳转到页尾: `command + 🔽` / `ctrl + end`
- 跳转到指定行: `control + g` / `ctrl + g`
- 函数之间跳转: `command + r` / `ctrl + r`
- 标签之间跳转: `control + m` / `ctrl + m`
- 保存全部文件: `option + command + s` / ``
- 跳转到文件: `command + p` / `ctrl + p`
- 在打开的文件中切换: `command + b` `ctrl + 数字键`/ `ctrl + b` `ctrl + pageUp` `ctrl + pageDown` `ctrl + 数字键`
- 关闭当前文件: `command + w` / `ctrl + w`

2. 单行操作

- 跳转到行首: `command + <-` / `home`
- 跳转到行尾: `command + ->` / `end`
- 移动一行: `control + command + 🔼` `control + command + 🔽` / `ctrl + 🔼` `ctrl + 🔽`
- 选择一行/下一行: `command + l` / `ctrl + l`
- 删除一行: `control + k` / `ctrl + shift + k` `shift + delete`
- 复制一行: `command + shift + d` / `ctrl + shift + d` （不占用剪切板）
- 复制一行
- 剪切一行
- 粘贴一行
- 从光标处删除到行首: `command + delete` / ``
- 从光标处删除到行尾: `command + fn + delete` / ``
- 合并当前行与下一行: `command + j` `ctrl + j`

3. 单词操作

- 跳过单词 `option + <-` `option + ->` / `ctrl + <-` `ctrl + ->`
- 选择一个/下一个单词 `command + d` / `ctrl + d`
- 选中文档中所有单词 `control + command + g` / ``
- 删除单词的前半部分 `alt + delete` / `alt + backspace`
- 删除单词的后半部分 `alt + fn + delete` / `alt + delete`
- 大写当前单词 `command + k, command + u` / `ctrl + k, ctrl + u`
- 小写当前单词 `command + k, command + l` / `ctrl + k, ctrl + l`

4. 编辑器操作

- 关闭编辑器 `command + q` / ``
- 关闭项目窗口 `command + shift + w` / `ctrl + shift + w`
- 全屏显示 `control + command + f` / `win + 🔼`
- 查看命令帮助 `command + shift + p` / `ctrl + shift + p`
- 调整字号大小 `command + '-'` `command + '='` / `ctrl + '-'` `ctrl + '='`

5. 书签

**ps**：windows 貌似没有办法添加书签，但是可以查看已有的书签

- 为本行添加/删除书签 `command + F2`
- 跳转到下一个书签 `F2`
- 跳转到上一个书签 `shift + F2`


> 我们几乎可以自定义这个编辑器内的任何东西，它只是一个 html 文件而已。



### UPDATE

- **UPDATE-2016.12.25:**
  * 隐藏右边的白线

    ``` css
    atom-text-editor::shadow .wrap-guide {
      visibility: hidden;
    }
    ```

  * [可以做一些简单的初始化配置](https://github.com/nieweidong/learn-atom/blob/master/README.md#聊聊settings)
  * 包包

    - [activate-power-mode](https://atom.io/packages/activate-power-mode) - 很炫酷的编辑效果，就是有bug，还很卡😂
    - [atom-beautify](https://atom.io/packages/atom-beautify) 美化代码的插件。
