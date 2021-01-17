---
title: 《你不知道的JavaScript（上卷）》02 this 读书笔记
date: 2020-11-20
categories:
- [杂谈, 读书笔记]
- [编程语言, JavaScript]
tag: 
- JavaScript
- 读书笔记
cover: https://xinghe-blog-bucket.oss-cn-beijing.aliyuncs.com/img/you-dont-know-javascript.jpg
---


> 当一个函数被调用时，会创建一个活动记录（有时候也称为执行上下文）。这个记录会包含函数在哪里被调用（调用栈）、函数的调用方式、传入的参数等信息。this就是这个记录的一个属性，会在函数执行的过程中用到。

## 为什么要用this

随着你的使用模式越来越复杂，显式传递上下文对象会让代码变得越来越混乱，使用this则不会这样

::: info
个人觉得this的最佳实践是: 
1. 在显而易见地使用某种设计模式时
2. 在显而易见地使用面向对象技术的时
3. 在处理原生API带来的副作用时

其他情况则一律不用，这三点其实是一个意思，尽量在有共识的实现中使用。
:::

## this 全面解析

::: info
this 指向的是调用this所在的函数(作用域)的那个对象。所以只有在函数执行时才能确定this的指向。

更通俗的说，**谁**在使用这个作用域。this就指向**谁**

  ``` js
  function show () {
    console.log(this)
  }
  window.show() // this => window or undefined
  const a = { show: show }
  const b = { display: show }

  a.show() // this => a
  b.display() // this => b
  ```

:::


``` js
function baz() {
  bar()
}

function bar() {
  foo()
}

function foo() {
  console.log(this)
}

const o = { baz: baz, bar: bar, foo: foo }

baz()   // this => window or undefined
o.baz() // this => window or undefined
o.bar() // this => window or undefined
o.foo() // this => o
```

::: warning
- 如果没有显式的对象对函数进行调用，则指向window(严格模式下是 undefined)
- 严格模式下，即使通过window 调用也会指向 undefined。这里有一种特殊情况就是代码声明不在严格模式中，但调用在严格模式中，this的指向是 `window` 而不是`undefined`
:::


### 绑定规则


#### this 的绑定方式 

**1. 隐式绑定**

> 函数被当做引用属性添加到某个对象中

``` js
function foo() { 
    console.log( this.a );
}

var obj2 = { a: 42, foo: foo };

var obj1 = { a: 2, obj2: obj2 };

obj1.obj2.foo(); // 42

// 隐式丢失【学习术语】
var a = 3
var baz = obj1.obj2.foo
baz() // 3
setTimeout(obj1.obj2.foo, 100) // 3
```

解决**隐式丢失**的方法

1. 使用箭头函数
2. 使用硬绑定（特殊的显示绑定）

**2. 显式绑定**

> call, apply

```js
function foo() { 
  console.log( this.a )
}
var a = 4
var obj = { 
  a:2
}

foo.call(obj) // 2
```

**2.1 硬绑定**: 实际上是两层**显式绑定** 。这样调用时只能修改外层的绑定，不会影响到内层的绑定

``` js
function foo(something) { 
  console.log( this.a, something )
  return this.a + something
}

// 简单的辅助绑定函数
function bind(fn, obj) { 
  // 无论外部怎么使用此函数 apply都把 fn 绑定到了 obj上
  return function() {
    return fn.apply( obj, arguments )
  }
}

```

**3. new 绑定**

``` js
function foo(a) { 
  this.a = a
} 

var bar = new foo(2)

console.log( bar.a ) // 2
```

使用`new`来调用函数，或者说发生构造函数调用时，会自动执行下面的操作。

1. 创建（或者说构造）一个全新的对象。
2. 这个新对象会被执行`[[Prototype]]`连接。
3. 这个新对象会绑定到函数调用的this。
4. 如果函数没有返回其他对象，那么new表达式中的函数调用会自动返回这个新对象。

### 绑定的优先级

从高到低 `new 绑定` > `显式绑定` > `隐式绑定` > `默认绑定`

``` js
var bar = new foo()        // bar
var bar = foo.call(obj2)   // foo
var bar = obj1.foo()       // obj1
var bar = foo()            // global or undefined
```

### 软绑定

::: info
软绑定用来解决，函数**硬绑定**之后。无法再进行**隐式绑定**的问题。
:::

``` js
if (!Function.prototype.softBind) { 
  Function.prototype.softBind = function(obj) {
    var fn = this;
    // 捕获所有 curried 参数
    var curried = [].slice.call( arguments, 1 ); 
    var bound = function() {
      return fn.apply(
        (!this || this === (window || global)) ?
            obj : this,
        curried.concat.apply( curried, arguments )
      ); 
    };
    bound.prototype = Object.create( fn.prototype );
    return bound; 
  };
}
```

``` js
function foo() {
   console.log("name: " + this.name);
}

var obj = { name: "obj" }, 
    obj2 = { name: "obj2" }, 
    obj3 = { name: "obj3" };

var fooOBJ = foo.softBind( obj ); 

fooOBJ(); // name: obj

obj2.foo = foo.softBind(obj); 
obj2.foo(); // name: obj2 <---- 看！！！

fooOBJ.call( obj3 ); // name: obj3 <---- 看！ 

setTimeout( obj2.foo, 10 );
// name: obj   <---- 应用了软绑定
```

### 关于箭头函数

**箭头函数**没有绑定，也无法通过任意方式修改绑定。其内部的 `this` 其实是指向上一层的函数作用域。

::: warning
箭头函数与this是两种风格的代码风格，应该尽量避免使用一起使用
:::