---
title: Flutter 起步
date: 2018-08-05
tag: 
- flutter
---

- [官网](https://flutter.io/)
- [中文网](https://flutterchina.club)


## 安装


### Windows 10

#### 一.下载
``` bash
# powershell/cmd/cmder
$ git clone -b beta https://github.com/flutter/flutter.git

或者用码云的镜像

git clone https://gitee.com/mirrors/Flutter.git
```

#### 二.添加环境变量

右键`我的电脑` - `属性` - `高级系统设置` - `环境变量`

1. 将存放flutter 的路径添加到 Path 中
2. 添加系统变量，国内镜像

``` diff
+ PUB_HOSTED_URL: https://pub.flutter-io.cn
+ FLUTTER_STORAGE_BASE_URL: https://storage.flutter-io.cn
```

### OSX

#### 一.下载
``` bash
# terminal
~/Library/Google $ git clone -b beta https://github.com/flutter/flutter.git
```

#### 二.添加环境变量

``` bash
# ~/.bash_profile 
# 添加下面三行

## 国内用户需要设置
export PUB_HOSTED_URL=https://pub.flutter-io.cn 
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
export PATH=/Users/apple/Library/Google/flutter/bin:$PATH


# terminal
$ source ~/.bash_profile
```




### 配置安卓环境
下载 [Android Studio](https://developer.android.com/studio/) WTF,总失败可以用迅雷下载 [Android Studio 中文社区](http://www.android-studio.org/) 提供的链接 WTF
打开 Android Studio , 点击 Plugins，选择 Browse repositories，搜索 Flutter 进行安装，

Browse repositories 响应慢试试设置 HTTP Proxy Setting Auto-detect proxy settings 再重新打开 Browse repositories

在安装 flutter 时，编辑器也会帮我们安装 dart 插件 WTF(不安就会卡在 initializing gradle )


### 检查配置

```bash
$ flutter doctor 
```

 

安装 Dart 插件

### 命令

``` bash
$ flutter doctor --android-licenses  # 同意协议才能往下进行
$ flutter config --no-analytics # 禁用通过 Google Analytics 发送数据（以免国内网络连接失败问题）
$ flutter  doctor  # 检查
$ flutter  devices # 检查链接设备
$ flutter  run     # 运行应用

$ flutter upgrade  # 升级 SDK
$ flutter --version # 查看 SDK 版本号

$ flutter clean   # 更新后可能会报错，清理 /build

```

OSX 按提示解决下列问题

iOS toolchain - develop for iOS devices (Xcode 9.4.1)
    ✗ libimobiledevice and ideviceinstaller are not installed. To install, run:
        brew install --HEAD libimobiledevice
        brew install ideviceinstaller
    ✗ ios-deploy not installed. To install:
        brew install ios-deploy

如果 android studio 提示 flutter dart 插件未安装，用android 新建一个flutter 项目即可




运行不起来或者卡在某一部 使用 flutter run -v 打印一下详细情况


### 配置编辑器

- [VSCode](https://flutterchina.club/get-started/editor/#vscode)

安装 Dart 插件

   F5 
or command + shift + p start debugging
or flutter run


### 安卓模拟器

- 网易mumu 只有32位模拟器 flutter 运行时报错 SSE2 is required [The Dart VM assumes at least a SSE2 capable CPU when running on x86.](https://github.com/dart-lang/sdk/issues/9529)

- Genymotion 好费劲啊 之后再研究吧

- [夜神模拟器](https://www.yeshen.com/)

  1. 启动模拟器
  2. `adb connect 127.0.0.1:62001`
  3. `flutter run`

  过一段时间发现 adb 版本不一致总是有问题

- android studio
  1. tools - AVD Manager 创建一个新的模拟器
  2. 回到 vscode 中点击左侧栏调试的调试，弹出框中选择刚才新建的设备，如果报错需要安装`haxm`，到 `C:\Users\admin\AppData\Local\Android\sdk\extras\intel\Hardware_Accelerated_Execution_Manager` 目录下点击安装 `intelhaxm-android.exe` 即可


## 新建项目

``` bash
$ flutter create [project]
# cd [project]
# git init
# git remote add origin <server>

```

## 安装三方依赖

pubspec.yaml

```
dependencies:
  flutter:
    sdk: flutter
  scoped_model: ^0.3.0
```

``` bash
project$ flutter packages get
```


### link 

- [material color](https://material.io/tools/color/#!/?view.left=0&view.right=0)
- [material icon](https://material.io/tools/icons/)
- [flutter widgets](https://docs.flutter.io/flutter/widgets/widgets-library.html)