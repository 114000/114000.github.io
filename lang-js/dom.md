---
layout: post
title: 应用 - DOM
desc: 一些DOM相关的API 都在这里啦！⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄
date: 2015-09-07
categories:
- [编程语言, JavaScript]

thumbnailImage: https://hd.unsplash.com/photo-1441986380878-c4248f5b8b5b
coverImage: https://hd.unsplash.com/photo-1441986380878-c4248f5b8b5b
---

<!-- # Javascript DOM 操作 -->

这篇文章贴的是一些是针对Javascript DOM操作原生的常用API的总结。然后推荐一下[廖雪峰](http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000)先生的Javascript教程，涵盖了ES6的新特性。

<!-- more -->

<!-- toc -->

---

## 获取元素

### 通过对象的属性值获取元素

#### html
`document.documentElement`

``` javascript
// e.g.
document.documentElement.style.fontSize = '24px'
```

#### body

`document.body`

``` javascript
// e.g.
document.body.scrollTop = 0

```

*注意*：我们只能从 `document`下得到 `body`,`html` 元素

<!-- more -->

#### 表单元素

HTML 中 `form` 元素的 `name` 属性的值在 JS 中就代表了它自己，并不需要书写额外的代码，而这个 `form`
包含的表单也可以用同样的方式得到。

`[FormName]`

`[FormName][InputName]`

`[SelectElement].options`

> html

``` html
<form action="http://www.baidu.com/" class="testForm" name="myform">
  <input type="text" name="username" placeholder="请输入用户名">
  <input type="radio" name="sex" value="male">
  <input type="radio" name="sex" value="female">

  <select name="myselect">
    <option value="bj">北京</option>
    <option value="nj">南京</option>
    <option value="dj">东京</option>
  </select>

  <div name="danger"></div>
</form>

```

> javascript

``` javascript
myform
// object : form

myform.action
// => string : 'http://www.baidu.com/'

myform.class
// => error : undefined

myform.className
// => string : 'testForm'

myform.username.placeholder
// => string : '请输入用户名'

myform.sex
// => array: [input, input]

myform.inputs
// => error : undefined

myform.myselect.options
// => array : [option, option, option]

myform.danger
// => error : undefined

```

*注意*：在获取表单元素时，如果被定位的表单元素为一则返回一个元素(不是数组)，
如果表单元素为多个则返回一组元素

### 通过对象的方法获取元素

#### `document.getElementById(Id)`

*参数*

| 参数 | 形式 | 详细 |
|:---|:---:|:---|
|Id| `string` |你想要查找HTML中 `Id` 属性对应的元素|

*返回*

它返回一个与传入Id匹配的元素。当我们的页面中有多个相同id的元素时（这不是一个好的习惯），
它也仅仅只返回它查询到的第一个元素。

> html

``` html

<h4 id="imh4">test</h4>
```
> javascript

``` javascript
document.getElementById('imh4').innerHTML
// => test
```

*注意*：`getElementById` 仅为 `document` 的专有方法

#### `document.getElementsByName(name)`

通过标签的 `name` 获取一组元素

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|name|`string`|你想要查找HTML中`name`属性对应的元素|

*返回*
`array` - 返回一个包含对象的数组

> html

``` html
<form action="http://www.baidu.com/" class="testForm" name="myform"></form>

<div name="danger"></div>
```

> javascript

``` javascript
document.getElementsByName('myform')
// => array : [form]

document.getElementsByName('danger')
// => array : [div]

document.getElementsByName('none')
// => array : []

```

*注意*：`getElementsByName` 仅为 `document` 的专有方法


#### `[Element].getElementsByTagName(tag)`

通过标签名获取一组元素

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|tag|`string`|你想要查找HTML标签对应的元素|

*返回*
`array` - 返回一个包含获取到的对象的数组


#### `[Element].getElementsByClassName(class)`

通过标签的 `class`属性的值获取一组元素

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|tag|`string`|你想要查找HTML中 `class`属性对应的元素|

*返回*
`array` - 返回一个包含获取到的对象的数组

*注意*： 兼容IE8+

#### `[Element].querySelector(selector)`

