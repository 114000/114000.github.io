---
layout: post
title: 初始化CSS
date: 2016-06-21
thumbnailImage: https://hd.unsplash.com/photo-1467348733814-f93fc480bec6
coverImage: https://hd.unsplash.com/photo-1467348733814-f93fc480bec6
categories: 前端
tag:
- CSS
---
css 初始化参考
<!-- more -->

<!-- toc -->

---

## 基本初始化

可以使用 [normalize.css](https://github.com/necolas/normalize.css/blob/master/normalize.css)

``` bash
npm install normalize.css --save
```

**Note:** `normalize.css` 的目的是将不同浏览器的相同元素的表现形式统一，而并不是清除所有的默认样式。

## 特例初始化(慎重使用)

``` css
/* 列表默认样式, li 元素本身没有样式 */
ul, ol {
  list-style: none; padding-left: 0; margin: 0;
}
/* 清除 td 元素的间隙, 此时 border-spacing 不生效 */
table {
  border-collapse: collapse;
}
/* 清除表单元素聚焦效果和边框 */
a, button, input, textarea {
  outline: 0; border: none;
}
/* 清除超链接的下划线 */
a {
  text-decoration: none;
}
```

## 关于移动端(慎重使用)

``` css
/* 字体太粗 */
body {
  -webkit-font-smoothing: antialiased;
}
/* 清除触摸元素后的阴影效果 */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-appearance: none;
}

/* ios默认文本框阴影 微信 number 有上下箭头 */
input, textarea, input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

/*  低版本安卓文本框层级问题  */
input:focus {
  -webkit-user-modify: read-write-plaintext-only;
}
```
