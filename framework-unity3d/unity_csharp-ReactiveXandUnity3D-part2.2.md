---
layout: post
title: "[译] ReactiveX 与 Unity3D <二.2>"
date: 2017-09-02
categories: Unity3D
tag:
  - Unity3D
  - csharp
---


[原文链接](http://ornithoptergames.com/reactivex-and-unity3d-part-2b/)

- [第一篇](http://coloration.cc/2017/08/26/unity_csharp-ReactiveXandUnity3D-part1/)
- [第二篇](http://coloration.cc/2017/09/01/unity_csharp-ReactiveXandUnity3D-part2/)
- 第二篇附加篇
- [第三篇](http://coloration.cc/2017/09/11/unity_csharp-ReactiveXandUnity3D-part3/)

我想为这个系列之前的一篇文章做一些补充。此前我们添加了一个按住 Shift 可以奔跑的效果。有些游戏则是使用 Shift 键来切换走跑状态的。通过我们的 Observable 控制器可以非常简单的完成修改。

基于信号架构的一个好处是，我们可以只改变信号的产生，而不用修改响应信号的代码。我们原来定义的 Run 信号是这样的：

```csharp
Run = this.UpdateAsObservable()
  .Select(_ => Input.GetButton("Fire3"))
  .ToReadOnlyReactiveProperty();
```

每一次 Update， 如果 Shift (“Fire3” 输入轴)被按下 Run 就返回 true, 否则就返回 false。（仅仅是为了使用方便，我们将它转化成了响应式属性）

将其改变被按键切换状态就像下面这样简单：

```csharp
var runValue = false;
Run = this.UpdateAsObservable()
  .Where(_ => Input.GetButtonDown("Fire3"))
  .Do(_ => runValue = !runValue)
  .Select(_ => runValue)
  .ToReadOnlyReactiveProperty();
```

runValue 是使用了闭包特性的*状态*。在每次 Shift 按钮被按下的 Update, 我们将 runValue 取反并重新赋值。此处的 Do 方法不是必须要有的；我们*完全可以*将 Do 中的函数移到 Select 中执行。然而 Do 明确指出有一些副作用正在发生。就像在这个例子中，状态值被操纵了，这就可以作为你的程序员伙伴的警告标志（也包括未来的你）。

当然你必须要小心没有其他地方会引用 runValue, 所以你可能希望通过将它隐藏在特定的函数中，来保护它。

最重要的是，除了那些负责*生成*运行信号的代码，我们没有改变任何其他任何一行代码。那些没有修改的代码也依然能按照预期运行！