# 《你不知道的JavaScript（上卷）》- 01作用域与闭包

2020-11-19

![](https://xinghe-blog-bucket.oss-cn-beijing.aliyuncs.com/img/you-dont-know-javascript.jpg)

## 作用域是什么

> 作用域是一套规则，用于引擎确定在何处以及如何查找变量（标识符）

## 作用域工作模型
- **词法作用域**：最为普遍的，被大多数编程语言所采用
  - **函数作用域**: `function () {}`
  - **块作用域**: `{}`
  - **被劫持的块作用域**: , `if{}`, `for() {}`
- **动态作用域**：运行时确定的作用域，出现在某些编程语言中


### 传统编译语言的编译流程

- **分词/词法分析(Tokenizing/Lexing)**
  - 分词: 程序字符串(string) - 词法单元(token)
  - 词法分析: 判断词法单元是独立的还是有上下文状态的**过程**，赋予语义
- **解析/语法分析(Parsing)**
  - 词法单元流(数组)转换为抽象语法树(AST: Abstract Syntax Tree)
  - 抽象语法树: 一个由元素逐级嵌套所组成的代表了程序语法结构的树
- **代码生成**
  - 代码生成: AST 转换为可执行的代码

> JavaScript 执行前编译

### 作用域

职员表
- 引擎: 从头到尾负责整个JavaScript程序的编译及执行过程。
- 编译器：负责语法分析及代码生成等脏活累活
- 作用域: 负责收集并维护由所有声明的标识符（变量）组成的一系列查询，并实施一套非常严格的规则，确定当前执行的代码对这些标识符的访问权限。


JavaScript `const a = 2` 执行过程

``` bash
- 编译器:Tokenizing
  - 'var a = 2' => ['var', 'a', '=', '2']
- 编译器:Lexing
  - 询问作用域是否有同名a变量
    - 有: 忽略声明（如果是const会抛出异常）
    - 无: 要求作用域在当前作用域的集合中声明一个新的变量，并命名为a
- 编译器:Parsing
  - ['var', 'a', '=', '2'] => AST
  - 生成代码
- 引擎:execute
  - 询问作用域是否存在a(这是一个LHS查询)
    - 有: 使用变量
    - 无: 继续查找
    - 没找到: 抛出异常
    - 找到了: 使用a
      - 赋值: a = 2
```

- **LHS**: Left Hand Side(函数声明不适合被认定为LHS, 原因在Note中)
  - `a = 2`
- **RHS**: Right Hand Side 可以理解为retrieve his source value（取到它的源值）
  - `consle.log(a)`
  - `foo()`


::: info
你可能会倾向于将函数声明function foo(a) {...概念化为普通的变量声明和赋值，比如var foo、foo ＝ function(a) {...。如果这样理解的话，这个函数声明将需要进行LHS查询。然而编译器可以在代码生成的同时处理声明和值的定义，比如在引擎执行代码时，并不会有线程专门用来将一个函数值“分配给”foo。因此，将函数声明理解成前面讨论的LHS查询和赋值的形式并不合适。

:::

``` js
function foo (a) { // 函数声名不适合理解为LHS
  console.log(a)
}

foo(2)

// RHS: foo, (line:5)
// LHS: a, (line:1)
// RHS: console,(line:2)
// RHS: a, (line:2)
```

### 作用域链

遍历嵌套作用域链的规则很简单：引擎从当前的执行作用域开始查找变量，如果找不到，就向上一级继续查找。当抵达最外层的全局作用域时，无论找到还是没找到，查找过程都会停止。

### 异常

**LHS**, **RHS** 的作用

- 查询到变量
  - 合理操作，正产运行
  - 不合理操作，抛出 `TypeError`。比如`null.log()`
- 查询不到变量
  - 非严格模式
    - LHS不会抛出异常，会声名一个全局变量
    - RHS 会报 `ReferenceError`
  - 严格模式 
    - LHS 与 RHS 都会报`ReferenceError`

## 词法作用域


> **词法作用域**: 如其名，在编写代码时，根据**代码结构**确定的作用域。


::: info
- `{}` 可以创建作用域。即函数，if,else,for,等语法以及空写 `{}`都可以创建子作用域。
- 一种是函数作用域，一种是块作用域，if,else,for,等则是被内部变量劫持的块作用域
::: 

::: warning
- 无论函数在**哪里**被调用，也无论它**如何**被调用，它的词法作用域都**只由**函数被声明时所处的位置决定。
- 词法作用域查找只会查找一级标识符: foo.bar.baz 只会查找foo
:::

### 遮蔽效应

> **遮蔽效应**：作用域查找会在找到第一个匹配的标识符时停止(由内而外)。

::: warning
被遮蔽的全局变量可以通过 `window.a` 来访问，非全局变量被遮蔽无法访问。
:::


### eval 与 with

`eval` 的注入会遮蔽父级作用域的变量，但在严格模式中 `eval` 有其自己的作用域并不会产生遮蔽效应。

``` js
function foo(str) {
  "use strict"
  eval( str )
  console.log( a ) // ReferenceError: a is not defined
}

foo("var a = 2")
```

`with` 在没有查找到变量时，会将赋值当做声明，泄露到 `with` 的作用域上 



``` js
function foo(obj) {
  with (obj) {
    a = 2
  }
}

var o1 = { a: 3 }

var o2 = { b: 3 }

foo( o1 )
console.log( o1.a ) // 2

foo( o2 )
console.log( o2.a ) // undefined
console.log( a ) // 2——不好，a被泄漏到全局作用域上了！
```

::: danger
  实践中 eval 与 with 都被视为此语言的糟粕部分被抛弃了。这里只是为了理解作用域，被拉出来展示一下
:::


### 词法作用域被破坏带来的问题

- 安全性，注入攻击
- 性能，JavaScript引擎会在编译阶段对词法进行静态分析，并预先确定所有变量和函数的定义位置，才能在执行过程中快速找到标识符。eval与with会破坏词法，导致标识符位置被修改。优化会失去意义



## 动态作用域

**JS没有动态作用域**

|-|词法作用域|动态作用域|
|:---|:---|:---|
|何时确定|定义时(编写代码时)|运行时|
|关注点|函数在何处声明|函数从何处调用|

最后，**this**关注函数如何调用，这就表明了this机制和动态作用域之间的关系多么紧密。如果想了解更多关于this的详细内容，参见本书第二部分“this和对象原型”。

## 函数作用域和块作用域

### 函数作用域

> **函数作用域**的含义是指，属于这个函数的全部变量都可以在整个函数的范围内使用及复用（事实上嵌套在其内部的作用域中也可以使用）

函数“隐藏”变量的技术
  - 是最小特权原则的延伸，内容私有化
  - 规避冲突

``` js
// good
const doSomething = (a) => {
  var b
  const doSomethingElse (a) => a - 1
  b = a + doSomethingElse(a * 2)
}
doSomething(2)

// bad
var b
const doSomethingElse = (a) => a - 1
const doSomething = (a) => {
  b = a + doSomethingElse(a * 2)
}
doSomething(2)
```

#### 函数表达式

**函数表达式**可以解决具名函数会污染所在作用域的变量名。

**函数声明**和**函数表达式**之间最重要的区别是它们的**名称标识符**将会绑定在何处。

``` js
// 函数表达式的名称标识符绑定在函数中
// 立即执行函数表达式 IIFE immediately invoked function expression
(function foo () {
  const b = 1
  console.log(b)
})()

// 函数的名称标识符绑定在父级作用域中
function foo () {
  const b = 2
  console.log(b)
}

foo()
```

**匿名函数表达式**的问题

- 匿名函数在栈追踪中不会显示出有意义的函数名，使得调试很困难
- 无法引用自身，事件无法解绑时
- 失去的可读性

::: info
- 始终给函数表达式命名是一项最佳实践

我也经常为贪时间不写函数名，但最后发现要么就是释放的时候要用，要么就是不知道这函数具体有什么用，还得仔细看代码才行
:::


IIFE 的另一个用途是倒置代码的运行顺序，常应用于UMD(Universal Module Definition)项目中

``` js
var a = 2

(function IIFE( def ) {
    def( window );
})(function def( global ) {
    var a = 3
    console.log( a ) // 3
    console.log( global.a ) // 2
})
```

### 块作用域

> 块作用域是一个用来对之前的最小授权原则进行扩展的工具，将代码从在函数中隐藏信息扩展为在块中隐藏信息。

**块级作用域的作用**

- 垃圾回收：可以利用块级作用域提前释放内存，不必等待函数完全执行之后再释放
- 迭代时重新绑定: `for (let i = 0; i < 10; i++) console.log(i)`

**声明变量关键字**

- `var` 无视块级作用域，提升变量到函数作用域。
- `let` 可以将变量绑定到所在的任意作用域中
- `const` 与 `let` 表现一致，但不能修改

::: info
声明变量的最佳实践是，所有变量都用const 声明，只在需要的时候用 let。永远不使用var
:::



## 提升

```js
console.log(a) // => undefined

var a = 2

console.log(b) // => ReferenceError: Cannot access 'b' before initialization

let b = 2

console.log(c) // => ReferenceError: c is not defined

function foo () {
  var c = 2
}

```

::: warning

无论是var提升还是函数提升在今后的编程实践中都是被禁止了。与其他语言不同的是，JS是需要兼容之前版本的。所以这些语言特性都会留在DNA里，不会随着语言版本的迭代而消失。但如果还有公司(除了做JS内核的)面试题包含这些。应聘者应该首先就排除这些了。

就这类的吧，都是写特例不想总结了。浪费生命
:::


## 作用域闭包

> 当函数可以记住并访问所在的词法作用域时，就产生了闭包，即使函数是在当前词法作用域之外执行。

闭包是基于词法作用域书写代码时所产生的自然结果。闭包的创建和使用在你的代码中随处可见

``` js
function add (a) {
  // 返回函数或对象并不是界定闭包的关键，只是我们经常这么用而已
  return function addA (b) {
    return a + b
  }
}

const add7 = add(7)

add7(5) // 12
add(2)(4) // 6
```

::: info

- 用来持久化一些运行时需要重用的变量
- 在同一个词法作用域声明并执行的函数，不能称为闭包
:::

### 模块模式

**模块模式**的两个**必要条件**
1. 必须有外部的封闭函数，该函数必须至少被调用一次`CoolModule`（每次调用都会创建一个新的模块实例）
2. 封闭函数必须返回至少一个内部函数(`doSomething`/`doAnother`)，这样内部函数才能在私有作用域中形成闭包，并且可以访问或者修改私有的状态。

``` js
var foo = (function CoolModule() { 
    var something = "cool"
    var another = [1, 2, 3]

    function doSomething() { 
        console.log(something)
    }

    function doAnother() {
        console.log(another.join( " ! " ))
    }

    return {
        doSomething: doSomething, 
        doAnother: doAnother
    }
})()

foo.doSomething() // cool 
foo.doAnother() // 1 ! 2 ! 3
```
