---
layout: post
title: "[译] ReactiveX 与 Unity3D <一>"
date: 2017-08-26
categories: Unity3D
tag:
  - Unity3D
  - csharp
---

[原文链接](http://ornithoptergames.com/reactiverx-in-unity3d-part-1/)

- 第一篇
- [第二篇](http://coloration.cc/2017/09/01/unity_csharp-ReactiveXandUnity3D-part2/)
- [第二篇附加篇](http://coloration.cc/2017/09/02/unity_csharp-ReactiveXandUnity3D-part2.2/)
- [第三篇](http://coloration.cc/2017/09/11/unity_csharp-ReactiveXandUnity3D-part3/)

**耦合性强的代码令人头痛**。一定是有某种自然力量，像重力那样，拽着代码的尾巴，将他们纠缠在一起，难以阅读，脆弱又混乱。正如你写的那样。而且由于一些原因这种情况在游戏开发中更为常见。除非你自觉的抵制它，否则你的游戏最终会达到临界值，进一步塌陷成一个黑洞。（为什么这样说，是我最近读了挺多的科幻小说）

我现在不想阐述耦合性的[定义](https://en.wikipedia.org/wiki/Coupling_(computer_programming))，也不想说服你觉得这是个需要解决的问题。**而是，我会直接告诉你应该怎么办。**

代码的好坏与我们使用的工具有很大关系（at risk of repeating myself），在游戏开发当中，通常会使用像组件系统这样的工具来管理代码的耦合。而我的目标是希望大家能够熟练使用另一种在游戏开发中（我认为）不太为人知晓的工具（至少到目前为止）：[ReactiveX](http://reactivex.io/)。

## 工具

从基础层面上来看，可以说 **ReactiveX** 很像事件处理。好吧，即便这样那也像用使用了涡轮增压来做事件处理。除了能触发和处理事件，我们还可以向处理一等公民(译注: 例如数字变量)那样处理事件队列。他们甚至有属于自己的名字：IObservable<T>。
并且我们还可以通过很多种方式将他们变形，延时，过滤，组合或者为其自定义行为。他们将会拥有你从前使用的事件处理的功能更为强大。（如果你想看，ReactiveX 可以提供一个[详尽的介绍](http://reactivex.io/intro.html)）

我能感受到你的怀疑。所有这些响应式功能的天书难道不是为 Web 开发者和大数据大佬准备的吗？

我能理解！因为程序员的初始状态都设置在了密苏里州（不轻信州-译注：俚语，密苏里州别名）。是骡子是马拉出来溜溜（译注：俚语，不会翻）。所以作为示范，我们重写 Unity3D 标准资源包中的 `FirstPersonController ` 看看。

## 目标

在 Unity 中进行原型设计使用标准资源包是非常方便的。资源包提供了简单的用例，它的第一人称控制器打包了一些脚本和游戏对象，它们为第一人称游戏提供了以下特性：

1. 使用 WSAD 进行移动
2. 使用鼠标进行环视（上下左右）
3. 基础的碰撞物理学，因此你可以在地上行走也可以倒在地上。
4. 按住 Shift 键进行奔跑
5. 相机摆动：行走时相机会随着步伐有轻微的上下浮动
6. 按 Space 键跳跃
7. 播放脚步声，跳跃声和落在地上的声音

你不需要对 Unity 的 `FirstPersonController ` 代码很熟悉。我们不会 100 % 实现它的所有功能。但是我们会尽量接近它。在此之后，我相信你会认同 Observable 是更简洁，更容易理解，也更容易修改的方式。

那么让我们开始吧！为了能流畅的进行下去，我假设你已经对 Unity 的基础比较熟悉了。这个系列被分为了三个部分。这一部分我们实现两个基本的效果和鼠标视角。

当我们完成时，效果应该大致如下（译注：youtube）：

<iframe width="786" height="442" src="https://www.youtube.com/embed/0BasblVKr_E?ecver=1" frameborder="0" allowfullscreen></iframe>

## 开始

在创建完Unity项目之后, 我们从 Asset Store 中导入两个包：Standard Asset（用于实现一些图形和声音效果）和 [UniRx](https://www.assetstore.unity3d.com/en/#!/content/17276)。 在[GitHub UniRx](https://github.com/neuecc/UniRx)上提供了一些关于 ReactiveX 框架和一些为 Unity 单独实现的特性的说明。

下一步我们为场景添加光照，一个 Quad 作为地板, 一个 Cube 作为障碍、一个自带相机的 GameObject 作为玩家和一个名为 “GameController” 的 GameObject，GameController 仅为了方便地保存全局的脚本文件。大致的结构看起来会是这样：

![场景内的大致结构](http://upload-images.jianshu.io/upload_images/711226-3728a1a14ca27c6f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我还在 Player 游戏对象上添加了一个 CharacterController 组件。
这是一个可以使用输入驱动一些简易的移动和碰撞处理的内置人物组件。你可以使用胶囊碰撞机，运动刚体和一些代码来实现这个功能。不过我们现在还不至如此麻烦。

## 行走的实现

现在让我们的玩家开始移动。比较典型的实现方式会像这样：

``` csharp
public class ClassicPlayerController : MonoBehaviour {
  private void Update () {
    // 读取键盘输入
    // 转换成移动速度
    // 将速度赋值给人物
  }
}
```
显然，这样已经让我们的代码变得紧耦合了。为什么玩家控制器必须要知道如何读取输入? 如果我们想要改变输入的方式。输入信号可能来自跳舞毯，VR头盔，Twitch命令，有感情的AI。我们不可能为这些输入的每一种都实现一个 PlayerController。即便你知道你的游戏始终只用键盘控制输入，那你也应该从现在起避免造成不必要的耦合。

另一种方案，我们将移动输入设想成一个信号：按下 W 键，代表信号说“前进”。我们的控制器不知道信号是怎么做的，只是在接收到信号时实现动作。信号就是 Observable，例如移动（movement，一个2D向量），它就可以表示成 IObservable<Vector2>。最后,玩家控制器订阅（Subscribe）这个 Observable 就会创建一个观察者（Observer），观察者每当Observable 处理了一个新的 Vector2 矢量时都会对订阅者发出通知。

所以。我们可以为输入创建一个单独的脚本来专注分离：

``` csharp
using UnityEngine;
using UniRx;
using UniRx.Triggers;
public class Inputs : MonoBehaviour {

  public IObservable<Vector2> Movement { get; private set; }

  private void Awake() {
    Movement = this.FixedUpdateAsObservable()
      .Select(_ => {
        var x = Input.GetAxis("Horizontal");
        var y = Input.GetAxis("Vertical");
        return new Vector2(x, y).normalized;
      });
  }
}
```
首先我们声明一个 movement 变量作为公开属性，然后再在 Awake 时对它进行初始化。Observables 的一大好处就是你不能从外部注入变量。当你创建完一个 Observable 之后，你唯一能做的就只有从订阅中拿到它的输出值。这听起来令人沮丧，但是对于编写低耦合的代码却是一个非常棒的特性。在已经存在的 Observable上变换出新的 Observable 是最常见的创建 Observable 方式。这里使用“变换”这个词不太恰当，因为原来的Observable 仍然还在 - 他们是不可变的 - 我们只能创建一个新的。

我们什么时候需要读取输入信号？Fixed Update（不是 Update，因为我们知道移动涉及到了物理系统）。UniRx 提供了一个可以在每次Fixed Update 时 “tick” 一次的 Observable, 你可以通过调用 `this.FixedUpdateAsObservable()` 获取它（ns: UnityRx.Trigger）。返回值是一个 IObservable<Unit>，没有更详细的解释。`Unit` 告诉我们信号中没有有效的信息数据。事实上信号得触发就代表了这个信号的全部了。在 Observable 上我们调用了一个名为 `Select` 的方法。这个方法会在每次输入之后会返回一个新的 Observable，输出的值由我们传入的函数决定。此例中，这个函数读取行走的 x y轴数据，然后返回一个归一化的矢量。所以此时的 Movement 是一个每次 Fixed Update 时根据键盘操作输出一个矢量的 Observable。（译注:Observable 只有在被订阅之后才有实际的调用效果，是惰性的）

我们该怎么使用它呢？ 在另一个脚本中。我们订阅这个变量并且将移动设置给角色

```csharp
public class PlayerController : MonoBehaviour {
  // ... fields omitted ...

  private void Start() {
    inputs.Movement
      .Where(v => v != Vector2.zero)
      .Subscribe(inputMovement => {
        var inputVelocity = inputMovement * walkSpeed;

        var playerVelocity =
          inputVelocity.x * transform.right +
          inputVelocity.y * transform.forward;

        var distance = playerVelocity * Time.fixedDeltaTime;
        character.Move(distance);
      }).AddTo(this);
  }
}
```

首先，需要注意的是，我们在 Awake 阶段设置这个变量，然后再 Start 阶段订阅。这是为了避免初始化顺序问题，也是我的一个习惯。

在我们获取 Movement Observable 实例之后，我们有一个简洁的小优化：在哪调用，哪里就可以使用变型转换的函数：在本例中我们忽略为0的移动矢量。如果用户没有按键，我们可以更早中断。

然后我们为订阅提供一个回调函数（ns:UniRx），这样每当 Observable 有新的值传来的时候就会调用这个函数。在这个函数中我们只是简单地乘上了玩家的行走速度，然后将 2D 的输入转化到 3D 的坐标系统，再乘以时间获得移动的距离，然后将这个移动应用到 CharacterController 上。

最后，有一个 UniRx 的细节，我们需要在订阅之后调用 `AddTo(this)`。了解 Observables 和他们的订阅（Observers）的生命周期是很重要的。只要信号持续输入，他们就非常乐意保持进程。（尽管 Observable 可以完成或抛出错误，但是此时却不在我们控制的范围之内）为了不使内存泄露，避免浪费进程的性能。我们需要确保在游戏对象销毁时清理他们。这就是 `AddTo(this)` 所要做的事情。基本上当 PlayerController 所在的游戏对象被销毁。它就会释放（dispose）订阅。但这并不会释放底层的 Observable, 也就是 Movement。Movement 会在 Inputs 游戏对象销毁时被释放，因为 Movement 是在 Inputs 对象的 Fixed Update Observable 开始的。

现在你只需要使用 WASD 按键就能移动了 。是不是没有想象中的那么困难?

## 环顾四周

好吧，现在我们有了基本的功能了，可以在此基础上添加鼠标操控视角的功能。鼠标输入则是另一个信号了，不过也是一个 2D 矢量。玩家控制器会将这个矢量变换为玩家游戏对象的左右旋转和玩家内部摄像机的上下旋转。我不会一步一步写代码了。我会把最终的代码贴出来。需要注意的是，我们没有更改之前移动的订阅。而是新建了一个关于鼠标信号输入的一个新的 Observable。现在我们只不过是再重复一遍类似的操作，但这两部分在这部分却是非耦合的。移动的代码确实没有什么必要依赖旋转的代码（至少在这些简单示例的需求中）。如果为了更方便管理代码,你甚至可以把他们放到不同的脚本中。[你可以在GitHub Gist 中找到这一部分的完整代码](https://gist.github.com/JavadocMD/c38c08e6e9f000a44d348f340119a8d2)。

剩下其他的部分都是实现细节。收缩上下旋转角度是因为我们不能把头仰到脖子后面去。将光标锁定在屏幕内并将其隐藏。将输入行为变为单例(这不是不可变性造成的坏处)。在编辑器中调整输入轴设置。记得查看上面的视频展示出的行为。这些就是第一部分的内容。

希望这篇文章通过这样一个小例子能够很好地开启 Observable 话题的。[下一次我们来点复杂的，处理不同的输入，添加一些特殊的效果](http://ornithoptergames.com/reactivex-and-unity3d-part-2)

---

译注：以下是完整代码，作者贴到了 github 上，没有写在原文中

>Inputs.cs

```csharp
using UnityEngine;
using UniRx;
using UniRx.Triggers;

public class Inputs : MonoBehaviour {
  public IObservable<Vector2> movement { get; private set; }

  public IObservable<Vector2> mouselook { get; private set; }
  public void Awake () {

    movement = this.FixedUpdateAsObservable()
    .Select(_ => {
      var x = Input.GetAxis("Horizontal");
      var y = Input.GetAxis("Vertical");

      return new Vector2(x, y).normalized;
    });

    mouselook = this.UpdateAsObservable()
    .Select(_ => {
      var x = Input.GetAxis("Mouse X");
      var y = Input.GetAxis("Mouse Y");

      return new Vector2(x, y);
    });
  }
}
```

> PlayerController.cs


```csharp
using UnityEngine;
using UniRx;

[RequireComponent(typeof(CharacterController))]
public class PlayerController : MonoBehaviour {

  float walkSpeed = 5f;
	
  [Range(-90, 0)]
  public float minViewAngle = -60;
	
  [Range(0, 90)]
  public float maxViewAngle = 60;

  Inputs inputs;
	
  CharacterController character;
  Camera view;

  void Awake () {
    character = GetComponent<CharacterController>();
    view = GetComponentInChildren<Camera>();
  }
	// Use this for initialization
  void Start () {
    inputs = GameObject.Find("GameController").GetComponent<Inputs>();

    inputs.movement
    .Where(v2 => v2 != Vector2.zero)
    .Subscribe(inputMovement => {
			
      var inputVelocity = inputMovement * walkSpeed;
      var playerVelocity = 
        inputVelocity.x * transform.right + 
        inputVelocity.y * transform.forward;

      var distance = playerVelocity * Time.fixedDeltaTime;
      character.Move(distance);
    }).AddTo(this);

    inputs.mouselook
    .Where(v2 => v2 != Vector2.zero)
    .Subscribe(inputLook => {

      var horzLook = inputLook.x * Time.deltaTime * Vector3.up * 100.0f;
      transform.localRotation *= Quaternion.Euler(horzLook);

      var verLook = inputLook.y * Time.deltaTime * Vector3.left * 100.0f;
      var newQ = view.transform.localRotation * Quaternion.Euler(verLook);

      view.transform.localRotation = 
      ClampRotationAroundXAxis(newQ, -maxViewAngle, -minViewAngle);
    });
  }

  private static Quaternion ClampRotationAroundXAxis (
    Quaternion q, float minAngle, float maxAngle
  ) {
    q.x /= q.w;
    q.y /= q.w;
    q.z /= q.w;
    q.w = 1.0f;

    float angleX = 2.0f * Mathf.Rad2Deg * Mathf.Atan(q.x);
    angleX = Mathf.Clamp(angleX, minAngle, maxAngle);

    q.x = Mathf.Tan(0.5f * Mathf.Deg2Rad * angleX);
    return q;
  }
}

```