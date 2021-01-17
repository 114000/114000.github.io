---
title: SVG
date: 2018-06-26
---

Scalable Vector Graphics

栅格图形 raster graphics, vector graphics ，位图 bitmap

### 基本形状

画笔中心为坐标位置

**圆**
``` xml
<!-- <circle cx="70" cy="95" r="50" style="stroke: black; fill: none"/> -->
<circle cx="70" cy="95" r="50" stroke="black" fill="none" />
<circle cx="55" cy="80" r="5" stroke="black" fill="#339933" />
<circle cx="85" cy="80" r="5" stroke="black" fill="#339933" />
```

**椭圆**

``` xml
<ellipse cx="30" cy="80" rx="10" ry="20" stroke="black" fill="none" />
```

**矩形**

``` xml
<rect x="10" y="35" width="40" height="40" stroke="black" fill="none" />
<!--圆角矩形 rx ry-->
<rect x="40" y="60" width="20" height="40" rx="10" ry="5" />
```
rx ry 如果设置百分比是视窗的百分比不是矩形的百分比

**多边形**

```xml
<polygon stroke="black" fill="none"
    points="
      35,37.5 37.9,46.1 46.9,46.1 39.7,51.5
      42.3,60.1 35,55 27.7,60.1 30.3,51.5
      23.1,46.1 32.1,46.1" />
<!--五角星-->
```
**线**

``` xml
<line x1="75" y1="95" x2="135" y2="85" stroke="black" />
<line x1="75" y1="95" x2="135" y2="105" stroke="black" />
```

**折线**

``` xml
<polyline 
  points="108 62, 90 10, 70 45, 50 10, 32 62" 
  stroke="black" fill="none" />
<!-- 'M' 形状折线 -->
```

**路径**

``` xml
<path stroke="black" fill="none" 
  d="M 75 90, L 65 90, A 5 10 0 0 0, 75 90"/>
```

- M[X, Y] 移动
- L[Xaim, Yaim] 画线
- A[Xr, Yr, ?, ?, ?] 类圆
- 最后坐标点用于闭合

**文本**

```xml
<text 
  x="55" y="165" 
  font-family="Courier New" font-size="14pt" 
  stroke="none" fill="black">Cat</text>
```

**图片**

``` xml
<image xlink:href="aaa.jpg" x="72" y="92" width="160" height="120" />
```

### 分组
``` xml
<g id="whiskers">
  <line x1="75" y1="95" x2="135" y2="85" stroke="black" />
  <line x1="75" y1="95" x2="135" y2="105" stroke="black" />
</g>
```

有层的概念，这与叠加，减去顶层都有关系，层的顺序也决定图形的表现

### 复用

``` xml
<use xlink:href="#whiskers" transform="scale(-1, 1) translate(-140, 0)" />
```
### 定义

``` xml
<defs>
...
</defs>
只会定义 不会绘制
```

### style
**颜色**
颜色表示法与css一致

``` xml
<line x1="10" y1="30" x2="50" y2="20"
  stroke="red"
  stroke="#f00"
  stroke="rgba(255, 0, 0, .8)"
  stroke="hsla(360, 100%, 50%, .8)"
```

**stroke-width**: 画线宽度
**stroke-opacity**: 画线透明度（0-1）
**stroke-dasharray**: 虚线设置[线段长度，线段间隔长度]循环设置，eg:9，3，5。`-9-[3]-5-[9]-3-[5]-9-` 9长度线段，3长度间隙，5长度线段，9长度间隙，3长度线段，5长度间隙
**stroke-linecap**: 线头尾的形状 butt[default], round, square
**stroke-linejoin**: 线拐角处的形状 miter[default] 尖的， round, bevel 平的
**fill-opacity**: 填充透明度（0-1）
**fill-rule**:

### 单位
不写默认为 px

1. `em` 默认字体大小，通常为文本行高
2. `ex` x 字母的高度
3. `px` 像素 1/96 英寸
4. `pt` 点，1/72 英寸
5. pc 12点， 1/6英寸
6. cm, mm, in（英寸）

### 坐标系

第四象限笛卡尔坐标系

设置相对坐标

eg: 在 4cm * 5cm的画布上设置一个每厘米有16个单位的坐标系统（起始点为0，0）
``` xml
<svg width="4cm" height="5cm" viewBox="0 0 64 80">
```
