---
# layout: post
title:  Background
date: 2018-06-29
sidebar: auto
tag:
- css
---

关于 css background 属性！关于颜色和渐变的方面的，再单独总结一篇 Color

本篇主要参考了[w3c的规范](https://www.w3.org/TR/css-backgrounds/#backgrounds) /（[中文](http://www.ayqy.net/doc/css2-1/colors.html#background)）

<!-- more -->
[[toc]]

---
## background-image

``` css
{ background-image: url("http://xxx.jpg"); }
```

|||
|---|---|
| 值 | `<背景图> [,<背景图>]*` 即一个或多个背景图像, 由逗号分隔 |
| 初始值 | `none`|
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式）|
| 计算值 | 由给定值决定 |
| 动画特征 | 无 |


**贴士**:
1. 可以绘制多张背景图像，设置在最前面的会绘制到最上层，最后设置的最接近背景色。
2. 即使设置的值为 `none`，宽高为0的图片，下载失败的图片或不能展示的图片（eg: 不支持的图片格式）。
仍然会创建图片层，但不会绘制任何东西。

  <!-- more -->

  eg: 实际绘制的背景层为 3

  ``` css
  {
    background-image: url(flower.png), none, url(grass.aaa);
  }
  ```

3. 在设置背景图像时对应设置一个背景色来应对图像无法获取的情况

  eg: 低版本浏览器不支持颜色渐变

  ``` css
  {
    background-color: red;
    background-image: linear-gradient(red #f00000);
  }
  ```
4. 图片有些时候无法正常显示，如在无图演示，或在高对比度模式中。所以不应该使用背景图像作为展示重要信息的唯一途径

#### 背景图可选值

1. `none`: 默认值，无背景图像，会生成图层但不会绘制任何东西
2. `url(<路径>)`: 指向图像的路径
3. `linear-gradient`: 线性变化
4. `repeating-linear-gradient`: 重复线性变化
5. `radial-gradient`: 径向变化

---

## background-color

``` css
{
  background-color: red;
}
```

|||
|---|---|
| 值 | `<颜色值>` |
| 初始值 | `transparent`|
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式）|
| 计算值 | 计算出的颜色值 |
| 动画特征 | 颜色值 |

**贴士**:

1. 背景色会显示在该元素所有[背景图像](#background-image)的下面
2. 背景色会与最底层的[背景图像](#background-image)共用同一个 [`background-clip`](#background-clip) 值


---

## background-repeat

``` css
{
  background-repeat: no-repeat;
}
```

|||
|---|---|
| 值 | `<平铺样式> [,<平铺样式>]*` |
| 初始值 | `repeat`|
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式）|
| 计算值 | 是一个`<平铺样式>`的列表，每一个`<平铺样式>`都包含两个代表维度的值 |
| 动画特征 | as repeatable list of sample list of length, percentage, or calc |

#### <平铺样式>可选值

``` css
{                                 /*   x轴方向      y轴方向  */
  background-repeat: repeat;      /*   repeat      repeat  */
  background-repeat: repeat-x;    /*   repeat    no-repeat */
  background-repeat: repeat-y;    /*  no-repeat    repeat  */
  background-repeat: no-repeat;   /*  no-repeat  no-repeat */
  background-repeat: space;       /*    space       space  */
  background-repeat: round;       /*    round       round  */
}
```

1. `repeat`: 重复平铺
2. `no-repeat`: 不重复平铺
3. `round`: 背景图像自动缩放直到适应且填充某个方向
4. `space`: 背景图像以相同的间距平铺且填充某个方向

**链接**：[更多关于 round, space 的介绍](http://chic.chicchina.net/shuxin/background-repeat.asp)

**贴士**：
1. `repeat`, `no-repeat`, `space` 和 `round` 可以任意两两组合赋值给 `background-repeat`
2. 有多个图像叠加但只有一组平铺参数时，这些图像共享一个 `background-repeat` 值

``` css
{
  background-image: url("cat.jpg"), url("dog.jpg");
  background-repeat: space no-repeat; /* 两张图片都只会在横向均匀分布开 */
  background-repeat: space no-repeat, no-repeat space; /* cat.jpg 在横向均匀分布开，dog.jpg 在纵向分布开 */
}
```

---

## background-position

|||
|---|---|
| 值 | `<位置> [,<位置>]*` |
| 初始值 | `0% 0%`|
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | 相当于背景位置的大小减去背景图像的大小（这样使用 50% 就会让图像居中，而不是图像的左上角在 50% 处，而长度单位不会有此效果）|
| 计算值 | 是一个`<位置>`的列表，每一个`<位置>`都是一对相对于左上角的偏移量，他们可以是长度也可以是百分量 |
| 动画特征 | 列表的`<位置>`使用的是长度，半分比，或者计算值（也就是使用 center 这样的关键字并不会触发动画） |

**贴士**：
1. 如果只给一个值，另一个则会被设置为 `center`

  eg:
  ``` css
  {
    background-position: 12px; /* 12px center */
    background-position: top;  /* center top */
  }
  ```
2. `<位置>`在使用两个关键字时可以重新排序，其中一个是长度和百分值就不会重新排序

  eg:
  ``` css
  {
    background-position: center left; /* left center */
    background-position: 20% left; /* 此样式不生效 */
  }
  ```
3. <位置> 可以指定从哪个方向来计算背景图像的偏移量
  eg:
  ``` css
  {
    background-position: left 10px top 15px;      /* 10px, 15px */
    background-position: left      top     ;      /*  0px,  0px */
    background-position: left      top 15px;      /*  0px, 15px */
    background-position: right 10px bottom 10px;  /* right 10px bottom 10px */
  }
  ```
4. <位置>设置为百分比值与设置为长度的区别

eg:
``` css
{
  background-position: 75% 50%;   
}

/*
|          75%            |    25%    |
|-------------------------------------|------------
| container     75%       |  25%      |
|           |-------------|-----|     |   50%
|           |             |     | 50% |
|-------------------------|-----------|------------
|           | background  |     |     |
|           |-------------|-----|     |
|                         |           |
|-------------------------------------|------------
|                         |           |
*/
```

- 定位区域的宽度的 75% 减去图片宽度的 75% 是背景图片距离左侧的偏移量
- 定位区域的高度的 50% 减去图片高度的 50% 是背景图片距离顶部的偏移量

图片的宽高是由 [`background-size`](#background-size) 决定的

---

## background-size

|||
|---|---|
| 值 | `<背景图像尺寸> [,<背景图像尺寸>]*` |
| 初始值 | `auto`|
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | 相当于背景位置的大小减去背景图像的大小（这样使用 50% 就会让图像居中，而不是图像的左上角在 50% 处，而长度单位不会有此效果）|
| 计算值 | 是一个`<位置>`的列表，每一个`<位置>`都是一对相对于左上角的偏移量，他们可以是长度也可以是百分量 |
| 动画特征 | 列表的`<背景图像尺寸>`使用的是长度，半分比，或者计算值（也就是使用 center 这样的关键字并不会触发动画） |
---

#### `<背景图像尺寸>`

> [ <长度> | <百分比> | auto ]{1,2} | cover | contain

1. contain: 在将背景图像较长的一边拉伸到 100%,
2. cover: 将背景图片较短的一边拉伸到 100%，


## background-attachment

|||
|---|---|
| 值 | `<attachment>`：`scroll`, `fixed`, `local` |
| 初始值 | `scroll` |
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式） |
| 计算值 | 由给定值决定 |
| 动画特征 | 无 |

- `fixed`: 固定在屏幕上，不随元素滚动
- `scroll`: 随着**元素本身**滚动
- `local`: 随着**元素内容**滚动, 并且定位在滚动内容上，不是元素上，即定位 bottom 后，滚动到最下方才会看到

ps:
1. `fixed` 属性值会将绘制背景的起始位置固定到 page box 上，与本身的 `background-origin` 不再有关系
2. `overflow: visible;` 也看不到 `fixed` 到元素外面的背景
## background-clip

|||
|---|---|
| 值 | `<盒模型>`：`border-box`, `padding-box`, `content-box` |
| 初始值 | `border-box` |
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式） |
| 计算值 | 由给定值决定 |
| 动画特征 | 无 |


``` css
element { background-color: red; }

/*

background-clip: border-box;

-----------------------
|         border-box  [background-color: red]
|   -------------------
|   |     padding-box [background-color: red]
|   |   ---------------
|   |   | content-box [background-color: red]
|   |   |


background-clip: padding-box;

....

background-clip: content-box;

-----------------------
|         border-box  [background-color: transparent]
|   -------------------
|   |     padding-box [background-color: transparent]
|   |   ---------------
|   |   | content-box [background-color: red]
|   |   |
*/

```

ps:
1. 根元素有着不同的背景绘制区，所以 `background-clip` 在根元素上不生效
2. 背景绘制总在边框的下方

## background-origin

|||
|---|---|
| 值 | `<盒模型>`：`border-box`, `padding-box`, `content-box` |
| 初始值 | `padding-box` |
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | N/A（无百分比形式） |
| 计算值 | 由给定值决定 |
| 动画特征 | 无 |


```css
element { 
  background-image: url('28x28.png'); 
  background-repeat: no-repeat;
}

/*

background-origin: border-box;

-------------------------
|[28x28.png] border-box
|   ---------------------
|   |        padding-box 
|   |   -----------------
|   |   |    content-box
|   |   |


background-origin: padding-box;

....

background-origin: content-box;

-----------------------
|         border-box
|   -------------------
|   |     padding-box
|   |   ---------------
|   |   |[28x28.png]
|   |   | content-box
*/

```

ps:
1. 如果 `background-attachment: fixed` 则此属性无效
2. 如果某个**方向**上有 `repeat` 属性，背景图会根据 `background-origin` 设定起始位置，但是它还是会在该**方向**上以图像填满背景

## background

|||
|---|---|
| 值 | `<bg-layer># , <final-bg-layer>` |
| 初始值 | 根据独立属性 |
| 适用 | 所有元素 |
| 是否继承 | 否 |
| 百分比形式含义 | 根据独立属性 |
| 计算值 | 根据独立属性 |
| 动画特征 | 根据独立属性 |

- `<bg-layer>` = ```

``` css
body { 
  background:
    red                  /* color: red */
                         /* image: none */
                         /* position: 0% 0% */
                         /* size: auto */
                         /* repeat: repeat, repeat */
                         /* attachment: scroll */
                         /* clip: border-box */
                         /* origin: padding-box */
  ;
}

p { 
  background: 
    url("chess.png")     /* image: url("chess.png") */
    40%                  /* position: 40% 50% */
    / 10em               /* size 10em 10em */
    gray                 /* color: gray */
    round                /* repeat: round round */
    fixed                /* attachment: fixed */
    border-box           /* clip, origin: border-box */
  ;
}


p {
  background: 
    red                  /* color: red */
    url("28x28.png")     /* image: url("28x28.png") */
    right 15px top 200px /* position: right 15px top 200px  */
    / 50px 50px          /* size: 50px 50px */
    no-repeat repeat     /* repeat: round repeat */
    fixed                /* attachment: fixed */
    border-box           /* origin: border-box */
    content-box          /* clip: content-box */
  ;
}


p {
  background: url(a.png) top left no-repeat,
              url(b.png) center / 100% 100% no-repeat,
              url(c.png) white;
}
/*
background-image:      url(a.png),  url(b.png),          url(c.png);
background-position:   top left,    center,              top left;
background-repeat:     no-repeat,   no-repeat,           repeat;
background-clip:       border-box,  border-box,          border-box;
background-origin:     padding-box, padding-box,         padding-box;
background-size:       auto auto,   100% 100%,           auto auto;
background-attachment: scroll,      scroll,              scroll;
background-color:      white;
*/

```



## 特殊的背景绘制

1. `::first-line` 与 `::first-letter` 伪类都被视为行内块，背景绘制不会充满一行（就算是块级元素包裹也不会）
2. 如果 `<html>` 没有指定颜色，则会用 `<body>` 的背景色填充页面


#### 最后

最近在看一本书（《CSS 揭秘》），里面介绍了样式表里很多细节的东西。这才发现自己每天太过关注于时髦事物，
忽略了基础技能的深化。我想这并不利于职业发展，索性放弃一些东西