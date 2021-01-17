<!-- $theme: default -->

# Flutter

使用一套基础代码构建 Android 和 iOS 应用

---

## Flutter SDK

- Meterial, Cupertino, icon, color
- 手势识别
- 动画
- 分平台打包上线

<https://flutterchina.club/widgets/>

---

## Dart

强类型，面向对象，类似 Java, Csharp。但写法相对灵活。

- 类型
- 句法
- OO
- FP

---

## 目录结构

```
-/
|- android/       android 平台代码
|- ios/           iOS 平台代码
|- lib/           项目代码
|- test/          测试代码
|- pubspec.yaml   项目配置文件
```

---

### Widget 

整个 Flutter 项目就是一个 `Widget` 树，Flutter 根据每一个 `Widget` 的 `build()` 方法返回的 `Widget` 来层层递进地构建应用。它包含：
- 看的见的 Widget: 例如 UI 控件，图片，
- 看不见的 Widget: 手势，布局，间隙，状态管理

### BuildContext 

`build(BuildContext context)` 方法中都会有一个上下文参数`context`。可以让全局API知道是谁进行了这个操作。

---
## 复杂 App 开发无法避开的问题

- 路由管理
- 网络请求
- 原生通信
- 状态同步

---


### 路由管理

App 中一般没有地址栏，所以路由是一种栈结构。由导航控制入栈和出栈。


###### 入栈

``` dart
Navigator.of(context).push(MaterialPageRoute(
  builder: (BuildContext context) => Page(/* params */)
));
```

```dart
Navigator.of(context).pushNamed('/routePath' /* +'/params'*/);
```
###### 出栈

``` dart
Navigator.of(context).pop();
```

---

### 网络请求

三方：
- <https://pub.flutter-io.cn/packages/http>
- <https://pub.flutter-io.cn/packages/dio>

---

### 原生通讯

调用电池电量，摄像头，支付SDK

BinaryMessenger
- BasicMessageChannel：用于传递字符串和半结构化的信息。
- **MethodChannel**：用于调用原生方法（method invocation）。
- EventChannel: 用于数据流（event streams）的通信。

---

### 状态管理

- 异步包装的单例
- Provider
- Rxdart
- [scoped_model](https://pub.flutter-io.cn/packages/scoped_model)
---

### 安装依赖

``` yaml
# /pubspec.yaml
dependencies:
  flutter:
    sdk: flutter

  # The following adds the Cupertino Icons font to your application.
  # Use with the CupertinoIcons class for iOS style icons.
  cupertino_icons: ^0.1.2
  
  # our dependencies
  rxdart: ^0.21.0
```

``` bash
# 一般情况下，保存后vscode 会自动执行命令
$ flutter packages get
```

---

### 其他难点

- 具体功能对应的 Flutter API, eg: Socket, Animation, 下拉刷新
- 图片适配, eg: 不同分辨率屏幕的图片尺寸
- 跨平台兼容, eg: Android 的返回键
- 接入三方SDK, eg: 支付宝，极光推送
---

### 相关链接

- [官网](https://flutter.dev/)
- [SDK Docs](https://docs.flutter.io/)
- [中文网](https://flutterchina.club/)
- [配置与创建项目](http://coloration.top/posts/flutter/flutter-start.html)
- [packages](https://pub.flutter-io.cn/)
- [深入理解Flutter Platform Channel](https://zhuanlan.zhihu.com/p/43163159)
- [Flutter 输入控件TextField设置内容并保持光标(cursor)在末尾](https://www.jianshu.com/p/74659eb6d0b0)

- 项目地址: git@code.aliyun.com:Wang.Binyu/share-flutter.git

---

