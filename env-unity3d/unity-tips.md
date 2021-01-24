---
title: Unity Tips
date: 2016-10-10
tag:
- unity3d
---

- 淡入效果要设置初值，防止闪烁
- play 时设置的参数不会保存
- 通过 Inspetor - [Renderer] - Order in Layer 可以设置绘制顺序
- 脚本中暴露（`public`）的变量会出现在 Unity 的面板中
- 创建预制体（`prefab`）将 Hierachy 栏的 GameObject 拖拽到 Project 栏，然后删除原来的 GameObject 即可。
- C# 不指定值是默认为 `null`
- 在Unity中所有用到模型旋转的，其底层都是由四元数实现的，它可以精确地计算模型旋转的角度

---

- `Input.GetMouseButtonUp(0)` 鼠标左键抬起
- `[number]Time.realtimeSinceStartup` 从开始到当前帧经过的时间
- `[number]Time.deltaTime` 上一帧执行所消耗的时间
- `[fn]GameObject.SetActive` 设置显示状态（true/false）
- `[fn]GameObject.GetComponent<[component type]>` 返回组件或 `null`
- `[fn]GameObject.Find(string name)` 找到对应名称的游戏对象
- `[component]SpriteRenderder.color` [SpriteRenderer](https://docs.unity3d.com/ScriptReference/SpriteRenderer.html) 渲染2D图像精灵，[color](https://docs.unity3d.com/ScriptReference/Color.html): { r, g, b, a, gamma, grayscale, linear,

- Time.time：从游戏开始时计时，截止到目前共运行的游戏时间，受Time.timeScale影响，游戏暂停时该时间不增加。
- Time.timeScale：时间流逝的速度。当该值设置为1f时表示和现实中的时间流逝一致；当该值设置为0.5f时，表示真实时间逝去1秒时，游戏时间仅逝去0.5秒；当设置该值为2f表示真实时间逝去1秒时，游戏时间逝去2秒。
- Time.deltaTime：上一帧所消耗的时间。
- Time.fixedTime：每一次执行FixedUpdate()函数的时间间隔。可通过导航菜单栏 “Edit”➤“Project Settings” ➤“Time”菜单项设置。
- Time.fixedDeltaTime：固定更新上一帧所消耗的时间。
- Time.realtimeSinceStartup：从游戏开始时计时，截止到目前共运行的真实时间，不受Time.timeScale影响，游戏暂停时该时间仍然增加。

- Mathf.Abs(a)：返回*a*的绝对值，参数为整数或者浮点数。
- Mathf.Clamp(a,min,max) ：将*a*限制在min和max之间，参数为整数或者浮点数。
- Mathf.Lerp(from,to,a)：插入值，返回值=from + to(1-*a*)。
- Mathf.Min(a,b,c)：返回两个或*n*个数的最小值，参数为整数或者浮点数。
- Mathf.Max(a,b,c)：返回两个或*n*个数的最大值，参数为整数或者浮点数。

- Mathf.Pow(a,b)：*a*的*b*次方。
- Mathf.Deg2Rad：常量浮点数，0.0174532924f，用于角度转换弧度。
- Mathf.Rad2Deg：常量浮点数，57.29578f，用于弧度转换角度。
- Mathf.Pi：常量浮点数表示圆周率3.141592653...。
- Mathf.Sin(a)：返回弧度*a*的正弦值。
- Mathf.Cos(a)：返回弧度*a*的余弦值。
- Mathf.Tan(a)：返回弧度*a*的正切值。
通过Input.deviceOrientation可以得到当前游戏运行的朝向。
通过Input.touchSupported可以得到当前游戏是否支持手指触控操作。
通过Input.multiTouchEnabled可以设置游戏是否支持多点触控。


- Input.GetKeyDown(KeyCode.A)) : 按下键盘A键
- Input.GetKey(KeyCode.A)) : 按住键盘A键
- Input.GetKeyUp(KeyCode.A)) : 抬起键盘A键
- Input.GetKeyDown(KeyCode.LeftShift)) : 按下键盘左Shift键
- Input.GetKey(KeyCode.LeftShift)) : 住键盘左Shift键
- Input.GetKeyUp(KeyCode.LeftShift)) : 抬起键盘左Shift键
- Input.GetMouseButtonDown(0)) : 按下鼠标左键
- Input.GetMouseButton(0)) : 按住鼠标左键
- Input.GetMouseButtonUp(0)) : 抬起鼠标左键
- Input.GetMouseButtonDown(1)) : 按下鼠标右键
- Input.GetMouseButton(1)) : 按住鼠标右键
- Input.GetMouseButtonUp(1)) : 抬起鼠标左键

