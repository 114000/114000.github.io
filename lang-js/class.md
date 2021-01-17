---
title: 基础 - Class
date: 2016-04-10
categories:
- [编程语言, JavaScript]
---

最近一直在忙没有时间去写东西，苦逼。今天总结一下 `Class` 的使用方法。[最下方](#editing-code)有搭建es6书写环境的简易方法

<!-- more -->

前一篇是[ES2015 系列之一 - Module](http://114000.github.io/2016/01/27/es2015Module)

<!-- toc -->

---

## 首先

首先我们要区分以下3样东西：`类、类的实例、“Object”类的实例`

``` javascript
// 类
class Dog {
  ...
}

// 子类
class Husky extends Dog {
  ...
}
```

``` javascript
// 类的实例
const david = new Dog()
const cota = new Husky()

```

``` javascript
// 对象（Object 类）的实例
const something = {
  "aaa": "xxx",
  "bbb": false,
  "ccc": [],
}
// 数组 （Array 类）的实例
const arr = [1, 2, 3, 4]
```

我们要注意一下写法规范，类的首字母一般都要大写，而实例的首字母一般需要小写

## 类的声明与继承

那么今天介绍一下与类相关的语法。新建一个文件 `dog.js`：

``` javascript
// dog.js

class Dog {

}
// or
const Dog = class {

}

export default Dog // 不要忘了导出

```

以上是两种声明类的方式。继承也十分简单：

``` javascript
// husky.js
import Dog from './dog' // 不要忘了导入

class Husky extends Dog {

}

// or

const Husky = class extends Dog {

}

export default Husky // 不要忘了导出
```

我们看一下效果：

``` javascript
// index.js
import Dog from './dog'
import Husky from './husky'

const david = new Dog()
const cota = new Husky()

console.log(david instanceof Dog)
// boolean: true => david 是 Dog 类的实例
console.log(cota instanceof Husky)
// boolean: true => cota 是 Husky 类的实例
console.log(cota instanceof Dog)
// boolean: true => cota 是 Dog 类的实例，因为 Husky 类继承自 Dog
```

## 静态方法

`静态方法`就是可以在类上直接使用的方法。与实例无关，我们修改一下 `dog.js`：

``` javascript
// dog.js

class Dog {
  // 狗的平均寿命有 8 岁
  static averageLife () {
    return 8
  }
}
```

``` javascript
// index.js
...
console.log(Dog.averageLife())
// boolean: 8
```

`static` 就是标记`静态方法`的关键字，平时我们会使用很多静态方法 ，比如 `Math.random()` `Date.now()` `Object.assign()` 等。 静态方法是可以被子类继承的：

``` javascript
// index.js
...
console.log(Husky.averageLife())
// boolean: 8
```

## 静态属性

类除了有静态方法，也有静态属性。和静态方法类似，它也会被子类继承。但是 es6 并不支持在类中直接声明静态属性，但我们可以通过在外部添加的方式：

```  javascript
// dog.js
class Dog {
  ...
}
// 添加静态属性
Dog.tag = 'animal'
Dog.friend = 'Cat'
```

``` javascript
// index.js
...
console.log(Dog.tag, Dog.friend)
// string: 'animal', string: 'Cat'
console.log(Husky.tag, Husky.friend)
// string: 'animal', string: 'Cat'
```

每个类都有一个默认的静态属性 `name`

``` javascript
console.log(Dog.name, Husky.name)
// string: 'Dog', string: 'Husky'

```

## 实例方法

我们修改一下 `dog.js`，声明一个不带 `static` 关键字的函数 `bark`:

``` javascript
// dog.js
class Dog {
  static averageLife () {...}

  bark () {
    console.log('wang! wang!')
  }

}
...
```

这样一来我们之前“介绍” 的 david 和 cota 就都会汪汪叫了

``` javascript
// index.js
...
david.brak(),
// string: wang! wang!
cota.brak()
// string: wang! wang!
```

我们不能让写在字典或者百度百科里的犬科，或者哈士奇这样的品类介绍发出叫声，只有某一只真是的狗才会叫，这就是实例方法。
但具体到某个家庭养的狗，差异性很大，我们知道大部分的狗可都会叫，但是可能金毛犬就很少吠叫，那么我们看看如何使用代码来描述这个现象。

我们新建一个文件 `goldenRetriever.js`：

``` javascript
// goldenRetriever.js
import Dog from './dog'

export default class GoldenRetriever extends Dog {
  brak () {
    console.log('Hm.. Hm..')
  }
}
```

对，我们就是用自身的实例方法来覆盖 Dog 中的 `bark` 方法。

``` javascript
// index.js
...
import GoldenRetriever from './goldenRetriever' // 别忘了引入

...

const jim = new GoldenRetriever()

jim.bark()
// string: 'Hm.. Hm..'
```

jim 没有发出汪汪的声音，我们用自己的实例方法覆盖掉了父类中对应的实例方法。

那么哈士奇不但会汪汪叫，还会狼嚎，那我们改怎么办呢？

``` javascript
// husky.js
import Dog from './dog'

class Husky extends Dog {
  bark () {
    super.bark()

    console.log('Ho!~ Ho!~')
  }

}
...
```

实验一下就会发现 cota 已经会狼嚎了诶，这里的 `super` 是父类的实例，这里面我们调用了父类实例的 bark 实例方法，这样就省去我们在为哈士奇添加“汪汪”的叫声了

## 构造函数

构造函数会在每个类中自动添加，就像这样

``` javascript
class Husky extends Dog {
  // // // // //  
  constructor () {
    super() // 这里的 super 是父类的构造函数
  }
  // // // // //

  bark () { ... }

}
```

注释之间的 `constructor` 是类的默认行为，所以在我们不需要覆盖掉构造函数的时候就可以不写，而如果我们想要使用 `this` 时, 就必须重写（覆盖）构造函数，并在它第一行执行 `super` 。
你们有没有听过哈士奇说 ‘I love you’? 没错 misa 就是这样一只哈士奇。哈士奇可真是一个神奇的物种！

``` javascript
// husky.js
export default class Husky extends Dog {
  constructor (canSayWhat) {
    super()
    this.canSay = canSayWhat
  }
  bark () { ...}
  say () {
    console.log(this.canSay)
  }
}

```

上面的代码是为哈士奇这个种类添加了说话的本领，但会说什么就是天赋的事儿了。misa 可是天生就会说 'I Love You!' 的：

``` javascript
// index.js
...

const misa = new Husky('I Love You!')

misa.say()
// string: 'I Love You!'

```

**注意**：这里需要说明一下构造函数中的 `this` 就是实例本身，所以 `this.canSay` 就是某个实例的一个`实例属性`

## get 和 set

狗和人一样都有年龄的，而且每年都在增长，而且一般超过 10 年的老狗身体状况就越来越不好了。而实际上 es5 以前并不能有效地监听实例属性的变化，
也就是说我们虽然能修改年龄，但实例本身并不能知道年龄的增长。但是 es5 之后新增了 get 和 set 函数从而解决了这个问题。那我们直接来看看如何使用。

``` javascript
// dog.js

class Dog {

  constructor () {
    // 最原始的类不用调用 super
    this._age = 0
  }

  get age () {
    return this._age
  }

  set age (nowAge) {
    this._age = nowAge

    if (nowAge > 10) console.warn('it\'s an old dog');
  }

  static averageLife () { ... }

  bark () { ... }
}

...
```

我们先看一下 misa 现在的年龄，然后再修改一下看看会发生什么

``` javascript
// index.js

console.log(misa.age) // 此处调用了 get 函数
// number: 0

misa.age = 1 // 此处调用了 set 函数

console.log(misa.age) // 此处调用了 get 函数
// number: 1

misa.age = 12 // 此处调用了 set 函数
// string: 'it's an old dog'
// number: 12

```

实际上就是这么简单就实现了，不知道有一点你注意到了没？get set 方法的名字（`age`）与实例属性的名字（`_age`）并不相同，你知道为什么么？

**注意**：

1. 这两个名字不同的原因是为了防止循环调用而导致程序崩溃，比如，get 函数中如果返回的是 `return this.age` 这个句法，那么就还是会再调用一次 get 函数，就是无穷的的递归了。同理 set 函数也是这样
2. `_age` 作为不想被外部直接读取（私有）的实例属性前面最好加上下划线标记一下，如果也有不想被外部读取（私有）的实例方法前面也要加上下划线 `_`。（这是一个写法规范，实际上还是能调用到的）

## 最后

我们已经可以用 es6 的语法进行简单的面向对象的编程了，最后再总结一下：

1. 类的声明和继承 - `class`， `extends`
2. 类的静态方法和静态属性 - `Dog.averageLife()` `Dog.friend` 而且可以被子类继承,
3. 实例的实例方法和实例属性 - `new`，私有的前面要加 `_`，可以通过 `super.bark()` 调用父级的实例方法
4. constructor 和 super - 在写实例属性的时候，必须在 contructor 第一行调用 super，如果是最顶级的类可以不写
5. get 和 set - 提供了修改实例属性的方法

## 更多

- [阮一峰《ECMAScript 6 入门》](http://es6.ruanyifeng.com/#docs/class)
- [ECMAScript 下个版本要支持的特性](https://github.com/tc39/ecma262)

---

## 最后贴一段环境的搭建方法

1. [nodejs.org](https://nodejs.org/en/download/) 网站下载 node 环境的安装包，然后无脑安装。
2. 打开命令行工具，终端或者 powershell，升级 npm： `npm install npm -g`
3. 新建一个文件夹 `mkdir use-es6-class`，并进入 `cd use-es6-class`。并且初始化项目 `npm init -yes`
4. 使用npm 安装几个包:
  * 全局安装一个包 `npm install webpack -g --save-dev`
  * 局部安装两个包 `npm install babel-loader babel-preset-es2015 --save-dev`

5. 在文件夹中新建三个文件并添写代码 `index.html`， `index.js` 和 `webpack.config.js`（文件的代码最后贴出）
6. 执行命令 `webpack -w`
7. 在 `index.js` 中编写代码即可

> index.html

``` html
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

> index.js 空的

> webpack.config.js

``` javascript
module.exports = {
  entry: './index.js',
  output: {
    filename: './bundle.js'
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