---
title:  flex
date: 2016-01-04
tag:
- css
---

flexible box 布局的用法

<!-- more -->

<!-- toc -->

---

## 问题在哪

现代 UI 脱离纯文本的流式布局，需要更好的视觉和交互体验。而且手机和 pc 的功能差异让前端的所涉及的范围变得越来越广。

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout01.png)

如右侧的典型的手机 UI 布局，如果使用传统的定位、浮动的样式来完成将会十分麻烦。还有诸如像

- 子元素水平垂直居中
- 子元素百分比占宽
- 子元素两端对齐
- ...

这样的布局需求，没有点积累也没办法马上写出来。而 flex 布局会帮助我们解决这些问题。

## 兼容性

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout02.png)

截图自 [http://caniuse.com/#search=flex](http://caniuse.com/#search=flex)

<!-- more -->

ie 低版本的支持不是很好，但是移动端现在基本没有兼容问题，只需要为低版本的设备添加浏览器前缀。

## 样式

下面我跟随例子来了解一下，与 flex 相关的 css 样式。

### 准备

新建一个 html 文件（这里的代码都是准备工作，具体细节不用在意，flex相关的代码之后会有涉及）

``` html
<!-- flex.html -->
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"></head>
<style>
body {margin: 0; display: flex; justify-content: center;}

.pink { background-color: #E91E63; }

.orange { background-color: #FF5722; }

.blue { background-color: #00BCD4; }

.green { background-color: #009688; }

.container { width: 640px; background-color: #efefef; }

.block {
  width: 100px; height: 100px;
  border-radius: 20px; box-shadow: 1px 1px 3px #757575;
  font-size: 40px; text-align: center; line-height: 100px;
  font-weight: bold; color: #ffffff; border: 4px solid #ffffff;
}


</style>
<body>
<div class="container">
  <div class="block pink">1</div>
  <div class="block orange">2</div>
</div>
</body>
</html>
```

然后我们用浏览器打开页面，应该是这个样子的

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout03.png)

下面我们就可以正式开始了。

### `display: flex` 启动 flex 渲染

这个样式需要加在容器的上，这样容器内的元素才会遵从父容器的 flex 命令。

新添加一个 `.box`，然后为 div.container 添加这个 css 类。

``` css
.box {
  display: flex;
}
```

``` html
...
<div class="container box">
  <div class="block pink">1</div>
  <div class="block orange">2</div>
</div>
...
```

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout04.png)

这不就是浮动么，这尼玛是个骗局啊！(╯‵□′)╯︵┻━┻

> 一般 `flex` 都需要配合其他样式一块使用，否则跟浮动 `float` 没有什么区别  

我们看看第二个基本样式

### `justify-content` - 对齐内容

从字面意思理解这个样式一定是加给容器元素的，为子元素指定**水平**对齐方式

| 可选值 | 描述 |
| :------------- | :------------- |
| `flex-start`(默认) | 开始方向对齐（左对齐）|
| `flex-end` | 结束方向对齐（右对齐）|
| `center` | 水平居中 |
| `space-around` | 均匀分布 |
| `space-between` | 两端对齐 |

我们试着修改一下 `.box`，看看页面有什么变化

``` css
.box {
  display: flex;
  justify-content: flex-start; /* flex-end, center, space-around, space-between */
}
```
![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout05.png)

好像还蛮神奇！我们再看看第三个样式

### `align-items` - 对齐项目

这个也是加给父级的，用于**垂直**对齐容器内的多个项目，它不与 `justify-content` 冲突，

| 可选值 | 描述 |
| :------------- | :------------- |
| `flex-start`(默认) | 子元素在容器顶部对齐 |
| `flex-end` | 子元素在容器底部对齐 |
| `center` | 垂直居中 |
| `baseline` | 基线位置对齐 |
| `stretch` | 拉伸子元素以填满整个容器，**ps**: 在子元素没有指定高度的情况下会生效。 |

有了这个我们就可以非常容易的实现子元素的水平垂直居中。修改一下 `.box`

``` css
.box {
  height: 300px; /*给容器添加一个高度，*/
  display: flex;
  justify-content: center; /*水平居中*/
  align-items: center; /* 垂直居中 */
}
```
![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout06.png)

顶部对齐 (`flex-start`) 和底部对齐 (`flex-end`) 大同小异，试一下就能明白。我们最后看一下 `baseline` 将第一个子元素的 `line-height` 样式修改为 `50px`

``` html
<div class="container box">
    <div class="block pink" style="line-height: 50px;">1</div>
    <div class="block orange">2</div>
</div>
```
别忘修改一下 css

``` css
.box {
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: baseline; /* 文字基线对齐 */
}
```

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout07.png)

### flex-direction 布局方向

这个样式也是加给容器元素的，来影响子元素的排列方向

| 可选值 | 描述 |
| :--- | :--- |
| `row` （默认） | 横向 |
| `row-reverse` | 横向反转 |
| `column` | 纵向 |
| `column-reverse` | 纵向反转 |

