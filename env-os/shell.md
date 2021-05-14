---
title: linux 常用命令
date: 2019-01-01
---

```
## 查看命令手册 manual
$ man [命令] 
```

### 查找命令

``` bash
$ which node
```

### 目录

|name|desc|
|---|---|
|`pwd`|当前目录路径|
|`ls`- list | 当前目录文件<br> `-a` - `all` 所有文件包括隐藏文件<br> `-l` - `line`单行显示文件，可显示详细信息 也可以直接使用 `ll` <br>`-t` - `time` 从新到旧排序 |

drwxr-xr-x [文件类型d][所有者权限rwx][用户组权限r-x][其他人员权限r-x]

没有 x 执行权限只能读到文件名，没法查看文件或进入目录

### 权限

|name|desc|
|---|---|
|`su`|切换为Root 用户|
|`chgrp` change group|改变文件所属用户组|
|chown|改变所有者 chown www:www www chown [user]:[usergroup] [目录/文件]|
|chmod|改变权限 chmod 774 [dir/file]|

### 文件操作

|name|desc|
|---|---|
|||


`usermod -a -G [groupName] [userName]` 不脱离原组，而加入新的组 `-a append` 更改完要重新登录才能生效

`id [username]?` 查询用户分组信息 

mac 修改域名指向 `/etc/hosts` 需要管理员权限




## 命令 
### 命令分类

1. 内建命令
    
    如：`cd`, `read`
    
2. Shell 函数
3. 外部命令：由Shell 副本（新的进程）所执行的命令

### a
- `who`: 现在的系统有谁在登录
- `cat`: 建立文件建立文件，并复制终端的输入到文件中。Ctrl + D。完成输入(end-of-file)
    * 命令后 `> 文件名` 是昔年并输入
    * 命令后 `文件名` 是查看
- `chmod`: 赋予文件执行权限

## 符号

- `|` : 管道 pipeline。左边的输出成为右边的输入 


## 安装 xz 解压工具

下载 <https://tukaani.org/xz/>

``` bash
$ tar -zxf xz-5.2.5.tar.gz
$ cd xz-5.2.5
$ ./configure
$ make & make install

$ xz -d ubuntu-20.04.2-preinstalled-server-arm64+raspi.img.xz
```

### Command Line