Input.acceleration.x 重力感应,类型为Vector3，每个轴向的值域是[-1,1]
Input.touches 手势输入
input.touches[0].fingerId 手指的编号，整型
input.touches[0].phase 手指的阶段，枚举类型。分为这几个阶段：Began开始接触屏幕、Moved移动、Stationary静止、Ended手指离开屏幕、Canceled系统关闭触控
input.touches[0].position 手指触碰屏幕的位置，Vector2类型。坐标以屏幕左下角为原点1像素对应一个单位，例如iPhone 4s的分辨率是960×640。所以如果应用是横屏的话，那么左下角的Position是（0,0），右上角的Position是（960,640）

脚本生命周期

- Awake()，脚本唤醒函数。当游戏对象被创建的时候，游戏对象绑定的脚本会在该帧（frame）内执行Awake()函数，无论脚本是否处于激活（enable）状态。
- Start()，该函数在脚本被激活的时候执行，位于Awake()函数之后。该函数的执行同样也是在游戏对象被创建的帧里。不同的是，如果脚本处于不激活状态（MonoBehaviour.enable=false），Start()函数是不会被执行的。
- Update()，只要处于激活状态下的脚本，都会在每一帧里调用Update()函数，该函数也是最为常用的一个函数，用来更新逻辑。
- LateUpdate()，该函数是延迟更新函数，处于激活状态下的脚本在每一帧里都会在Update()函数执行后调用该函数，通常用来调整代码执行的顺序。比如玩家的角色需要一个摄像机来跟随，那么通常角色的移动逻辑会写在Update()里。而摄像机跟随在LateUpdate()里，这样可以确保在角色的位置计算完毕后，再根据角色位置确定摄像机的位置和视角。
- FixedUpdate()，该函数用于固定更新。在游戏运行的过程中，每一帧的处理时间是不固定的，当我们需要固定间隔时间执行某些代码时，就会用到FixedUpdate()函数。在导航栏中，点击 “Edit”➤“Project Settings”➤“Time”菜单项，之后在Inspector视图里出现时间管理器，其中 “Fixed Timestep”选项用于设置FixeUpdate()的更新频率，更新频率默认是0.02秒，如图3-2所示。固定更新常用于移动物体等操作，因为固定更新每一帧调用的时间间隔是一样的，所以移动速度是均匀的。
- OnGUI()，绘制界面函数。因为Unity使用最新的uGUI界面系统来创建页面，所以OnGUI()一般作为测试功能使用，如创建测试按钮等。
- OnDestroy，在当前脚本销毁时调用该函数，我们可以在函数里填写删除时需要处理的逻辑。

脚本旁边的选框代表一个布尔值 enabled。enabled 只与生命周期函数有关，注释掉所有生命周期函数，选框将消失

