---
layout: post
title: "[译] ReactiveX 与 Unity3D <三>"
date: 2017-09-11
categories: Unity3D
tag:
  - Unity3D
  - csharp
---

[原文链接](http://ornithoptergames.com/reactivex-and-unity3d-part-3/)

- [第一篇](http://coloration.cc/2017/08/26/unity_csharp-ReactiveXandUnity3D-part1/)
- [第二篇](http://coloration.cc/2017/09/01/unity_csharp-ReactiveXandUnity3D-part2/)
- [第二篇附加篇](http://coloration.cc/2017/09/02/unity_csharp-ReactiveXandUnity3D-part2.2/)
- 第三篇

本系列的最后一篇文章。我们将会为玩家控制器添加跳跃功能及其声音的播放。效果如下(译注：youtube):

<iframe width="786" height="442" src="https://www.youtube.com/embed/6ZG7QQA9F8c" frameborder="0" allowfullscreen></iframe>

## Jumping to a conclusion

虽然将 WASD-移动的代码和控制跳跃的代码完全分离是十分诱惑的。但这会在每一帧中多次调用 CharacterController 的 Move 方法。就算是最好的情况也会浪费性能，更糟糕地，还可能会产生 bug。

而且它还会引起了其他问题：执行顺序和哪个行为该作为输出信号。而我们需要找到一个能将这些信号组合在一起，并一次计算完整移动的方法。组合信号是一个常有的需求，会有一些工具能给我们提供帮助的。最后我们选择 Zip，这个方法可以将两个（或多个）Observable 合并到一起，你可以在组合函数中运行并获取每个 Observable 的值。([这是查看奇妙交互图解的一个很好的时机](http://reactivex.io/documentation/operators/zip.html))

``` csharp
observableA.Zip(observableB, (a, b) => /*  在此组合 a,b */);
```

这个方法会返回给我们一个 Observable，它的类型是我们组合函数返回的类型。让我们用一个简单的结构体来打包一下输入值。

``` csharp
public struct MoveInputs {
  public readonly Vector2 movement;
  public readonly bool jump;

  public MoveInputs(Vector2 movement, bool jump) {
    this.movement = movement;
    this.jump = jump;
  }
}
```
这种定义结构体的方法会使代码变得冗长：通常的做法是保留结构字段的可变性，且不使用构造函数。但我觉得让结构字段变为只读是值得做的。因为你真的不会希望有人意外地或故意的来破坏你 Observable 中的值，不变性（Immutability ）是优点。 

现在我们知道该怎么组合东西了，那我们该如何定义我们的跳跃信号？你可能会这么做:

``` csharp
this.UpdateAsObservable().Select(_ => Input.GetButton("Jump"));
```

设想将它与我们的移动信号组合的情况。你能察觉到 bug 吗？回想一下，移动信号是每一次 Fixed Update 产生一次。Update 与 FixedUpdate 不是以相同速度运行的（除非可能是碰巧了）。然而 Zip 方法不知道这些信号的预期频率，它只是一个接一个的获取，耐心地等待慢信号将它“累积”到快信号上。在我测试的时候，跳跃命令会滞后，而且随着游戏进行越来越严重。我不确定 Zip 的内部缓冲区最终是否会溢出并崩溃，或者只是开始丢弃一些值。无论是哪一种都不太好。所以如果尝试简单地修复它的话，下面这样可以吗？

```csharp
this.FixedUpdateAsObservable().Select(_ => Input.GetButton("Jump"));
```

很遗憾也不行。输入采样与 Update 有关，所以我们在 FixedUpdate 采样会很容易丢失按键信息（或者帧率真的不太稳定，还可能计算多次按键）。所以我们还是得在 Update 阶段对输入进行采样，但是需要将按键状态保留至 Fixed Update，然后清除它。我从数字电路设计中获得了一些灵感，就是“锁存器（Latch）”。我们将使用自定义的 Observable 实现锁存器。输入的是数据信号- Jump 按键按下，锁信号会告诉我们何时应该产生输出 - Fixed Update 状态。

那么首先，我们怎么从头创建一个 Observable ? 因为到目前为止，我们都只是变换已经存在的 Observable。最基本的方式是使用 Create 方法，像这样。

``` csharp
Observable.Create<T>(observer => {
  // 使用 observer 实例实现 Observable 行为
  // 发送一个值: observer.OnNext(value)
  // 抛出异常终止: observer.OnError(exception)
  // 完成: observer.OnCompleted()

  // 返回 IDisposable, 用于释放我们创建的东西。
  return diposable;
});
```
这么看来真的是很开放的形式，实例给了你很大的自由度去实现各种行为的信号。你可以在里面使用其他的 Observable，你可以加载网站或者获取文件资源，你更可以什么都不做。这一切都取决于你。这里我会略过细节。但这对于要创建 Observable 的你来说是十分重要的。[*Intro to Rx* 是进一步了解这些东西的很棒的资源，包含了所有的细节](http://www.introtorx.com/Content/v1.0.10621.0/04_CreatingObservableSequences.html#CreationOfObservables) ，甚至还是用 C# 描述的。方便极了!
重点来了。锁存器 Observable 会在内部订阅我们的数据，并锁住信号，同样保持锁的状态。在我们开始写代码之前，先看看下面的状态图。

![Observable-Latch-Marble-Diagram.png](http://upload-images.jianshu.io/upload_images/711226-46894b8360198202.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

现在代码如下（译注：代码逻辑参考上图）：

```csharp
public static IObservable<bool> Latch(
  IObservable<Unit> tick,
  IObservable<Unit> latchTrue,
  bool initialValue) {

  // 创建一个自定义的 Observable.
  return Observable.Create<bool>(observer => {
    // 状态值
    var value = initialValue;

    // 创建一个锁存器的内部订阅
    // 只要锁存器触发，存储 true;
    var latchSub = latchTrue.Subscribe(_ => value = true);

    // 创建一个 tick 的内部订阅
    var tickSub = tick.Subscribe(
      // 只要 tick 触发，把当前值发送出去并重置状态
      _ => {
        observer.OnNext(value);
        value = false;
      },
      observer.OnError, // tick 报错则报错
      observer.OnCompleted); // tick 完成则完成

    // 如果我们创建的这个订阅被释放，那我们需要将内部的订阅也释放掉。
    return Disposable.Create(() => {
      latchSub.Dispose();
      tickSub.Dispose();
    });
  });
}
```

注意两个内部的订阅需要做好处理。否则它们的生命周期会超出需要的范围，造成内存泄漏和 CPU 的浪费。

对 tick 的订阅中还有一些我们没有处理的细节: 那就是 OnError 和 OnCompleted 处理函数。到目前为止，我们还没有看到一个可以抛出异常或被终止的 Observable。从 web 获取资源的 Observable 可以作为一个很好的例子：如果连接中断它会出错。如果成功则会触发一个值随即终止。Subscribe 的第二第三个参数可以让我们提供函数来处理其他情况。在此处，我不想自作聪明地对信号的错误和完成做任何处理。所以我只是将这两个函数传入 tick observer 里。所以只要 tick 抛出错误，那我们也同样报错。

你可能会质疑两个异步进程访问值的正确性。你的想法是对的，但是我觉得此处潜在的竞争条件造成的影响是可以忽略不记的(the same hand-waving I did over the run input, if you recall).


根据 Latch 的定义，我们终于可以把所有东西都放在一起来创建一个 IObservable<MoveInputs>：

```csharp
Jump = this.UpdateAsObservable().Where(_ => Input.GetButtonDown("Jump"));
var jumpLatch = CustomObservables.Latch(this.FixedUpdateAsObservable(), Jump, false);
MoveInputs = Movement.Zip(jumpLatch, (m, j) => new MoveInputs(m, j));
```

我们现在已经非常成功地协调了两个非常不同的信号：一个连续的（WASD键按住），一个瞬时的（空格按下然后释放）。

回到 PlayerController 中，我们将 ` inputs.Movement.Subscribe(...) ` 改为 `inputs.MoveInputs.Subscribe(...) `，其他的就顺水推舟了（完整的代码在下方）。

类似于我们控制器输出的 Walked 信号一样：我们同样可以在计算中加入 Jumped(跳跃) 和 Landed （落地）的信号。我们还可以使用一个 Walked 的订阅和一点点数学计算，就可以创建一个 Stepped （步）信号来模拟我们的脚步。我们需要这些来添加音效。

## Sounds to astound

没有为玩家提供音效简直就是一种伤害！不过感谢迄今为止所做的工作，这使得一切变得简单了。我们这里使用一个简单的 Unity 脚本，PlayerAudio，来配置 AudioClips 和 AudioSource，然后像下面这样订阅就可以了。

```charp
player.Jumped
  .Subscribe(_ => audioSource.PlayOneShot(jump))
  .AddTo(this);
```

这对我们之前的实现来说是十分优雅的回报。而且它不只限于音效，现在针对这些响应添加视觉效果或是AI触发器都是很容易做到的事情。我们可以很容易地监控玩家跳跃的次数，来通知成就系统。最重要的是，我们可以用健全的、可预测的、解耦的代码来完成所有这些工作。

## Conclusion

十分感谢你一步步地跟着做下来了！希望你对自己尝试这些技术感到兴奋。想要继续学习可以查阅 ReactiveX 提供的优秀的[文档（包括交互图）](https://github.com/neuecc/UniRx) 以及阅读免费的在线书籍 [*Intro to Rx*](http://www.introtorx.com/) 是入门和成为超级专业人士的好方法。

[你可以在 GitHub Gist  上找到反正的第三部分代码](https://gist.github.com/JavadocMD/ec0cb1c7a680f6760a82d3ddd44ba603)

> CustomObservables.cs

```csharp
using UniRx;
using UnityEngine;
public static class CustomObservables {
  public static IObservable<bool> Latch (
    IObservable<Unit> tick,
    IObservable<Unit> latchTrue,
    bool initialValue) {

    return Observable.Create<bool>(observer => {
      // 状态值
      var value = initialValue;

      // 创建一个锁存器的内部订阅
      // 只要锁存器触发，存储 true
      var latchSub = latchTrue.Subscribe(_ => value = true);

      // 创建一个 tick 的内部订阅
      var tickSub = tick.Subscribe(_ => {
        // 只要 tick 触发，把当前值发送出去并重置状态
        observer.OnNext(value);
        value = false;
      },
      observer.OnError,      // tick 报错则报错
      observer.OnCompleted); // tick 完成则完成

      // 如果我们创建的这个订阅被释放，那我们需要将内部的订阅也释放掉。
      return Disposable.Create(() => {
        latchSub.Dispose();
        tickSub.Dispose();
      });
    });
  }

  public static IObservable<T> SelectRandom<T>(
    this IObservable<Unit> eventObs, T[] items
  ) {
    // 边界值
    var n = items.Length;
    if (n == 0) {
      // 没有项目
      return Observable.Empty<T>();
    }
    else if (n == 1) {
      // 只有一项
      return eventObs.Select(_ => items[0]);
    }

    var myItems = (T[]) items.Clone();
    return Observable.Create<T>(observer => {
      var sub = eventObs.Subscribe(_ => {
        // 选择第一项之后的一项
        var i = Random.Range(1, n);
        var value = myItems[i];

        // 与索引值0的元素交换，避免重复选取
        var temp = myItems[0];
        myItems[0] = value;
        myItems[i] = temp;

        // 最后发送选中的值
        observer.OnNext(value);
      }, observer.OnError, observer.OnCompleted);

      return Disposable.Create(() => sub.Dispose());
    });
  }
}
```

> MoveInputs.cs

```csharp
using UnityEngine;
public struct MoveInputs {
  public readonly Vector2 movement;
  public readonly bool jump;

  public MoveInputs (Vector2 movement, bool jump) {
    this.movement = movement;
    this.jump = jump;
  }
}
```

> Inputs.cs

```csharp
using UnityEngine;
using UniRx;
using UniRx.Triggers;
using System;

public class Inputs : MonoBehaviour {
  // 单例
  public static Inputs instance { get; private set; }

  public IObservable<Vector2> movement { get; private set; }
  public IObservable<Vector2> mouselook { get; private set; }
  public ReadOnlyReactiveProperty<bool> run { get; private set; }
	
  public IObservable<Unit> jump { get; private set; }
  public IObservable<MoveInputs> moveInputs { get; private set; }
  
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

    // Jump: 在 Update 时采样
    jump = this.UpdateAsObservable()
    .Where(_ => Input.GetButtonDown("Jump"));

    // 但是需要锁住状态直到 FixedUpdate 才发送
    var jumpLatch = CustomObservables.Latch(
      this.FixedUpdateAsObservable(), jump, false
    );

    // 压缩跳跃和移动，这样我们就能在同一时间处理他们俩个了。
    // Zip 只能在这使用时因为 movement 和 jumpLatch 会以
    // 同样的频率发出信号: 即每次 FixedUpdate 时
    moveInputs = movement.Zip(jumpLatch, (m, j) => new MoveInputs(m, j));

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
  public abstract IObservable<Unit> landed { get; }
  public abstract IObservable<Unit> jumped { get; }
  public abstract IObservable<Unit> stepped { get; }
  
}
```

> PlayerController.cs

```csharp
using UnityEngine;
using UniRx;

[RequireComponent(typeof(CharacterController))]
public class PlayerController : PlayerSignals {

  float walkSpeed = 5f;
  float runSpeed = 10f;
  float jumpSpeed = 3f; // 译注: 调整跳跃速度使你能调到方块上
  float stickToGround = 5f;
  float _strideLength = 2.5f;
	
  [Range(-90, 0)]
  public float minViewAngle = -60; // 玩家最低能看多少角度
	
  [Range(0, 90)]
  public float maxViewAngle = 60; // 玩家最高能看多少角度

  // 实现 PlayerSignal
  public override float strideLength {
    get { return _strideLength; }
  }

  Subject<Vector3> _walked; // 我们自己看是 Subject
  public override IObservable<Vector3> walked { get { return _walked; } }

  Subject<Unit> _landed;
  public override IObservable<Unit> landed { get { return _landed; } }

  Subject<Unit> _jumped;
  public override IObservable<Unit> jumped { get { return _jumped; } }

  Subject<Unit> _stepped;
  public override IObservable<Unit> stepped { get { return _stepped; } }


  CharacterController character;
  Camera view;

  void Awake () {
    character = GetComponent<CharacterController>();
    view = GetComponentInChildren<Camera>();

    _walked = new Subject<Vector3>().AddTo(this);
    _landed = new Subject<Unit>().AddTo(this);
    _jumped = new Subject<Unit>().AddTo(this);
    _stepped = new Subject<Unit>().AddTo(this);
  }
	
  void Start () {
    // 这样就可以将 character 立刻固定在地面上，
    // 这样我们的第一帧就被称为“接地”。否则，我
    // 们在程序启动时会发生虚假的着陆。
    character.Move(-stickToGround * transform.up);

    var inputs = Inputs.instance;

    // 处理 wsad 的行走和奔跑效果
    inputs.moveInputs
    .Subscribe(i => {
      // 注意: CharacterController 是一个有状态的对象。
      // 但是只要只在这个函数中修改它, 我能确保事情会按
      // 预期发展
      var wasGrounded = character.isGrounded;

      // 玩家在 y 轴的垂直移动（跃起和受重力下坠）
      var verticalVelocity = 0f;
      if (i.jump && wasGrounded) {
        // 在地上并且要跃起
        verticalVelocity = jumpSpeed;
        _jumped.OnNext(Unit.Default);
      }
      else if (!wasGrounded) {
        // 在空中：需要重力下坠
        verticalVelocity = character.velocity.y + (Physics.gravity.y * Time.deltaTime);
      }
      else {
        // 否则我们就在地上：把我们往下推一点
        // （是为了让 character.isGrounded 产生效果 ）
        verticalVelocity = -Mathf.Abs(stickToGround);
      }

      // 玩家在 xz 平面上的移动
      var horizontalVelocity = i.movement * (inputs.run.Value ? runSpeed : walkSpeed);

      // 在玩家的坐标系中组合水平和垂直移动
      var playerVelocity = transform.TransformVector(new Vector3(
        horizontalVelocity.x, // 输入的 x (+/-) 对应着横向的 右/左 (玩家的x轴)
        verticalVelocity,
        horizontalVelocity.y  // 输入的 y (+/-) 对应着 前/后 (玩家的z轴)
      ));

      // 使用移动量
      var distance = playerVelocity * Time.fixedDeltaTime;
      character.Move(distance);

      // 输出信号
      if (wasGrounded && character.isGrounded) {
        // 这一帧，开始和结束时都在地上
        _walked.OnNext(character.velocity * Time.fixedDeltaTime);
      }

      if (!wasGrounded && character.isGrounded) {
        // 这一帧落地
        _landed.OnNext(Unit.Default);
      }

    }).AddTo(this);

    // 跟踪走动的距离来广播“步伐”事件
    var stepDistance = 0f;
    walked.Subscribe(w => {
      stepDistance += w.magnitude;
      if (stepDistance > strideLength)
        _stepped.OnNext(Unit.Default);

      stepDistance %= strideLength;
    }).AddTo(this);

    /* 译注：此处往下与第二部分的代码一致 */
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
      view.transform.localRotation = ClampRotationAroundXAxis(newQ, -maxViewAngle, -minViewAngle);
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

> PlayerAudio.cs

这段代码没试，大家有时间可以找几段音频测试一下

```csharp
using UnityEngine;
using UniRx;

[RequireComponent(typeof(PlayerController), typeof(AudioSource))]
public class PlayerAudio: MonoBehaviour {
  public AudioClip[] footSteps;
  public AudioClip jump;
  public AudioClip land;

  PlayerSignals player;
  private AudioSource audioSource;

  void Awake () {
    player = GetComponent<PlayerController>();
    audioSource = GetComponent<AudioSource>();
  }

  void Start () {
    player.stepped
    .SelectRandom(footSteps)
    .Subscribe(clip => audioSource.PlayOneShot(clip))
    .AddTo(this);

    player.jumped
    .Subscribe(_ => audioSource.PlayOneShot(jump))
    .AddTo(this);

    player.landed
    .Subscribe(_ => audioSource.PlayOneShot(land))
    .AddTo(this);
  }
}
```

> CameraBob.cs

```csharp
// 和第二部分没有区别
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