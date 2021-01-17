---
title: Flutter 布局与样式
date:  2018-08-21
tag:
- flutter
---

### 盒模型

``` dart


/* dart // css */
allWidgets(params) // box-sizing: border-box;

params.width: 240.0 // width: 240?

new Container(params); // box 以下属性只有 Container 才能配置


params.decoration: new BoxDecoration(
  color: Colors.black26
  // background - background-color: #262626;
  
  border: new Border.all(width: 10.0, color: Colors.black38);
  // border: 10? solid #383838;
  
  border: new BorderDirectional(bottom: new BorderSide(color: Colors.red, width: 1.0, style))
  // border-bottom: 1? solid red;

  borderRadius: new BorderRadius.all(new Radius.circular(8.0))
  // border-radius: 8?
)


params.margin: new EdgeInsets.all(4.0)
// margin: 4?
params.margin: new EdgeInsets.only(bottom: 8.0)
// margin-bottom: 8? 


params.padding: new EdgeInsets.fromLTRB(20.0, 30.0, 20.0, 20.0)
// padding: 30? 20? 20? 20?
params.padding: new EdgeInsets.symmetric(vertical: 2.0, horizontal: 5.0)
// padding: 2? 5?
```

### flex 相关
``` dart
/* dart // css */ 

new Row(params);
new Column(params);
// flex-direction: row;
// flex-direction: Column;

mainAxisSize: MainAxisSize
  .min
  ..max

params.mainAxisAlignment: MainAxisAlignment // justify-content
  .start         // flex-start; def  0  [col] 0 [col] 0 [col] 12
  ..end          // flex-end;        12 [col] 0 [col] 0 [col] 0
  ..center       // center;          6  [col] 0 [col] 0 [col] 6 
  ..spaceBetween // space-between;   0  [col] 6 [col] 6 [col] 0
  ..spaceAround  // space-around;    2  [col] 4 [col] 4 [col] 2
  ..spaceEvenly  // space-evenly;    3  [col] 3 [col] 3 [col] 3

params.crossAxisAlignment: CrossAxisAlignment // align-items
  .center        // center; def
  ..stretch      // stretch;
  ..start        // flex-start;
  ..end          // flex-end;
  ..baseline     // baseline;


new Expanded(flex: 2 /* default 1*/); 
// flex: 1; 不需要父容器 display: flex;

new Center(); 
// justify-content: center; align-items: center;
```


### grid

``` dart
/* dart // css */

```

### postition: absolute;

``` dart
/* dart // css */
new Stack(params);
params.alignment: const Alignment(0.6, 0.6);
// left: 60%; top: 60%;
params.children[0] // position: relative;
params.children[n] // position: absolute;
```


### 列表 

``` dart
/* dart // html or css*/
new ListView(params) // ul
param.children = [ new ListTile() ] // ul>li>title+subtitle+leading....

```


### 文字

``` dart
/* dart // css */
new TextStyle(params);

params.color: Colors.white         // color: white;
                                   // font: 900 24? Georgia;
params.fontSize: 24.0              // font-size: 24?
params.fontWeight: FontWeight.w900 // font-weight: 900;
params.fontFamily: "Georgia"       // font-family: Georgia;
```








### MaterialApp

``` dart
MaterialApp(
  debugShowCheckedModeBanner: [Boolean],  // 右上角条幅
  home: [Widget] // 默认widget
  theme: [ThemeData]
)
```

### Scaffold


``` dart

Scaffold(
  appBar: AppBar(
    leading: IconButton // 左侧图标区, 如果不设置可以自动触发左侧抽屉
    title: Text(''),    // 标题
    elevation: 2.0      // 阴影
    actions: <Widget>[] // 右侧图标区
    bottom: Tabbar
  )
)

```


#### TabBar TabBarView DefalutTabController
