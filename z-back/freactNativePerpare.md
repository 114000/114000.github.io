---
title: 【归档】React Native 踩坑记事(准备篇)
date: 2016-01-23
tag: Outdated
---

::: danger
2019-12-16: 留档
:::

---

记录了一下搭建 ReactNative 开发环境是遇到的坑。

<!-- more -->

<!-- toc -->

---

$$ 准备 ReactNative

* 首先 [node](https://nodejs.org/en/) 要在4.0以上，最好再更新一下 npm 的版本

``` bash
$ npm i npm -g
```

**注意**：Mac 用户使用全局安装时需要添加 `sudo` 提高命令的权限

``` bash
$ sudo npm i npm -g
# 需要输入开机密码
```

* 把 npm 指向国内镜像，避免网络环境对安装过程造成的麻烦

``` bash
$ npm config set registry https://registry.npm.taobao.org
$ npm config set disturl https://npm.taobao.org/dist
```

<!-- more -->

* 安装 react-native 命令行工具

``` bash
$ npm i react-native-cli -g
# Mac 用户需要 $ sudo npm i react-native-cli -g
```

* 初始化我们的项目，这里的项目名必须以**大写字母**开头。否则会**报错**

``` bash
$ react-native init UseRN
```

**注意**：我们也可以不使用这个工具，而使用普通的 npm 安装 react-native，只不过之后我们会使用这个工具快速运行我们的项目，所以建议安装上。

``` bash
# 不使用react-native-cli初始化项目
$ git clone git@github.com:facebook/react-native.git UseRN

$ cd react-native
react-native $ npm i
```

也可以去 [github](https://github.com/facebook/react-native) 下载安装包


如果顺利的话，我们的项目已经初始化完成了。现在需要看看是否能在 IOS/Android 中运行起来

$$ 准备 IOS 开发环境

由于做 IOS 开发只能使用 Mac，所以就没有 windows 环境的搭建介绍了。IOS 的开发环境将对来说比较简单了。只**需要保证 Xcode 版本在 7.0 以上**就行了。 要不 react-native 中 object-c 部分的语法会不支持。 写这篇文章的时候是 0.19-rc，这个版本 react-native-cli 添加了 run-ios 命令来直接运行项目，不用再在 xcode 中build项目。

``` bash
UseRN $ react-native run-ios
```

$$$ IOS - Error while persisting cache: 缓存时出错

![ReactNativePerpare01](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2016-01-23-ReactNativePerpare01.png)

此时错误信息指向了 `...../react-deep-force-update` 文件夹下的 `lib/index.js` 和 `.babelrc` 文件。

**注意**：不是 `.babelrc.stage` 文件，没有这个文件。（坑死我了 😂）

**解决办法**：

1. 直接删除 `.babelrc`。

``` bash
$ rm -rf ...../react-deep-force-update/.babelrc
```

2. 关闭 react packager 命令窗口。
3. 重新运行命令安装新的应用。

``` bash
# IOS
UseRN $ react-native run-ios

# android
UseRN $ react-native run-android
```

**原因**：
还不清楚 😂

安卓也有[同样的问题](#UnableToDownloadJSBundle)

$$$ 准备 Android 开发环境

- [安卓环境配置](http://reactnative.cn/docs/android-setup.html) - ReactNative 中文网 （翻译自 ReactNative 官网）
- [真机调试](http://reactnative.cn/docs/running-on-device-android.html) - ReactNative 中文网 （我是勤劳的搬运工 ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄）

建议还是整个 android 的设备进行调试原厂的模拟器和Genymotion模拟器感觉都不怎么好用。

**注意**：安装 git `brew install git` 需要先安装 `homebrew`

``` bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

如果还没有运行过 xcode（app store 下载） 需要按照提示同意一下 xcode 的条款，启动xcode 软件或者执行：

``` bash
# You have not agreed to the Xcode license.
# Before running the installer again please agree to the license by opening
# Xcode.app or running:
#     sudo xcodebuild -license

sudo xcodebuild -license
```

$$$ Android - 安装完应用白屏

可能是悬浮窗功能被禁用。在对应应用的**权限管理**中启用悬浮窗。启动之后一般设备可以选择**按菜单键来打开开发者菜单**。没有菜单键的也可以**摇晃手机调出菜单**。还有些手机变态到要横屏状态下按右上角的电池图标才能调出菜单（ MX2 没错~ 说的就是你 😂）

$$$ Android - Unable to download JS bundle from the dev server

![ReactNativePerpare02](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2016-01-23-ReactNativePerpare02.png)

红屏了~。没有连接到开发环境上。首先你要连到开发服务器上。

**解决方法**:

- 先查看本机的 ip 地址。

``` bash
# mac
$ ifconfig

# window
$ ipconfig
```

- 然后调出开发者菜单。-> `dev Settings` -> `debug server host & port ...` 把刚才查到的本机ip + 端口号填上 （我的是 192.168.1.207:8081）返回 Reload 下。

$$$ Android - Unable to download JS bundle

红屏了~。这个问题可能是打包失败导致的。

**解决方法**：

1. 可能是和 [IOS 同样的问题](#ErrorWhilePersistingCache)，如果控制台有错误信息，就是使用相同的解决方法。
