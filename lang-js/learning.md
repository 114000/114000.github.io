---
title: 概念
date: 2018-06-23
tag:
- javascript

writing: true
---

# 作用域
## 词法作用域 lexical scope

每当创建一个函数也就生成了一个词法作用域，只有函数的花括号能创建作用域

内层的作用域可以访问所有外层的变量直到全局变量

作用域内给为生命的变量命名，将会在全局作用域创建这个变量


### 执行环境

these in-memory scope structures are called execution contexts.
当程序运行时，创建一个用于保存变量和变量值的存储系统，这些内存中的作用域结构被称为执行环境

as the program runs, it will be building up internal data stores for keeping track of all the variables that are available to different function objects

a new execution context should be created every time you `run` a function. Thus,
for each lexical scope there may be many in-memory scopes created during execution,
or there may be none. It all depends on how many times you run a given function
in your code.


## 闭包 closure

every function should have access to all the variables from all the scopes that
surround(外围) it.

a closure is just any function that somehow remains available after those outer
scopes have returned.

一些函数通过某种方式可以随时被访问,  即使它的外部代码已经执行完毕


## this

`this` is an identifier that gets a value bound to it, much like a variable
`this` 是一个标识符 它需要和值进行绑定，跟变量差不多
But instead of identifying the values explictly in your code
但是在你的代码中，它并不是和某个具体值进行绑定
'this' gets bound to the correct object automatically
而是自动绑定到正确的对象上 

函数直到被调用时，才会得知 `this` 的指向 `obj.fn()` `fn` 内的 `this` 此时指向 `obj`

函数形参被调用前不会绑定任何值

点符号（或中括号）是我们为关键词 `this` 传入绑定的机制方法，如果没有点 `this` 会绑定到默认值上 `global`

`fn(r,g) = fn.call(this, r, g)`

每次调用 `new` 关键字都会创建一个新的对象


## Lesson 4 原型链

Prototype chains are a mechanism for making objects that resemble other objects
原型链是创建与其他 对象相似的对象的一种机制

When you want two objects to have all the same properties
当你为了节省内存或避免重复代码

either to save memory or to avoid code duplication
需要两个对象拥有完全相同的属性时

you might decide to copy every property over from one object to another
你可能需要从一个对象复制所有的属性到另一个对象

But as an alternative, JavaScript provides the option of prototype chains
但JavaScript 提供了原型链这种替代方式

This make one object behave as if it has all the properties of the other object
by delegating the field lookups from the first object to the second one

通过将一个对象中的字段查找委派于第二个对象的方式, 可以使得一个对象表现得似乎拥有另一个
对象的所有属性

`var a = Object.Create(b)` 依托于b为原型链的上游创建 a，访问a中不存在的属性会回溯到 b 中进行查找并返回

这并不是一个类似 `var a = Object.assign({}, b)` 这样的复制过程，此时a与b是完全独立的

原型链的源头是对象原型，它提供所有对象的共享方法 如 `toString` `hasOwnProperty` `constructor`

原型链有利于共享代码 节约内存

``` javascript
// no
var Car = function (loc) {
  this.loc = loc
  this.move = function () { this.loc++ }
} 
// yes

var Car = function (loc) {
  this.loc = loc
}

Car.prototype.move = function () {
  this.loc++
}
```

## Lesson 5 对象修饰模式
## Lesson 6 函数类

类名通常大写

the functions that produce these fleets of similar objects are called Constructor Functions.

because their job is to construct the objects that will qualify as members of the class
因为构造函数的工作就是构造同属一类的对象

So to recap, the class is the notion of a category of things that
you'd like to build and all of the entailed code that supports that category.

也就是说，类是指你要创建的某一类事物以及创建这类事物所需的代码。

``` javascript
var Car = function (loc) {
  var obj = { loc: loc }
  Object.assign(obj, Car.methods)
  return obj
}

Car.methods = {
  move: function () {
    this.loc++
  }
}
```

There aren't any interesting rules that will become active as result of the fact that we added a .methods property the the Car function.