我们再加一个小块可能会更明显一些

``` html
<div class="container box">
  <div class="block pink">1</div>
  <div class="block orange">2</div>
  <div class="block blue">3</div>
</div>
```

``` css
.box {
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center; /* 先修改回垂直居中 */
  flex-direction: row; /* row-reverse column column-reverse */
}

```
![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout08.png)

### flex 子元素占比

这个样式是加给子元素的，用来设定子元素占据父级的比例。

| 可选值 | 描述 |
| :--- | :--- |
| `<number>` | 子元素比例 |

> 容器元素会先将自身的宽度减去自身的内边距（padding）,减去没有定义比例的子元素(即没有给定 `flex: <number>` 样式)的宽度, 减去子元素的外边距（margin）所剩下的宽度再分配给使用比例的子元素身上。

太晦涩了，看看例子一目了然

``` css
.box {
  height: 300px;
  display: flex;
}

.酱油君 { /* 没有设定比例的子元素 */
  font-size: 28px;
  background-color: #a1887f;
}

.left-son-box {
  background-color: #f8bbd0;
  flex: 1;
  margin-right: 70px; /* 子元素有外边距 */
}
.right-son-box {
  background-color: #bbdefb;
  flex: 1;
}
```

``` html
<div class="container box">

  <div class="left-son-box">
    <div class="block pink">1</div>
    <div class="block orange">2</div>
  </div>

  <div class="right-son-box">
    <div class="block blue">3</div>
  </div>

  <div class="酱油君 block">酱油君</div>

</div>
```
![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout09.png)

目测这时两个 son-box 的比例还是 1: 1。

flex 也是可以嵌套了，我们来实现一个比较流（bian）行(tai) 的布局方式

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout11.png)


我们先把酱油君撵走 ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

``` html
<div class="container box">

  <div class="left-son-box">
    <div class="block pink">1</div>
    <div class="block orange">2</div>
  </div>

  <div class="right-son-box">
    <div class="block blue">3</div>
  </div>
</div>
```

``` css
.left-son-box {
  background-color: #f8bbd0;
  flex: 2; /* 左边的盒子占2份 */
  display: flex; /* 不要忘了加这个哈 */
  flex-direction: column;
  justify-content: space-around;
  /*
   *  由于使用 flex-direction 旋转了布局方向，
   *  现在justify-content 设定的就是纵向上的展现方式了
   */
  align-items: center;
  /*
   *  同样地原因 align-items 现在指定的是横向的样式
   */

}
.right-son-box {
  background-color: #bbdefb;
  flex: 1; /* 右边的盒子占1份 */
  display: flex; /* 不要忘了加这个哈 */
  justify-content: center;
  align-items: center;
}
```

我们看一下效果好像还可以奥

![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout10.png)


### order 子元素顺序

这个样式是子元素的，子元素的顺序值 `order` 越大，它的位置越靠后。

| 可选值 | 描述 |
| :--- | :--- |
| `<number>` （默认：0） | 子元素顺序 |

- order 的数值越高排序越靠后。。。

- 醉了，大哥你能不能说人话。(╯‵□′)╯︵┻━┻

- 😓我们还是举个🌰吧

我们稍微改以下布局

``` html
<div class="container"> <!-- 去掉 box 样式 -->
  <div class="box"> <!-- 两个box中包含的东西是一样的 -->
    <div class="left-son-box">
      <div class="block pink">1</div>
      <div class="block orange">2</div>
    </div>
    <div class="right-son-box">
      <div class="block blue">3</div>
    </div>
  </div>
  <div class="box">
    <div class="left-son-box">
      <div class="block pink">1</div>
      <div class="block orange">2</div>
    </div>
    <div class="right-son-box">
      <div class="block blue">3</div>
    </div>
  </div>

</div>
```

添加一条样式

``` css
/* 让第偶数个 .box 里的 .left-son-box 显示在右边 */
.box:nth-child(2n) .left-son-box {
  order: 1;
}
```
![](https://raw.githubusercontent.com/114000/114000.github.io/master/images/2015-12-29-flexibleBoxLayout12.png)

这样就很轻松的完成了左右交替的 flex 布局，使用 mvvm 框架的同学应该完全理解这样做的好处，
因为两个 `.box` 里的内容是完全一致的，做视图循环时不用考虑数据和视图的差异性啦。

这样比较实（ji）用（ben）flex 的样式就介绍到这里了，还有更多关于 flex 样式相关的东西可以看看下面的参考资料。
切忌钻到 flex 的布局的牛角尖里，很多时候以上的内容完全就可以应付。别让自己的代码变得难以维护。😂

## 更多

- [flexboxfroggy - flexible box 布局练习的小游戏](http://flexboxfroggy.com/)
- [Flex 布局教程：语法篇](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)
- [Flex 布局教程：实例篇](http://www.ruanyifeng.com/blog/2015/07/flex-examples.html)

（完）