---
title: 将Spine动画导入unity3D
date: 2017-05-11
tag:
- unity3d

---

[Spine 官方指引](http://zh.esotericsoftware.com/spine-unity)

## 导入
1.拿到的动画文件有三个

```diff
fileName.altas // 图集的坐标文件
fileName.json  // 动画数据
fileName.png   // 图片
```
因为 unity 引擎不识别 `.altas` 文件后缀，所以我们需要把文件改成`fileName.altas.txt`

`补充: spine 可以直接设置后缀名称为 .altas.txt 2018.1.4`

2.接下来下载 spine 的 unity 支持 
github: [spine-runtime](https://github.com/EsotericSoftware/spine-runtimes), 将下载内容中的 `spine-csharp` 和 `spine-unity` 两个文件夹导入到unity

![github: spine-runtime](http://upload-images.jianshu.io/upload_images/711226-5a3cbb0ab521ab7a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3.将三个动画文件导入到unity中，unity-runtime 会另外生成3个文件

![导入成功](http://upload-images.jianshu.io/upload_images/711226-bcddaea5f7068385.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4.创建动画
在`Hierarchy` 面板中单击右键，选择 `spine` - `SkeletonAnimation`, 如果在UI(Canvas)中创建动画请选择  `spine` - `SkeletonGraphic`

![](http://upload-images.jianshu.io/upload_images/711226-a822c848abdc0429.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
将自动生成的 `fileName_SkeletonData` 拖拽到 SkeletonAnimation 组件的 SkeletonData Asset 属性上。然后选择AnimationName 属性中选择对应动画，运行即可播放。


![](http://upload-images.jianshu.io/upload_images/711226-c5ae586dc82c1d03.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 脚本控制

用脚本控制动画播放

``` csharp
using Spine.Unity;
using UnityEngine;

public class SpineAniController {
  SkeletonAnimation ani;
  SkeletonGraphic gph;

  public void Play (string aniName) {
    ani = ani ?? gameObject.GetComponent<SkeletonAnimation>();
    gph = gph ?? gameObject.GetComponent<SkeletonGraphic>();
    
    ani.state.SetAnimation(0, aniName, false);
    gph.AnimationState.SetAnimation(0, aniName, false);
  }

  public void PlayExample () {
    Play("chi");
    Play("peng");
  }
}
```