我们向Car 函数添加.methods 属性的行为并不会导致任何有趣的规则生效

决定实例之间相似和不同之处的代码均包含在函数中，这是函数类的特点（优点和缺点）

## Chapter 7: 原型类


``` javascript
var Car = function (loc) {
  var obj = Object.create(Car.methods)
  obj.loc = loc
  return obj
}
```

Whenever a function is created. it'll have an object attached to it, that you can use as an container for methods just in case you plan on using that function, to build instances of a class.

无论什么时候，当一个函数对象被创建的时候 都会被附加一个对象属性，你可以把它当做一个方法容器 为了处理你把这个函数当做构建实例的类。

### prototype

``` javascript
var Car = function (loc) {
  var obj = object.create(Car.prototype)
  obj.loc = loc
  return obj
}

Car.prototype.move = function () {
  this.loc++
}
```

But in truth, nothing interesting has changed between at 'methods' and prototype.

So you should really see this .prototype object as a freely provided object for storing things with no additional special characteristics.(附加的特殊特性)


_试着理解 amy 的原型是 Car.prototype 和 Car 的原型是 Car.prototype 之间的不同_


### prototype.constuctor

Car.prototype.constructor => Car
amy.constructor => Car


### instanceof

the instanceof operator works by checking to see if the right operand's .prototype object can be found anywhere in the left operand's prototype chain

instanceof 运算符用于检查右侧运算对象的 .prototype 对象是否存在在左侧运算对象的原型链中


if methods were defined inside the constructor there really wouldn't be any reason to delegate the instances to any prototype at all.

如果方法已经在构造器中被定义,则完全没有理由将实例委托到任何原型中

## Lesson 8 伪类模式

the pattern we're about to build is called pseudo-classical because it attempts to resemble the class system from other languages by adding a thin layer of syntactic conveniences.

之所以称之为伪类，是因为它仿照其他语言中的类系统试图增添一些语法上的便利

Whenever we choose to use the keyword `new` in front of a function invocation, our function is going to run in a special mode called Constructor Mode

每当我们在一个函数调用前使用关键字 new ，该函数便会以一种特殊的模式--构造模式来运行

使用new 关键字会在函数的开头和结尾加上自动运行的代码

``` javascript
this = Object.create(X.prototype) 
return this
```

如果不使用new 则不会插入执行这些代码

``` javascript
var Car = function (loc) {
  this.loc = loc
}

Car.prototype.move () {
  this.loc++
}
```

实现上来说两种模式之间并没有本质区别，伪类模式只是原型模式的语法糖，

In fact, the primary difference between these two patterns is the number of performance optimizations that the JavaScript engines has implemented, that only apply when you're using the pseudo-classical pattern.

这两种模式之间的主要区别在于 JavaScript 引擎实现性能优化的数量。而这些优化是伪类所独有的

## Lesson 9 超类和子类

使用函数类实现 
``` javascript
var Car = function (loc) {
  var obj = { loc: loc }
  obj.move = function () {
    obj.loc++
  }
  return obj
}

var Van = function (loc) {
  var obj = Car(loc)
  obj.grab = function () {/*  */}
  return obj
}

var Cop = function (loc) {
  var obj = Car(loc)
  obj.call = function () {/*  */}
  return obj
}
```


## Lesson 10 伪类子类

``` javascript
var Car = function (loc) {
  this.loc = loc
}

Car.prototype.move = function () {
  this.loc++
}

var Van = function (loc) {
  Car.call(this, loc)
}

// no
Van.prototype = Car.prototype
// 子类在原型链上添加方法也会影响到超类的原型链
// no
Van.prototype = Object.create(Car)
// 混淆了构造器和原型链，实际上构造器（Car）也将自身委托给了原型链(Car.prototype)
// no
Van.prototype = new Car()
// 没有参数

// yes
Van.prototype = Object.create(Car.prototype)

Van.prototype.constructor = Van
// 由于Van的原型链委托给了Car的原型链，因此Van的原型链上缺失了自己的 constructor

Van.prototype.grab = function () {}
```


