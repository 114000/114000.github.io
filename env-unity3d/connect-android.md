---
title: Unity3D 与 Android 通信
date: 2017-07-10
tag:
- android
- unity3d
---

这篇文章主要记述**Android Studio 打出 jar 包供 Unity 使用的过程**，主要参考的链接就是这篇[《unity-与Android交互(unity5、android studio)》](http://www.voidcn.com/blog/yangxuan0261/article/p-6186822.html)

整个过程分为 `准备` - `code` - `打包导入`

## 一. 准备

Android Studio 和 Android SDK 的准备就不介绍了，这里出现了一个问题。当 SDK Tool 的版本为26时，Unity 将不能使用 SDK 打包。解决方法是降级 SDK。参考[链接](https://stackoverflow.com/questions/42538433/not-finding-android-sdk-unity#)

1. 创建新的 Android 工程

  **Note:** 实际上我们只需要创建 Module，但是其必须依赖于某个项目目录中，所以创建的项目名称和包名都可以随意填写。

  ![20170709204740.png](http://upload-images.jianshu.io/upload_images/711226-6204051c553115ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 之后一直**下一步**直至创建项目完成。此时我们点击 `File` - `New` - `New Module` 来创建新的模块

 ![$SG@KRX%7BC%YSHV6XET17M.png](http://upload-images.jianshu.io/upload_images/711226-2b648b9cc840f9ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 选择 Android Library  然后 Next。创建 Module 的名称可以随意填写，但是**包名要与使用该 Module 的 Unity 项目相同**

  ![588NUK$_118D74LR(K8~JX4.png](http://upload-images.jianshu.io/upload_images/711226-5f890ed323198cca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4. 将 Unity 中的 `class.jar` 文件放入 Module 的 `libs` 目录下，并为其添加依赖

  eg: `\Unity\Editor\Data\PlaybackEngines\AndroidPlayer\Variations\mono\Release\Classes` -
 `\AAA\nativeforandroid\libs`

5. 将此 `class.jar` 添加为依赖项，选中项目`右键` - `Open Module Settings`

  ![](http://upload-images.jianshu.io/upload_images/711226-e7ad551d4fac52f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  ![](http://upload-images.jianshu.io/upload_images/711226-d22cf8d7139b60ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

  ![](http://upload-images.jianshu.io/upload_images/711226-b7e118457e69ad2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

6. 修改 `build.gradle` 
   
 
  ![20170709213222.png](http://upload-images.jianshu.io/upload_images/711226-d0991a55c749aed4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  选中这个 Module 的 `build.gradle` 文件，在最下放加入以下代码
  
  ``` bash
  task clearJar(type:Delete){
    delete 'build/outputs/BB.jar'
    delete 'build/outputs/AndroidManifest.xml'
  }

  task makeJar(type:Copy){
    # 好多文章此处为 /bundles/release/ 但是我没有找到
    from('build/intermediates/bundles/default/')     
    into('build/outputs/')
    include('classes.jar')
    include('AndroidManifest.xml')
    rename('classes.jar','NativeForAndroid.jar')
  }

  makeJar.dependsOn(build) 
  ```

7.修改 AndroidManifest.xml
  `nativeforandroid/manifests/AndroidManifest.xml`
  ```xml
  <manifest 
    xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example">  <!-- 包名 -->

    <application
      android:allowBackup="true"
      android:label="@string/app_name"
      android:supportsRtl="true">
        <!-- 添加此 activity 标签 -->
        <activity android:name="com.example.Test"> 
          <intent-filter>
              <action android:name="android.intent.action.MAIN" />
              <category android:name="android.intent.category.LAUNCHER" />
          </intent-filter>
          <!--添加一下一行，否则 Unity打包时会报错-->
          <meta-data android:name="unityplayer.UnityActivity" android:value="true" />
        </activity>
    </application>
</manifest>
  ```

## 二. code

在 Module 中的 `Java/包名(没有标记)` 的文件夹下新建 Java Class。

eg: `Test.java`


![](http://upload-images.jianshu.io/upload_images/711226-34dadde217958212.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

``` java
package com.example;

import android.os.Bundle;
import android.widget.Toast;
import com.unity3d.player.UnityPlayerActivity;

public class Test extends UnityPlayerActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
  }


  // 定义一个显示Toast的方法，在Unity中调用此方法
  public void ShowToast(final String displayString){
    // 需要在UI线程下执行
    runOnUiThread(new Runnable() {
      @Override
      public void run() {
        Toast.makeText(getApplicationContext(), displayString, Toast.LENGTH_LONG).show();
      }
    });
  }
}

```

## 三. 打包导入



在 Android Studio 右上角找到 Gradle 按钮，在所在的模块下找到之前我们添加过的 `clearJar` 和 `makeJar` 命令


![K$X)B5BBEIAYID_1FT$NXDO.png](http://upload-images.jianshu.io/upload_images/711226-533d2bc6ff46ce4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

双击 `makeJar` 执行打包命令，等下方读条结束后，前往 `\AAA\nativeforandroid\build\outputs` 目录中找到打包好的 `AndroidManifest.xml` 和 `NativeForAndroid.jar`。将它们拖入 Unity 项目目录 `Assets/Plugins/Android/` 下


![](http://upload-images.jianshu.io/upload_images/711226-5d23257b8818c18d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 四. 调用

```csharp
using System.Runtime.InteropServices;

...

  void OnClick () {
     var jc = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
     var jo = jc.GetStatic<AndroidJavaObject>("currentActivity");

     jo.Call("ShowToast", "Toast"); // 函数名，参数
  }
...
```

#### 参考链接

- [Android Studio下打jar包及使用jar包](http://www.jianshu.com/p/1589be7962cd)
- [unity-与Android交互(unity5、android studio)](http://www.voidcn.com/blog/yangxuan0261/article/p-6186822.html)
- [unity 打包报错 Unable to list target platforms. Please make sure the android sdk path is correct. See the Console for more details.](https://stackoverflow.com/questions/42538433/not-finding-android-sdk-unity#)
- [gradle 最后需要加 makeJar.dependsOn(build)](http://blog.csdn.net/clever_jian/article/details/53097933?locationNum=2&fps=1)
- [AndroidStudio 导出关于Unity的Jar包](http://blog.csdn.net/u010019717/article/details/51762010)
- [Unity3D游戏开发之Unity与Android交互调用研究](http://blog.csdn.net/qinyuanpei/article/details/39348677)
- [Unity3D研究院之打开Activity与调用JAVA代码传递参数（十八）](http://www.xuanyusong.com/archives/667)
- [Unity Android Plugin开发指南](http://imgtec.eetrend.com/blog/8260)