- [20行 Shell 脚本的马尔可夫链 - 马尔可夫链的含义是根据概率推测下一项最可能的结果。本文使用20行 Shell 脚本实现一个简单的马尔可夫链。](https://0x0f0f0f.github.io/posts/2019/11/really-fast-markov-chains-in-~20-lines-of-sh-grep-cut-and-awk/)
- [命令行的艺术](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)
- [udacity 《Shell 讲习班》](https://cn.udacity.com/course/shell-workshop--ud206/?utm_source=wechat-kol-ruanyf&utm_medium=kol&utm_campaign=freeco)
- [命令行工具的增强 - 这篇文章给出增强版命令行工具的清单，比如 bat 取代 cat，htop 取代 top 等等](https://remysharp.com/2018/08/23/cli-improved)
- [命令行 2048 游戏](https://github.com/plibither8/2048.cpp)
[《Linux 命令行（第五版）》](https://nostarch.com/tlcl.htm)
- [命令行脚本的运行原理-脚本的第一行为什么以 #! 开头？Shell 内部又是如何处理脚本的？](https://blog.twentytwotabs.com/the-smallest-bash-program-in-the-universe/)
- [nodebook - 一般情况下，Node REPL 环境只能在命令行使用。这个工具起了一个服务，让你在浏览器里就能使用 REPL 环境。](https://github.com/netgusto/nodebook)
- [bat bat 是 cat 命令的加强版，同样在命令行输出文件内容，但是带有高亮和分页，并且与 Git 集成。](https://www.ostechnix.com/bat-a-cat-clone-with-syntax-highlighting-and-git-integration/)
- [webtty 一个使用 WebRTC 协议分享命令行对话的工具，特点就是点对点的分享，不需要中间代理，而且可以在浏览器之中使用。](https://github.com/maxmcd/webtty)
- [ydcv - 有道辞典的命令行版本](https://github.com/felixonmars/ydcv)
- [ervy 命令行打印图表的库。](https://github.com/chunqiuyiyu/ervy)
- [navi 一个命令行的交互式备忘工具，你可以查阅某个命令的作用。](https://github.com/denisidoro/navi)
- [如何让 SSH 更安全？提高 SSH 安全等级的一些知识。本文较难，需要密码学知识。](http://stribika.github.io/2015/01/04/secure-secure-shell.html) 
[asciinema 一个录制、分享命令行操作的工具，支持Linux, macOS](https://asciinema.org/)
- [taskbook - 任务管理的命令行小工具。](https://github.com/klauscfhq/taskbook) 
- [dd 命令教程 - dd 命令通常用来克隆整块磁盘，或者制作 Linux 系统的 USB 启动盘。这篇文章教你怎么用，其实很简单。"](https://opensource.com/article/18/7/how-use-dd-linux) 
- [hiper - 一个查看网页加载性能的命令行程序](https://github.com/pod4g/hiper) 
- [DNS 基础知识与 dig 命](https://www.redhat.com/sysadmin/dns-domain-name-servers)
- [如何写 Linux 的监控脚本 - 本文演示一个简单脚本，监控某个服务是否正常，如果启动失败就会发邮件通知管理员](https://www.redhat.com/sysadmin/linux-monitoring-and-alerting)
- [BashUpload 一个可以从命令行上传文件的网站，文件上传后可以保存七天，其间可以无限次下载。](https://bashupload.com/)
- [youtube-dl-interactive - 具有互动界面的命令行 Youtube 下载器，基于 youtube-dl。](https://github.com/synox/youtube-dl-interactive)
- [bat - 命令行的 cat 命令用来显示文件的内容，bat 命令完全跟 cat 一致，只有一个地方不一样，就是现在的内容会带有行号和代码高亮。](https://github.com/sharkdp/bat)
- [Learn command line - 一本开源的初级命令行教程，特色是配有大量的手绘图。](http://hellowebbooks.com/learn-command-line/) 
- [percollate 命令行抓取网页，生成 PDF 文件的工具。](https://github.com/danburzo/percollate)
- [如何制作命令行动画？-本文介绍如何使用 ncurses 这个 C 语言标准库，写一个简单的命令行动画。](https://github.com/harrinp/Command-line-guide/blob/master/README.md)
- [谷歌官方的 Bash 脚本风格要求](https://google.github.io/styleguide/shell.xml)
- [让你的生活更轻松的9个 Bash 快捷别名 本文介绍9个实用的 Bash 函数，你可以参考他的方式，将自己常用的操作封装成函数，然后设置别名。](https://medium.com/@raimibinkarim/9-bash-aliases-to-make-your-life-easier-3e5855aa95fa)
- [一个 Bash 脚本，可以在 Debian 系的发行版上，让用户通过图形界面，一次性选择所要安装的应用程序，主要用于新系统的装机。](https://github.com/shubhampathak/autosetup)
- [ExplainShell.com Bash 命令的可视化解释工具。遇到复杂的 Bash 命令，可以输入到这个网站，查看该命令的解释。](https://www.explainshell.com/)
- [Bash 操作指南 - 收集各种 Bash 常用操作的仓库，比如分割字符串、倒转数组等等。](http://github.com/dylanaraps/pure-bash-bible) 
- [xonsh shell - 一个基于 Python 的 Shell，最大特点就是跨平台。](https://xon.sh/)
- [rebound - 有人终于把这个工具写出来了，一旦 Python 或 JS 脚本报错，就到 Stack Overflow 取回报错信息的解释。](https://github.com/shobrook/rebound)
- [如何将任意命令装为图形界面](https://chriskiehl.com/article/gooey-as-a-universal-frontend)
- [什么是cgi脚本](http://rickcarlino.com/2019/07/20/what-were-cgi-scripts-html.html)
- [一个多功能、跨平台的终端模拟器](https://eugeny.github.io/terminus/)
- [nvtop - Linux 服务器的 top 命令可以查看 CPU 的状态。nvtop 命令则是用来查看 NVidia GPU 的状态。](https://github.com/Syllo/nvtop)
- [tomato-clock - 一个实现番茄工作法（将工作划分为25分钟的片段）的 Python 小脚本。](https://github.com/coolcode/tomato-clock)

- [mv 命令无需两次键入文件名](https://news.ycombinator.com/item?id=22860140)
- [scp 命令的原理和特点 - scp命令用于向远程主机复制文件，本文解释它的原理，以及优点和缺点。](https://gravitational.com/blog/scp-familiar-simple-insecure-slow/)
- [ping 的故事 - ping是最常用的网络命令之一。这篇文章是ping的作者介绍他怎么写出这个工具。他以前的工作是研究声纳和雷达，声纳发出的声音脉冲就叫做ping。](https://ftp.arl.army.mil/~mike/ping.html)
- [wtf - 在终端窗口显示控制台面版](https://github.com/senorprogrammer/wtf) 
- [通过游戏学习 Vim，看上去比较有趣](https://vim-adventures.com/)
