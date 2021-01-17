---
title: 基础 - 语法
date: 2018-02-02
categories:
- [编程语言, JavaScript]

---

执行环境
1. 浏览器: `ctrl` + `shift` + `i` / `cmd` + `alt` + `i`, 
2. native: ReactNative, Weex, Electron（chromium）
3. Server: Nodejs
4. cocos2d-js, weChatGame

### 函数是一等公民

``` javascript
function foo () {}
const foo = function () {} // 匿名函数

const baz = {
  foo: function () {}
}

baz.foo()

function bar () {
  const foo = () => {}
  const foo = a => a + 1
}
```

additional
1. 自执行匿名函数：`(function (global) {})(window)` 变量注入
2. 声明变量：默认用 `const`，需要的时候才用 `let`, 尽量别用 `var` 词法作用域的问题

### this 在使用时才知道它的指向

``` javascript
const baz = {
   foo: function () { console.log(this) },
   a: 12
}
baz.foo()
// this => baz
const foo = baz.foo
foo()
window.foo()
// this => window
```

additional
全局变量: browser: windows, nodejs: global

### 异步执行，事件驱动

``` javascript
// browser
document.addEventListener('click', function (e) { alert(1) }, false)
fetch(url).then(() => {})
.catch(e => {})
.then(() => {}) // ....

// server
var server = http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.end('<h1>Hello world!</h1>');
})
// cocos2d-js
this.node.on(cc.Node.EventType.TOUCH_END, function (e) { 
  // handle event 
})

```

additional
1. 声明字符串: js 中尽量用单引号声明，因为有的时候会调用 html 中的双引号


### 变量

``` javascript
  true, 1, { a: 1 }, [1], '1'
  false, 0, null, undefined, ''
  NaN != NaN
```

additional

[== 与 === 的区别](https://www.cnblogs.com/lindasu/p/7471519.html)，建议平时两个值比较时使用 === 来判断，单值判断可以直接用 `if (null)`, `undefined ? 1 : 2`

### 类型

``` javascript
typeof 1 => 'number'
typeof NaN => 'number'
typeof '1' => 'string'
typeof true => 'boolean'
typeof undefined => 'undefined'
typeof [] => 'object'
typeof {} => 'object'
typeof null => 'object'

Array.isArray([]) => true
isNaN(NaN) => true
```

###  原型链 Prototype `__proto__`

每一个实例对象都包含一个 prototype 对象，指向它的原型，并最终指向 Object
``` 
  Object -----  Array ----- extandArray
  _proto_ --- _proto_ ----- _proto_
                               |---------------- .myExtandMethod
                 |----------<--x---------------- .map
    |---------<--x----------<--x---------------- .hasOwnPorperty
```

### 条件

```
if (SYNAX) {}
else if (SYNAX) {}
else {}

switch (age) {
  case 20: alert('青春')
    break
  case 40: alert('成熟')
    break
  default: 
    break
}
```

### 表达式

```
const a = 12
a === 6 ? '是6' : '不是6'
timer && clearTimeout(timer) // if (timer) clearTimeout(timer)
return resultArray || [] // return resultArray ? resultArray : []
```



### 值

```js
null == undefined                     true   
null == false                         false
null == 0                             false
null == ''                            false 

undefined == false                    false
undefined == 0                        false
undefined == ''                       false


!null                                 true
!undefined                            true
!0                                    true
!''                                   true
 
0 == true                             false
'' == true                            false
1 == true                             true
'1' == true                           true


NaN == NaN                            false           
isNaN(NaN)                            true
Infinity === Infinity                 true      
Math.abs(-Infinity) === Infinity      true
!NaN                                  true           
!Infinity                             false             

(function () {}) == (function () {})  false
[] == []                              false
({}) == {}                            false
![], !{}, !(function () {})           false
```

### example 