## Lesson 12 从像素到动画

### ImageData

- width (pixel)
- height
- data{Uint8ClampedArray - unsigned 8 bit number(0-255)}
  [r0, g0, b0, a0, r1, g1, b1, a1, r2, ....., rn, gn, bn, an]


createImageData: 初始化一个可修改的空的图像数据对象
GetImageData: 检索图像数据对象 in 背景画布
PutImageData: 存储图像数据对象 in 背景画布


`requestAnimationFrame`, only sends a request if the last frame is already finished drawing,
or the window is actively being viewed.(或窗口被主动查看) `setInterval` and `setTimeout`,
execute no matter what. so if your drawing takes a really long time to finish a single frame,
and your interval is really small, it can cause your browser to slow down or crash.

exLink:

[Kibo](https://github.com/marquete/kibo)
[“人类视觉和颜色感知”](http://micro.magnet.fsu.edu/primer/lightandcolor/humanvisionintro.html)



Part 2

## Lesson 1

针对移动设备的调试

安卓
打开开发者模式 setting - about device - click Build Number 7 times

chrome input chrome://inspect


https://github.com/google/ios-webkit-debug-proxy
https://www.smashingmagazine.com/2014/09/testing-mobile-emulators-simulators-remote-debugging/2/
http://www.css88.com/doc/chrome-devtools/


## Lesson 2 关键渲染路径 Critical Rendering Path

The Critical Rendering Path is the sequence of steps that the browser goes through to convert the HTML, CSS and JavaScript
into actual pixel on the screen.

关键渲染路径是指浏览器所经历的一系列步骤,从而将 HTML, CSS, JavaScript 转换为在屏幕上呈现的像素内容

First we grab the HTML and we start building the document object model. we then have to fetch the CSS and build the 
CSS object model. We combine those two to create the Render Tree. Then we have to figure out where everything
goes on the page, which the Layout step. And then finally we can paint pixels on the actual screen.

然后我们需要弄明白所有内容都位于网页的哪个位置

characters(tag) => tokens => nodes => dom

``` 
Characters      <html><head><meta>...
    |          
    |           # within the angle brackets has special meaning in HTML
    |           # it's set to be a tag. whenever we encounter a tag,
    |           # the browser emit a token.
    |
  Tokens        
    |           startTag: HTML, startTag: head, 
    |           startTag: meta, startTag:link
    |           endTag:head, startTag: body, 
    |           startTag: p, hello, endTag: p...
    |
    |           # this entire process is done by the tokenizer
    |           # 整个过程都由令牌生成器来完成
    |           # and while the tokenizer is doing this work,
    |           # the another process that is consuming these 
    |           # tokens and is converting then to node objects
    |
  Nodes                        
    |
    |           {startTag: HTML} token create [html] node,
    |           Then we consume the next token {startTag: head}
    |           and create [head] node. 
    |
    |           # the tokenizer emits start and end tokens,
    |           # which tells us the relationship between 
    |           # the nodes The startTag head token comes
    |           # before EndTag html token, which tells that
    |           # the head token is the child of html
    |
    |
   DOM        
    |                           [html]
    |                             |
    |                 ------------------------
    |                 |                      |
    |               [head]                 [body]
    |                 |                      |             
    |           -------------                |
    |           |           |                |
    |         [meta]  [link src="xx"]    [p style=""]
    |                                        |
    |                                      "Hello"
    |
    |           # Eventually, once we comsume all of the tokens,
    |           # we arrive at the document object model(DOM),
    |           # which is a tree structure that captures the 
    |           # <content> and <properties> of the HTML and all 
    |           # the relationship between the nodes.
  ```
将部分网页数据提前回传，是不错的提高速度的优化方式


##

<https://developers.google.com/web/tools/chrome-devtools/device-mode/?utm_source=dcc&utm_medium=redirect&utm_campaign=2016q3>


## Lesson 6 将 CSS 转换为css dom


characters(tag) => tokens => nodes => dom

``` 
Characters      
    |           body { font-size: 16px; } p { font-weight: bold; }
    |           span { color: red } p span { display: none }
    |           img { float: right }
    |          
    |           # The first thing the broswer has to do 
    |           # is identify the correct tokens.
    |
  Tokens        
    |           <below link>
  Nodes                        
    |
    |           # The parser would convert the tokens to nodes, 
    |           # and in this case, the first would be body
    |
  CSSOM        
    |                [body] ================= font-size: 16px
    |                  |
    |           ----------------
    |           |      |       |
    |           |      |     [img] ========== font-size: 16px*
    |           |      |                      float: right
    |           |      |
    |           |    [span] ================= font-size: 16px*
    |           |                             color: red
    |           |
    |          [p] ========================== font-size: 16px*
    |           |                             font-weight: bold
    |           |
    |         [span] ======================== font-size: 16px*
    |                                         font-weight: bold*
    |                                         display: none
    |       
    |
    |           # the children of the body note, inherit it's
    |           # parent's styling rules of sixteen pixel font
    |           # size. This is what we mean by cascading rules
    |           # (层叠规则) and cascading style sheets(层叠样式表).
  ```

[构建对象模型](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model#css-object-model-cssom)

我们不能像逐步处理 HTML 一样，只截取一部分 CSS tree 来加快页面的显示是因为。  

假设我们只收到部分 CSS 字节就开始构建 CSSOM。那么此后我们收取到相同选择的样式时。那我们就必须更改 CSSOM。这可能会使我们在渲染页面时使用了错误的样式。

the browser blocks page rendering. until it receives and processes all of the CSS. the CSS is render blocking


[阻塞渲染的 CSS](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-blocking-css)

虽然 CSSOM 是阻塞渲染的，然而如果选择器更为复杂更具体，则实际上会是浏览器必须去做更多的匹配工作。

the more specific rule is more expensive because it has to traverse more nodes in the DOM tree.
That said, before you go all crazy and rewrite all of your rules, measure first. Chances are selector
matching is not your performance model link. Measure first, optimize second.

有时候选择器匹配并不是性能瓶颈, 所以，先衡量再优化


使用 Dev-tool 中的时间轴工具，可以更好的调试和优化项目
<https://developer.chrome.com/devtools/docs/timeline#saving-and-loading-recordings>

# Lesson 9 The Render Tree 渲染树

渲染树会根据 DOM 树结构的顺序进行渲染，一边渲染一遍在 CSSOM 中查找对应的样式


样式 display: none 的节点及其子节点都被跳过渲染

the render tree captures both the content and the style



# Lesson 11 布局

``` html
<meta name="viewport" content="width=device-width">
```

What its doing is telling the browser that the width of the layout viewport should be equal to the device width. 

So, let's say that the devices width is 320 pixels. Then, if this meta viewport tag is present, the browser will set the layout viewport to 320 pixels and that will be our 100%

那么如果存在这个元视口的标记的话,


如果我们不使用这个标记的话浏览器会选择默认的视口宽度，通常为 980px。

inline 行内元素的宽度始终由其内容决定 

if the dimensions of the layout viewpoint change,
the browser has to rerun the layout step.
That's what happens every time you rotate your phone or, 
for that matter, resize your browser.

如果布局视口的尺寸更改了，浏览器就要重新运行布局步骤。每次旋转手机时或者重新调整浏览器的大小时，都会出现这种情况。

Recall that any time we update the render tree, either by modifying styles or the content, there's a good chance we have to rerun layout.

任何时候我们通过修改样式或内容来更新渲染树时, 很有可能就需要重新调整布局


a good rule of thumb is batch updates to avoid having multiple layout events

黄金法则是批量更新，避免出现多个布局事件



```html
<!DOCTYPE HTML>
<html>
<head>
  <link rel="stylesheet" href="css/style.css" type="text/css" />
  <script src="js/app.js"></script>
</head>
</html>
```

rendering steps

1. begin constructing the DOM by parsing HTML
2. request CSS & JS resources. 
3. Parse CSS and construct the CSSOM tree.the script is synchronous, we cant execute it until we have the CSSOM. So we'll need to create the CSSOM as soon as possible.
4. Execute JS. Completing the CSSOM will unblock the JavaScript engine, so we'll be able to execute JavaScript as soon as we've received it.

5. Once the JavaScript is finished, we can resume and finish constructing the DOM. Once we have the DOM and CSSOM, we'll merge the two and build the Render Tree.
6. run layout and paint the page

 CSS 压缩 - <https://developers.google.com/speed/pagespeed/service/MinifyCSS>
 内联和优化“关键 CSS” - <https://developers.google.com/speed/pagespeed/service/PrioritizeCriticalCss>


 # 优化

1. minify 注释和空行会被浏览器忽略掉，所以不需要保留。可以减少文件体积
[资源最小化](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer#minification-preprocessing--context-specific-optimizations)
2. compress 压缩 css 与 js 文件，[通过 GZip 进行的文本压缩](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer#text-compression-with-gzip)
3. cache 让浏览器做缓存 [http缓存](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)


构建渲染树，同时需要 DOM 和 CSSOM。所以至少这两者同时构建完，网页才能开始渲染

JavaScript 设计模式 https://cn.udacity.com/course/javascript-design-patterns--ud989

## 通过媒体查询取消阻止css

``` css
body { font-size: 16px; }

@media screen and (orientation: landscape) {
  .menu { float: right; }
}

@media print {
  body { font-size: 12px; }
}
```

[响应式 Web 设计的简介](https://developers.google.com/web/fundamentals/layouts/rwd-fundamentals/)
[呈现阻止 CSS](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-blocking-css.html)

``` html
<link rel="stylesheet" href="style.css">
<link ref="stylesheet" href="style-print.css" media="print">

<!-- media="print" -->
```

the broswer still downloads both style sheets, but it wouldn't block rendering on `style-print.css`. and in this
particular case it just means that the browser has to download less data for `style.css` which would help with
the download speed.

阻止渲染的意思是说，浏览器必须要将所有需要的 css 全部下载完才能开始渲染。因此是阻止渲染了这些css。
而通过媒体查询区别出的 css 不会被下载因此也就没有被阻止渲染

此处应该用阻塞渲染比较好理解

## JavaScript 与关键渲染路径 critical render path

``` html
<p>
  Awasome page
  <script>
  document.write('with JavaScript')
  </script>
  is awasome
</p>
```
First, the document parser creates a paragraph node and adds the text fragment.
Then it encounters the script tag, at which point it **pauses DOM construction** and
waits for JavaScript engine to execute the script. The script appends with JavaScript
and exits. At which point, you resume DOM construction and append is awesome text 
fragment. As a result, we get 'Awasome page with JavaScript is awasome' 


``` html
<style src="style.css" /> <!-- p { color: black }--> 
<p>
  Awasome page
  <script>
  document.write('with JavaScript')
  </script>
  is awasome
</p>
```

```
request page -- idle -- Build DOM ---blocked--- Build CSSOM --- Run JS --- Build DOM
    |                      
  GET html   ---------- response
                           |
                        GET css  -------------- response
```

浏览器请求 HTML，一旦获得响应，就开始构建 DOM 。然后发现 CSS 并发出请求，然后解析器继续操作并找到标记


``` html
<script src="analytics.js" async></script>
```

1. it tells the broswer that it doesn't have to block DOM construction. When it 
encounters the script size. As a result, the broswer dispatches the script request,
and continues parsing the DOM.

2. the execution of the script doesn't block on the CSS Object Module. So, if the
script is available before the CSS Object Module is ready. It can still be executed
right there and then.

内联js脚本无法使用 async 属性，它总会被 CSS 对象模型阻止。除非它在 css 上面执行。
也可以使用 [window.onload](https://developer.mozilla.org/zh-CN/docs/Web/API/GlobalEventHandlers/onload)/document.DOMContentLoaded 事件 ??? (好像CSSOM 没处理)

此外，你还可以向脚本标记添加 defer 属性，告诉解析程序脚本应该等到文档加载后执行。[详细了解 defer 属性](https://hacks.mozilla.org/2009/06/defer/)

[解析程序阻止与异步 JavaScript](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/adding-interactivity-with-javascript#parser-blocking-vs-asynchronous-javascript)

## 一般策略和 CRP 图标

1. minimize Bytes
2. Reduce critical resources (可以用媒体查询来避免阻塞的CSS, 用异步的方式避免阻塞的JS)
3. shorten CRP length(文件数量，文件大小，以及数据请求次数)

[优化关键渲染路径](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/optimizing-critical-rendering-path)
[关键渲染路径性能模式](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/analyzing-crp#performance-patterns)
[脚本标记的详细信息](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/script)
[如何交付可在一秒或一秒内呈现的页面](https://developers.google.com/speed/docs/insights/mobile)

## 具有外链 CSS 的 CRP 表

``` html
<html>
  <head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <p>Hello <span>web preformance</span> students!</p>
    <div><img src="awesome-photo.jpg"></div>
  </body>
</html>
```

CRP

```
   <T0>                   <T1>
request page ---idle--- Build DOM ---idle--- Build CSSOM - RenderPage  [Render process]
    |                      
  GET html   ----5kb--- response                                       [Network]
                           |
                        GET css  ----4kb---- response
```

关键资源:2
关键资源大小: 9kb
最低关键路径长度或来往次数: 2


``` html
<html>
  <head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <p>Hello <span>web preformance</span> students!</p>
    <div><img src="awesome-photo.jpg"></div>
    <script src="app.js"></script>
  </body>
</html>
```

CRP

```
   <T0>                   <T1>
request page ---idle---- Build DOM ----block---- Build CSSOM - RunJS - Build DOM - RenderPage  [Render process]
    |                      
  GET html   ----5kb---- response                                                              [Network]
                           |
      render blocking    GET css  ------4kb----- response
      parser blocking    GET js   ---2kb--- response
```

CSS 抵达后 浏览器开始构建 CSSOM 并放行了 JavaScript 并使其能够执行，在执行完 JavaScript 之后，DOM 解析器被放行，这意味着
DOM 的构建完成，最终我们获得了 DOM 和 CSSOM 表明我们可以渲染网页了

关键资源:3
关键资源大小: 11kb
最低关键路径长度或来往次数: 2

浏览器可同时下载 css 和 js 两个文件，所以最低关键路径长度为2

从下方链接中可以找到一些优化 CRP 的策略
[关键渲染路径](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)

```html
...
<script src="app.js" async></script>
...
```

`async` 属性得知 js 不会 block 关键渲染路径，也就不能称之为关键资源


## 预加载扫描程序 Preload Scanner

```html
<html>
  <head>
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link href="style.css" ref="stylesheet" />
    <script src="app.js"></script>
    <script src="timeing.js"></script>
  </head>
  <body>
    ......
  </body>
</html>
```

CRP

```
   <T0>                   <T1>
request page ---idle---- Build DOM ----block---- Build CSSOM - RunJS - Build DOM - RenderPage  [Render process]
    |                      
  GET html   ----5kb---- response                                                              [Network]
                           |
      render blocking    GET css  ------4kb----- response
      parser blocking    GET js   ---2kb--- response
      preloaded          GET js   --------- response
```

正常情况下 CSS 会阻塞 app.js 的执行，等到 CSSOM 构建完成才会执行 app.js, 进而在请求 timing.js。而浏览器实现的 Preload Scanner
会在 CSSOM 阻塞js的时候预扫描剩下的代码，并提前加载其余js

[“浏览器预加载程序如何加快页面加载速度”](http://andydavies.me/blog/2013/10/22/how-the-browser-pre-loader-makes-pages-load-faster/)