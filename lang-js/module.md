---
title: 基础 - Module
date: 2016-01-27
categories:
- [编程语言, JavaScript]

thumbnailImage: https://hd.unsplash.com/photo-1453230806017-56d81464b6c5
coverImage: https://hd.unsplash.com/photo-1453230806017-56d81464b6c5
---

学习和总结es6的语法，系列第一篇。写的不好，慢慢写

<!-- more -->

<!-- toc -->

## 准备工作

由于现在的浏览器还没有完全支持ES6的特性，所以我们需要自己搭建一个可以使用ES6语法的环境。
这里用到了比较基本的 npm (nodejs包管理工具) 和 webpack (模块加载器) 的部分。
需要简单带过一下。


### 使用npm 新建项目并安装依赖

``` bash
# 为我们的项目新建一个文件夹
$ mkdir use-es6
$ cd use-es6

# 用npm初始化一个项目
use-es6$ npm init -yes

# 为我们的项目安装需要的node包
use-es6$ npm i webpack -g --save-dev
use-es6$ npm i babel-loader babel-preset-es2015 --save-dev
```

**ps**: 虽然 webpack 本身就可以实现模块化，但是这里我们要使用 es6 的语法来进行模块化开发，所以我们需要使用 [babel](http://www.babeljs.io) 来进行语法转化。

### webpack 的基本配置

要使用的 node 包我们安装好了之后，我们还要将 babel 的转化功能添加到 webpack 中才能使用。新建三个文件。

``` bash
# mac
use-es6$ touch webpack.config.js index.js index.html

# windows
use-es6$ ni webpack.config.js
use-es6$ ni index.js
use-es6$ ni index.html

```
我们打开新建的 `webpack.config.js` 文件，添加如下代码

``` javascript
// webpack.config.js
module.exports = {
  entry: './index.js', // 我们的入口文件，需要自己新建
  output: {
    filename: './bundle.js' // 这是语言转化后打包的文件
  },
  module: {
    loaders: [
      {
        test: /.js$/,
        loader: 'babel',
        query: {
          presets: ['es2015']
        }
      }
    ]
  }
}
```

我们在 `index.html` 引入转化好的 `bundle.js` 文件这样我们就可以使用浏览器的控制台来查看我们写的程序了。

``` html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<script src="bundle.js"></script>
<body>

</body>
</html>

```

准备都做好了之后我们在终端执行监听，这样每当我们文件变化的时候 webpack 就会帮我们自动转化语法了

``` bash
use-es6$ webpack -w
# 因为是在监听文件所以这个窗口是不能关闭的
```

## 化繁为简 - 解构

在介绍模块语法之前，有必要简单对es6中对象（Object）的解构赋值进行一下了解。
我们定义一个 `food` 对象如下。我想从其中把 `meat` 拿出来作为一个新的变量。

``` javascript
var food = {
  meat: ['beef', 'pork', 'mutton', 'fish', 'shrimp'],
  fruits: {
    spring: ['apple', 'strawberry', 'cherry'],
    summer: ['watermelon', 'peach', 'litchi'],
    autumn: ['grape', 'hawthorn', 'sugarcane'],
    winter: ['orange', 'kiwifruit', 'banana'],
  },
  vegetable: {
    spring: ['leek', 'spinach', 'bamboo shoots'],
    summer: ['cucumber', 'tomato', 'eggplant'],
    autumn: ['sweet potato', 'carrot', 'celery'],
    winter: ['Chinese cabbage', 'radish', 'taro'],
  }
}

// before es6
var Meat = food.meet

// es6
var { meat: Meat } = food

// **很重要的一点**：
// 如果你要声明的变量名恰好和对象中的 `key` 相同，
// 就可以简写为
var { meat } = food
// 等同于
var { meat: meat } = food

```

解构的好处在于你可以使用清晰简便的语法声明多个变量，和深层次的变量

> 多变量

``` javascript
// before es6
var meat      = food.meat
var fruits    = food.fruits
var vegetable = food.vegetable

// es6
var { meat, fruits, vegetable } = food
```

> 深层次

``` javascript

// before es6
var winter = food.fruits.winter
var summer = food.vegetable.summer

// es6
var { fruits: { winter }, vegetable: { summer } } = food
```

这样结构变得十分清晰，再看看下面的例子里都代表着声明了那些变量?

``` javascript

var {
  fruits: {spring, summer: summer, autumn: autFruits },
  vegetable,
  vagetable: {autumn: autVegetable, winter},
  meat,
  meat: [beef, ...otherMeat]
} = food

/* ------------------- */

var spring       = food.fruits.spring
var summer       = food.fruits.summer
var autFruits    = food.fruits.autumn

var vegetable    = food.vegetable
var autVegetable = vegetable.autumn
var winter       = vegetable.winter

var meat         = food.meat
var beef         = meat[0]
var otherMeat    = meat.slice[1]

```

最后的 `meat` 用到了数组的解构赋值, 其实跟对象大同小异，有兴趣可以看看**变量**结构赋值的详细介绍 [链接](http://es6.ruanyifeng.com/#docs/destructuring)


## 正题 - es6 的模块系统

其实理解了对象解构，es6 模块的导入导出就基本已经搞定一半了，剩下就是记一些语法的事儿了。

1. 还用刚才写的那个 `food` 对象。（查了好久翻译的说 😂）新建一个 `food.js` 把它存到里面。然后我们想在 `index.js` 搞到这些吃的应该怎么办？ 首先人家要是不卖给你是没有办法的。所以我们先看如何将食物上架（导出）。

> 现在正值冬季，食材店的老板想卖一些**冬季的蔬菜水果**和**肉类**。

``` javascript
// food.js
var food = {
  ...
}

// 我们先拿到这些冬季的蔬菜水果和肉类

var {
  fruits: { winter: winterFruits }, // 冬季水果
  vegetable: { winter: winterVegetable }, // 冬季蔬菜
  meat // 肉类
} = food

// 导出
export { winterFruits, winterVegetable, meat }

// 上面是以下方法的简写，跟对象的结构赋值的情形类似，但是这里我们需要使用 as 这个关键字。

export {
  winterFruits as winterFruits,
  winterVegetable as winterVegetable,
  meat as meat
}

```


2. 食材已经上架了，我们想要买点蔬菜和肉。

``` javascript
// index.js

import { meat, winterVegetable } from './food.js'

```

**注意**：这里的变量名是与 `food.js`  中导出的变量名是一一对应的，如果你想为变量重命名还需要理解之前我们介绍的对象的解构, 只不过这里我们不再是对象了，所以我们需要使用一个关键字 `as` 来实现

``` javascript
// index.js

import { meat, winterVegetable as vegetable } from './food.js'

// vegetable => ['Chinese cabbage', 'radish', 'taro']
// meat => ['beef', 'pork', 'mutton', 'fish', 'shrimp']
```

同样我们在导出的时候也可以为变量起个别名

``` javascript
// food.js
...
export { meat as MEAT }
```

``` javascript
// index.js
import { MEAT } from './food'
import { meat } from './food'

// MEAT => ['beef', 'pork', 'mutton', 'fish', 'shrimp']
// meat => undefined

```

这样我们就可以做菜了。如果我们想要买到店里卖的所用的食物可以这样买

``` javascript

import * as AllFood from './food.js'

// AllFood =>
// {
//   meat: ['beef', 'pork', 'mutton', 'fish', 'shrimp'],
//   winterFruits: ['orange', 'kiwifruit', 'banana'],
//   winterVegetable: ['Chinese cabbage', 'radish', 'taro']
// }

```

**注意**：其实我们可以看到 `import` 关键字是可以声明变量的，用它来声明的变量的作用域在当前模块内。

3. 店家每天会推出一款特价食材，非常便宜。每天我都买来当晚餐。

``` javascript
// food.js
var food = {...}

var { meat: [ todayDiscount ] } = food

export default todayDiscount

```

买买买

``` javascript
// index.js

// 作为 default 导出的变量，在被导入时可以随意起名字
import myDinner from './food.js'

// myDinner > 'beaf'
```

在项目大的时候，模块可能会循环调用，但是前端遇见的情况比较少，我就不查了 ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

## 相关链接

- [阮一峰的es6电子书 - module](http://es6.ruanyifeng.com/#docs/module)
- [babeljs.io - learn es2015](http://babeljs.io/docs/learn-es2015/)
- [深入浅出ES6（十六）：模块 Modules](http://www.infoq.com/cn/articles/es6-in-depth-modules)

（完）