![脚本中无生命周期钩子函数](http://upload-images.jianshu.io/upload_images/711226-eae2392698b49ecb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![脚本中有生命周期钩子函数](http://upload-images.jianshu.io/upload_images/711226-d8032b972e9ccb64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- OnEnable()，激活函数，当脚本被激活时（`enabled` 变为 `true`）调用。
- OnDisable()，当脚本被禁用时（`enabled` 变为 `false`）调用。




![图标左下角为脚本添加图标](http://upload-images.jianshu.io/upload_images/711226-9eda3ec45befdd6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


List 命名空间 `using System.Collections.Generic;`
Random 命名空间 `using Random = UnityEngine.Random;`


使用 Quaternion.RotateTowards 转动速度不能为负数，否则动画会抖动
## 学习链接

- [c# 泛型](http://www.blogjava.net/Jack2007/archive/2008/05/05/198566.html)
- [litJSON](http://bbs.9ria.com/thread-196437-1-1.html)
- [c# promise](https://github.com/Real-Serious-Games/c-sharp-promise)
- [unity promise](https://xldcode.github.io/2016/08/05/Using%20promises%20for%20Unity%20async%20operations/)
[ugui 事件捕获](http://www.woodenhouseso.com/article/2015/9/18/ugui_eventhandler_simpledesc)
[博客](http://gulu-dev.com/)
[3d text 穿透问题](http://blog.csdn.net/zkq666666/article/details/48707965)
[unity with protobuf-net](http://www.ceeger.com/forum/read.php?tid=13479)
[unity 整合 swift](http://www.jianshu.com/p/1a141e4fccb3?nomobile=yes)


[内存优化](https://onevcat.com/2012/11/memory-in-unity3d/)



### schma

[获取电量](http://www.voidcn.com/blog/u010019717/article/p-6244031.html)
[唤醒APP的那些事](http://www.jianshu.com/p/862885bd8ea2)
[android html唤醒APP（原生）](http://blog.csdn.net/daijin888888/article/details/50009387)
[Android 通过网页打开自己的APP(scheme)](http://blog.csdn.net/qduningning/article/details/37602101)



#### 热更新

[游戏研究院](https://zhuanlan.zhihu.com/pyluo)
[Unity3D热更新LuaFramework入门实战(1)——代码热更新](https://zhuanlan.zhihu.com/p/21386682)
[tolua 基础集成](http://www.gad.qq.com/article/detail/17149)

<http://blog.csdn.net/wwwsq/article/details/44123469>
<https://www.cnblogs.com/VariousCloudShadow/p/7241239.html?utm_source=itdadao&utm_medium=referral>
<http://blog.csdn.net/lyh916>


### 法线贴图

[crazybump](http://www.crazybump.com/)
[数字人C4D贴图雕刻UV之六：一张贴图搞定](http://www.360doc.com/content/16/1225/08/4740032_617447287.shtml)


### 苹果内购接入

Window - Services - in-APPPurchasing -> on

<http://m.manew.com/thread-100403-1-1.html>

<https://www.jianshu.com/p/d9d742e82188>

<https://zhuanlan.zhihu.com/p/32395810>

[iOS开发之推送警告but you still need to add "remote-notification" to the list of ](https://www.jianshu.com/p/e3176299fa54)

### ios 打包常见错误处理

![6C7A10CE409D918DF8844DAC14257327.jpg](http://upload-images.jianshu.io/upload_images/711226-49263fe1d84131d9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![6D52F2574F5823A84C2E7881A7823904.jpg](http://upload-images.jianshu.io/upload_images/711226-d75fd4972774cf78.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 脚本打包

[Unity脚本生成ipa或apk的方法](http://www.jianshu.com/p/a9261113b4ac)
[Unity3D研究院之Android全自动打包生成apk（六十九）](http://www.xuanyusong.com/archives/2748)
[Unity自动打包工具](http://blog.csdn.net/ynnmnm/article/details/36774715)


### 游戏字体过滤与位图字体制作

字体
- [谷歌字体](https://fonts.google.com/)
- [免费中文字体](http://www.pdadians.com/free-chinese-fonts-for-designers/)

字体制作工具
- [bmfont - Windows](http://www.angelcode.com/products/bmfont/)
- [bmGlyph - Mac](https://www.bmglyph.com/)


## 过滤掉字体文件中不需要的文字

> 需求：包含中文的字体包大小相对较大，而使用率很低。会占用过多的流量或存储空间

准备
1. 字体文件，如果是商用需要看好字体的协议否则倾家荡产
2. 保留的文字集合，保存到文本文件即可 [附：常用汉字3500](https://github.com/kaienfr/Font/blob/686f71695558996670a48dbf70027a55d4593507/learnfiles/%E5%B8%B8%E7%94%A8%E6%B1%89%E5%AD%97%E5%BA%93%203500.txt)

### 方法1：BMFont


- http://book.51cto.com/art/201504/473605.htm
---