用法类似JQuery

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|tag|`string`|你想要查找HTML中 `class`属性对应的元素|

*返回*
`object` - 返回一个获取到的对象

*注意*： 兼容IE8+

#### `[Element].querySelectorAll(selector)`

用法类似JQuery

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|selector|`string`|你想要查找HTML中 `class`属性对应的元素|

*返回*
`array` - 返回一个包含获取到的对象的数组

*注意*：兼容IE8+


*tip* - 通过class获取元素的封装函数，为了兼容IE8以下浏览器

> javascript

``` javascript
function getByClass(parent, classStr) {

  if(parent.getElementsByClassName)
    return parent.getElementsByClassName(classStr)
  else {
    var arr = []
    var elements = parent.getElementsByTagName('*')
    var hasClass = false

    for(var i = 0; i<elements.length; i++) {

      var tmp = element[i].class.split(/\s+/)

      for(var j = 0; j<tmp.length; j++) {
        if(classStr === tmp[i]) hasClass = true
      }

      if(hasClass) arr.push(element[i])
    }
  }

  return arr
}

// use

getByClass(document, 'danger')

// => array : [div]

```

---
## 创建元素

### 通过属性创建元素

#### `[element].innerHTML`

> javascript

``` javascript
// eg:
div.innerHTML = '<h1>Hello</h1>'
```

*注意*：该属性被赋予的值会直接渲染到页面上并覆盖原本的内容，对单标签元素无效

### 通过方法创建元素

#### `document.createElement(tag)`

*参数*

| 参数 | 形式 | 详细 |
|:----|:---:|:----|
|tag|`string`|想要创建元素的标签|

*返回*
`array` - 返回一个创建好的对象


*注意*：只有document元素可以使用该方法。如果想插入到页面中，我们还需要调用
`[element].appendChild(createElement)`方法将它插入到DOM🌲中 （它也是JSONP的实现方式）

---
## 元素的属性
### 一般属性

一般的属性值我们都可以通过 `.` 运算和 `[]` 运算来获取到活修改，例如

> html

``` html
<a id="link" href="http://www.jianshu.com/"></a>
<input type="text" name="myTxtInput" value="1">
```
> javascript

``` javascript
document.getElementById('link').href
// => string: 'http://www.jianshu.com/'

document.getElementsByName('myTxtInput').value = '2'
// '1' => string : '2'
```

也可以通过一些 **方法** 来操作 **自定义属性** ，当然他们对一般属性也是有效的

> javascript

``` javascript
[Element].getAttribute([attributeName])
[Element].setAttribute([attributeName],[attributeValue])
[Element].removeAttribute([attributeName])
```
需要说明的有以下特殊的几个

### [Element].className
className实际上就是标签的class属性，我们可以通过直接修改他的值来改变class

> javascript

``` javascript
div.className = 'col-xs-6 col-md-4'
```

也可以通过 `[element].classList` 进行操作，兼容IE10+

> javascript

``` javascript
div.classList
// => ['col-xs-6', 'col-md-4']

div.classList.add('col-offset-2')
// => ['col-xs-6', 'col-md-4', 'col-offset-2']

div.classList.remove('col-md-4')
// => ['col-xs-6', 'col-offset-2']

div.classList.contains('col-xs-6')
// => true
```

### [Element].style

我们会得到一个名为 `CSSStyleDeclaration` 的对象，最基础最直接的DOM操作是通过修改它来完成的

> javascript

``` javascript
div.style.color  = 'orange'
div.style.left = '100px'
```

就这样，当我们使用 `CSSStyleDeclaration` 这个对象的时候，我们在行内设置的样式会被添加到这个对象
中并附上索引值，如

> html

``` html
<div style="width: 100px; color: red">
```

> javascript

``` javascript
var div = document.getElementsByTagName('div')[0]
div.style.left = '100px'

div.style[0]
// => string : 'width'
div.style[1]
// => string : 'color'
div.style[2]
// => string : 'left'

```

这个对象里面的属性值大概变态多到300+，囊括了所有的样式在内，有的我也不知道有个鸟用，大家有空
一定要撸撸文档:stuck_out_tongue_closed_eyes:
