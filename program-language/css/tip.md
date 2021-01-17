---
title:  tips
date: 2018-09-16
tag:
- css
---


15.跟随系统使用暗模式 (Safari 12.1)

``` css
body {
    color: black;
    background: white;
}

@media (prefers-color-scheme: dark) {
    body {
        color: white;
        background: black;
    }
}
```

14.当**手机**浏览器出现顶栏与底栏时，100vh不代表中间间隙

``` js
window.addEventListener('resize', function () {
  const vh = window.innerHeight * 0.01
  document.documentElement.style.setProperty('--vh', vh + 'px')
})

```

``` css
.full-height {
  
  height: calc(var(--vh, 1vh) * 100);
  height: 100vh; /* Fallback for browsers that do not support Custom Properties */
}
```
[原文](https://css-tricks.com/the-trick-to-viewport-units-on-mobile/)

13.文字少于1行居中显示，多余1行居左显示

``` css
div {
  text-align: center;
}

div p {
  display: inline-block; text-align: left;
}
```

12.在设置 `body { overflow-x: hidden; }` 后，个别浏览器会无法正确获取 `document.body.scroll`。
尝试使用

``` js
window.addEventListener('scroll', (evt) => {
  const offsetTop = window.srollY
  const offsetHeight =  window.innerHeight
})

```

11.thead 不能设置高度 要设置 thead tr/th 的高度, 如果使用flex布局，会使垂直居中无法生效

10.单行文本省略号（需要指定宽度）

```css
{
  text-overflow: ellipsis; 
  overflow: hidden; 
  white-space: nowrap; 
  /* width: some value */
}
```

9.clearfix

``` css
.clearfix::after {
  display: block;
  clear: both;
  content: "";
}
/* 没事别用浮动，容易上天。多尝试 flexible grid  */

```

8.单独改变列表标记的样式(ie7+)
``` css
ol, ul  { list-style: none; }
ol { counter-reset: item; }
ol li::before { content: counter(item) ". "; counter-increment: item; }
ul li::before { content: "-" }

/* 设置样式 */
.custom ul li::before,
.custom ol li:before {
  color: red;
  font-weight: bold;
}
```

7.iOS 低版本safari 的 button 标签对 justify-content 属性支持不够：无法居中。使用div代替 `移动端`

6.使容器滚动顺畅`移动端`
```css
.mobile-container { -webkit-overflow-scrolling: touch; }
```

5.隐藏滚动条 `移动端`
``` css
/*需要同时设置 width 和 display */
.container::-webkit-scrollbar {
  width:0; display: none;
}
```

4.父级元素有transform css属性，则其内部元素的 position: fixed; 样式会失效

``` css
body { transform: 'translate(0)'}
nav { position: fixed; }
```

3.阻止用户选中装饰性文字或图片
```css
img { user-select: none; }
```

2.强制文字折行：
```css
.word-container { word-break: break-all; }
```

1.阻止键盘顶起背景图：设置容器的 min-height 为 100%`移动端`
```css
.container { min-height: 100%; }
```