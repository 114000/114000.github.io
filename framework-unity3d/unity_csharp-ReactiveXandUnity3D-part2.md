---
layout: post
title: "[译] ReactiveX 与 Unity3D <二.1>"
date: 2017-09-01
categories: Unity3D
tag:
  - Unity3D
  - csharp
---

[原文链接](http://ornithoptergames.com/reactivex-and-unity3d-part-2/)

- [第一篇](http://coloration.cc/2017/08/26/unity_csharp-ReactiveXandUnity3D-part1/)
- 第二篇
- [第二篇附加篇](http://coloration.cc/2017/09/02/unity_csharp-ReactiveXandUnity3D-part2.2/)
- [第三篇](http://coloration.cc/2017/09/11/unity_csharp-ReactiveXandUnity3D-part3/)


这是三部曲的第二篇。使用 ReactiveX 实现 Unity 标准资源包中的第一人称控制器，是这个系列文章的主要内容。

我们上一篇已经完成了行走和鼠标控制视野功能。现在我们来添加奔跑功能和摄像机震动功能。这篇文章里我们将会开始看到一些我们在第一部分所做工作的一些回报。以下是我们这次将要完成的效果：

<iframe width="786" height="442" src="https://www.youtube.com/embed/G_N8l9Sd-aI" frameborder="0" allowfullscreen></iframe>

## My little runaway
（译注：题目好像是歌名）

"按住 Shift 跑动" 在第一人称游戏中几乎是标准实践，所以我们要支持这个功能。即便使用 Observable 也有很多种实现方式。不过我觉得这是一个介绍响应式属性（Reactive Properties）的绝佳机会。这个特性是 UniRx 中独有的，它不在 ReactiveX 的标准中。

响应式属性让我们二者兼得：技能拥有属性的灵活性，也可以拥有 Observable 的功能。你不仅可以像设置和获取一个正常属性值那样来操作响应式属性，而且你还可以通过订阅这个属性来得到它变化的通知。将奔跑的信号输入转换成响应式属性的原因是，我不想对用户按下和释放按键做出反应，我仅仅想要知道在计算移动时，按键处于按下状态。下面给 Inputs 脚本添加一些代码（我省略了之前的代码）


```csharp
public ReadOnlyReactiveProperty<bool> Run { get; private set; }
// ...

private void Awake() {
  // ...
  Run = this.UpdateAsObservable()
    .Select(_ => Input.GetButton("Fire3"))
    .ToReadOnlyReactiveProperty();
}
```

首先，我声明了一个 `ReadOnlyReactiveProperty`属性。如果我使用普通的 ReactiveProperty 属性，那么任何代码都可以改变它的值。为了能让你的代码解耦，更好的方式是，在任何可能的情况下限制写的权限。并且无论什么情况下，我们都不必主动设置 Run 的值，因为我们完全可以制造另一个 Observable 来生产新值。正如我们在 Awake 中所做的：每次 Update 时得到 “Fire3” 按钮的状态，将它转化为属性值。（“Fire3” 是 Unity 项目默认定义的输入轴, 可以方便地匹配到 Shift 键）

使用这个输入也很简单。在 PlayerController 添加一个 runSpeed 属性。现在我们在计算移动的时候，就可以查询 Run 的值来决定使用哪种速度了。

```csharp
// In PlayerController.Start()
inputs.Movement
.Where(v => v != Vector2.zero)
.Subscribe(inputMovement => {
  var inputVelocity = inputMovement * (inputs.Run.Value ? runSpeed : walkSpeed);
    // ... etc.
```

这可能是实现这个功能最简单的方式了，但它是否足够好呢？ 此处使用 Observable (或者任何其他的异步代码) 有些许微妙之处：因为除非两个输入信号直接依赖于彼此，否则我们基本上无法保证它们的执行顺序。换句话说：我不清楚当我访问 Run 值的时候，它是否已经更新完毕了。所以在使用这段代码的时候，我们心中最好有预期。

站在移动信号的角度看， Run 值可能会落后一帧。现在有方法可以确保正确的执行顺序（我们将在第三部分看到他们），但这会是你的代码变得复杂化。你要想清楚这样做是否值得。跑慢一帧有没有关系？可能没问题，也可能有。这当然就是你的工作啦，去把它找出来。但现在，我们会继续使用这个简单的方法。

> 在下面的情况下，你可能对这种执行效果感觉足够了：首先你知道 Update 是在 FixedUpdate 之前处理的，并且我们代码的调用都是像这样直截了当的。但你不能指望这点。所以最好是围绕这个问题进行设计。

## Bob and un-weave

实现摄像机摆动将会带来更多的代码混合，也因此我们可以看到 Observables 展现给我们的低耦合代码了。我们会对摄像机进行轻微的弹动来模拟行走，所以我们需要知道移动时每一帧间隔的空间距离。在标准资源中，这个效果是通过让播放器的控制器直接更新负责相机摆动效果的类来实现的。自然地，这会将播放器控制器代码和相机摆动的代码耦合在一起，而这正是我们要避免的。现在，我们要使用 Observable 生成这两个类之间的接口。（好吧，它实际上是一个抽象类，但是很容易使用 Unity 的 inspector 做兼容处理）

``` csharp
public abstract class PlayerSignals : MonoBehaviour {
  public abstract float StrideLength { get; }
  public abstract IObservable<Vector3> Walked { get; }
}
```

我们的 `PlayerController` 将会继承并实现这个抽象类（译注：原作者在代码的第一版时使用的是接口，后又转而使用了抽象类，原文此处行文为接口），因此控制相机摆动的脚本则不需要直接依赖 PlayerController 。`StrideLength` 是一个简单的配置项。那我们怎么实现 Walked Observable 呢? Unity 的 CharacterController 组件实际上会为我们[计算这个值](https://docs.unity3d.com/ScriptReference/CharacterController-velocity.html)（这是考虑到墙壁碰撞后移动的实际距离），我们要做的就是导入这个值。改写移动的代码。

```csharp
inputs.Movement
  .Where(v => v != Vector2.zero)
  .Subscribe(inputMovement => {
    // ...
    var distance = playerVelocity * Time.fixedDeltaTime;
    character.Move(distance);
    var distanceActuallyWalked = character.velocity * Time.fixedDeltaTime;
}).AddTo(this);
```
我们想要将 `distanceActuallyWalked` 放到一个 Observable 中。但是我说过不能从外部向 Observable 中注入值，对吧？

其中一个选择是介绍一个新概念：Subject。在 ReactiveX 中，Subject 结合了 Observer 和 Observable ， 但你**不能**将它理解成是一个 “可读写的 Observable”。 那它就与响应式属性没有什么区别了。Subject 没有像响应式属性那样定义一个“当前值”。 你只能通过订阅 Subject 来得到它改变后传给你的通知，但你不能拿到它的当前值。所以你可以将它理解成阉割版的响应式属性。而且你在任何情况下都应该选择能使代码正常运行而功能添加又最少的选项。在实践中需要根据如何使用信号来进行决策。

那我们在 PlayerController 脚本中添加一个  Subject<Vector3> 字段，因为这是属于**我们自己的**信号（译注：“我们”指 PlayerController， 相对于 Inputs而言），那就需要在 Awake 中初始化它。 

```csharp
walked = new Subject<Vector3>().AddTo(this);
```

为了能在我们的游戏对象中约束这个信号的生命周期，添加了 `AddTo(this)`。

现在我们用下面这行代替 `distanceActuallyWalked`:

```csharp
walked.OnNext(character.velocity * Time.fixedDeltaTime);
```
OnNext 方法会为信号提供一个新的值。任何订阅这个信号的人都会得到携带这个新值得通知。

我们到现在还没接触到相机摆动的那一部分，但是我觉得我们已经做的相当不错了。我们的脚本不仅仅只是“消耗”信号，而且还能产生新的信号。这使你可以集成不基于 Observable 的系统，比如 Unity 的物理系统和场景图。

这里最后需要记着点。到目前为止，我都十分谨慎地限制着代码的读写权限。如果我公开了 Subject 的权限，那么潜在地，任何人都可能在此处修改信号的值并破坏我们的代码（可能是在上线前一天的夜里3点钟）。不过不用担心：因为 Subject 是一个 Observable，我们可以像下面这样通过定义来简单的限制一下我们变量的可见性。

``` csharp
private Subject<Vector3> walked;
public override IObservable<Vector3> Walked {
  get { return walked;  }
}
```

我们可以看见 Subject，其他人只能看见 IObservable。干净漂亮！

Okey，接着就是实际的相机摆动脚本了！这个脚本需要设置在相机的游戏对象上，控制它的运动。我们要订阅 Walked 信号并累计玩家移动的距离，然后在对步长取模。我们用 Unity AnimationCurve 将这个值转化为能正确调整相机位置的正弦曲线。（译注：代码中的注释就不翻译了，最下面有完整的代码和注释）

```csharp
public class CameraBob : MonoBehaviour {
  // IPlayerSignals reference configured in the Unity Inspector, since we can
  // reasonably expect these game objects to be in the same hierarchy
  public PlayerSignals player;
  public float walkBobMagnitude = 0.05f;
  public float runBobMagnitude = 0.10f;

  public AnimationCurve bob;

  private Camera view;
  private Vector3 initialPosition;

  private void Awake() {
    view = GetComponent<Camera>();
    initialPosition = view.transform.localPosition;
  }

  private void Start() {
    var distance = 0f;
    player.Walked.Subscribe(w => {
      // Accumulate distance walked (modulo stride length).
      distance += w.magnitude;
      distance %= player.StrideLength;
      // Use distance to evaluate the bob curve.
      var magnitude = InputsV2.Instance.Run.Value ? runBobMagnitude : walkBobMagnitude;
      var deltaPos = magnitude * bob.Evaluate(distance / player.StrideLength) * Vector3.up;
      // Adjust camera position.
      view.transform.localPosition = initialPosition + deltaPos;
    }).AddTo(this);
  }
}

```
注意，`distance` 变量是需要在订阅内部使用的 `状态`。在这我用使用了*闭包*来实现。之前我们是使用类变量来实现的。（例如：CharacterController 实例）

为了提升真实感，我们还可以根据玩家的跑动状态来决定相机摆动的幅度大小。归根结底，这个例子是为了说明如何清晰整洁地重用一个信号：当我们处理 Run 的时候真的无需考虑相机如何摆动。

我们完成了第2部分！我们添加了跑动和相机特效，而并没有将我们的代码混杂。当需求变化时，我们可以轻易地将相机摆动的效果移除，因为它没有和任何代码耦合在一起。接下来的第三部分，我们将会添加跳跃和一些其他的效果。

你可以在 GitHub Gist 上找到[完整的代码](https://gist.github.com/JavadocMD/b9d87c639953e19ea1943f550907b9aa).

---

译注：以下是完整代码，作者贴到了 github 上，没有写在原文中

> Inputs.cs

```csharp
using UnityEngine;
using UniRx;
using UniRx.Triggers;
using System;

public class Inputs : MonoBehaviour {
  // 单例
  public static Inputs instance;
	
  public IObservable<Vector2> movement { get; private set; }
  public IObservable<Vector2> mouselook { get; private set; }
  public ReadOnlyReactiveProperty<bool> run { get; private set; }
  public void Awake () {
    instance = this;

    // 隐藏鼠标指针，将其锁定在游戏窗口内
    Cursor.lockState = CursorLockMode.Locked;
    Cursor.visible = false;

    // 移动输入 tick 基于 fixedUpdate
    movement = this.FixedUpdateAsObservable()
    .Select(_ => {
      var x = Input.GetAxis("Horizontal");
      var y = Input.GetAxis("Vertical");
			
      return new Vector2(x, y).normalized;
    });

    // 鼠标视野 tick 基于 Update
    mouselook = this.UpdateAsObservable()
    .Select(_ => {
      var x = Input.GetAxis("Mouse X");
      var y = Input.GetAxis("Mouse Y");

      return new Vector2(x, y);
    });

    // 按下时奔跑
    run = this.UpdateAsObservable()
    .Select(_ => Input.GetButton("Fire3"))
    .ToReadOnlyReactiveProperty();

  }
}

```

> PlayerSignals.cs

```csharp
using UnityEngine;
using UniRx;

public abstract class PlayerSignals: MonoBehaviour {
  public abstract float strideLength { get; }
  public abstract IObservable<Vector3> walked { get; }
}
```
> PlayerController.cs

``` csharp
using UnityEngine;
using UniRx;

[RequireComponent(typeof(CharacterController))]
public class PlayerController : PlayerSignals {

  float walkSpeed = 5f;
  float runSpeed = 10f;
  float _strideLength = 2.5f;

  [Range(-90, 0)]
  public float minViewAngle = -60; // 玩家最低能看多少角度
	
  [Range(0, 90)]
  public float maxViewAngle = 60; // 玩家最高能看多少角度

  // 实现 PlayerSignal
  public override float strideLength {
    get { return _strideLength; }
  }

  private Subject<Vector3> _walked; // 我们自己看是 Subject

  public override IObservable<Vector3> walked {
    get { return _walked; } // 其他人看是 IObservable
  }

  CharacterController character;
  Camera view;

  void Awake () {
    character = GetComponent<CharacterController>();
    view = GetComponentInChildren<Camera>();

    _walked = new Subject<Vector3>().AddTo(this);
  }
	
  void Start () {
    var inputs = Inputs.instance;

    // 处理 wsad 的行走和奔跑效果
    inputs.movement
    .Where(v2 => v2 != Vector2.zero) // 如果移动量为0则忽略
    .Subscribe(inputMovement => {
			
      // 计算速度 （方向 * 速率）
      var inputVelocity = inputMovement * (inputs.run.Value ? runSpeed : walkSpeed);
			
      // 将 2D 的速度 转化为 3D 玩家的坐标
      var playerVelocity = 
        inputVelocity.x * transform.right +  // x (+/-) 对应右/左
        inputVelocity.y * transform.forward; // y (+/-) 对应前/后

      // 使用移动量
      var distance = playerVelocity * Time.fixedDeltaTime;
      character.Move(distance);

			
      // 移动产生信号
      _walked.OnNext(character.velocity * Time.fixedDeltaTime);

    }).AddTo(this);

    // 处理鼠标输入
    inputs.mouselook
    .Where(v2 => v2 != Vector2.zero) // 如果鼠标没动则忽略
    .Subscribe(inputLook => {
      // 将 2D 鼠标输入转化为欧拉角的转动量

      // inputLook.x 使角色绕纵轴旋转（+ 代表右转）
      var horzLook = inputLook.x * Time.deltaTime * Vector3.up * 100.0f;
      transform.localRotation *= Quaternion.Euler(horzLook);

      // inputLook.y 使相机绕横轴旋转 （+ 代表向上转）
      var verLook = inputLook.y * Time.deltaTime * Vector3.left * 100.0f;
      var newQ = view.transform.localRotation * Quaternion.Euler(verLook);

      // 我们必须在这里翻转最小/最大视角的标志和位置, 
      // 因为此处数学计算和角度相矛盾(+/- 对应下/上)
      view.transform.localRotation = ClampRotationAroundXAxis(
        newQ, -maxViewAngle, -minViewAngle
      );
    });
  }

  // 直接从标准资源中的 MouseLook 脚本中拿出来的(这真的是一个标准函数...)
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

> CameraBob.cs

```csharp
using UnityEngine;
using UniRx;

[RequireComponent(typeof(Camera))]
public class CameraBob: MonoBehaviour {

  public PlayerSignals player;

  float walkBobMagnitude = 0.05f;
  float runBobMagnitude = 0.10f;

  public AnimationCurve bob = new AnimationCurve(
    new Keyframe(0.00f,  0f),
    new Keyframe(0.25f,  1f),
    new Keyframe(0.50f,  0f),
    new Keyframe(0.75f, -1f),
    new Keyframe(1.00f,  0f)
  );

  Camera view;
  Vector3 initialPosition;

  void Awake () {
    view = GetComponent<Camera>();
    initialPosition = view.transform.localPosition;

    // 译注: 作者在 Inspector 界面进行配置，为了更好理解
    // 将获取脚本的代码写在了这。但这样使得代码变的耦合有利有弊
    player = transform.parent.GetComponent<PlayerSignals>();
  }

  void Start () {
    var distance = 0f;
    player.walked.Subscribe(w => {
      
      // 累计行走的距离（步幅的模长）
      distance += w.magnitude;
      distance %= player.strideLength;

      // 用 distance 设置相机的震动曲线
      var magnitude = Inputs.instance.run.Value ? runBobMagnitude : walkBobMagnitude;
      var deltaPos = magnitude * bob.Evaluate(distance / player.strideLength) * Vector3.up;

      //  调整相机位置
      view.transform.localPosition = initialPosition + deltaPos;

    }).AddTo(this);
  }
}
```