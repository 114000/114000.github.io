![](https://xinghe-blog-bucket.oss-cn-beijing.aliyuncs.com/img/you-dont-know-javascript.jpg)

2020-11-25

## 类型

JavaScript 的**变量**没有类型，**值**才有类型

JavaScript 内置类型

1. 空值 `null`
2. 未定义 `undefined`
3. 布尔值 `boolean`
4. 数字 `number`
5. 字符串 `string`
6. 符号 `symbol`
7. 对象 `object`

> 除了对象类型`object type` 其他都称为原始类型`primitive type`

**typeof**

``` js
typeof undefined === "undefined"; // true
typeof true === "boolean"; // true
typeof 42 === "number"; // true
typeof "42" === "string"; // true
typeof { life: 42 } === "object"; // true
typeof Symbol() === "symbol"; // true

// 历史遗留bug, 永远都不会修复
typeof null === "object"; // true

// 其他特殊情况
typeof function () {} === 'function'
```

:::info
- `null` 需要用复合语句判定 `!obj && typeof obj === 'object'`
- `null` 是唯一一个用 typeof 检测会返回"object"的**原始类型**值
- 除了函数以外，所有的对象的 `typeof` 取值都为 `object`。例如正则，数组，Map, Date
- 但函数确是对象，它的length代表参数长度
- 在对变量执行 `typeof` 操作时，得到的结果不是变量的类型，而是变量持有的值的类型
:::

`undefined` 和未声明的区别

``` js
var a

a // undefined
b // ReferenceError: b is not defined

typeof a === 'undefined'
typeof b === 'undefined' // typeof 的特殊安全防范机制
```

### 数组

创建稀疏数组 (sparse array) 时，稀疏位值为 undefined

``` js
var a = []
a[0] = 1
a[2] = 3
a[1] // undefined 已经被赋值了，值为 undefined
a[5] // undefined 是在对象内查找不到返回 undefined
a['0'] // 1       索引值可转化为非负10进制整数时等同于 a[0]
a.foo = 'bar'
a['foo'] // 'bar' 数组可以被当成对象进行属性的读取，
         // 但是这些属性不计入数组的长度（非最佳实践）
a.length // 3
```

**类数组**

`arguments`, `DOMList` 转化为真正的数组

- `Array.prototype.slice.call(arguments)`
- `Array.from(buttonDOMList)`

### 字符串

JavaScript 中字符串是不可变的，无法通过索引修改。只会创建一个新字符串返回

**读取字符的两种方法**

- `'foo'[1]`
- `'foo'.charAt(1)`

**借用数组方法处理字符串**

``` js
a.join;         // undefined
a.map;          // undefined

var c = Array.prototype.join.call( a, "-" );
var d = Array.prototype.map.call( a, function(v){
    return v.toUpperCase() + ".";
} ).join( "" );

c;              // "f-o-o"
d;              // "F.O.O."
```

::: warning
- 但像，`reverse`, `splice` 可修改成员变量的数组方法，不适用于字符串，需要二次转换
- 如果经常需要字符数组的话，建议直接使用字符数组存储
:::

### 数字

### 特殊值

- null: 指空值(empty value) ，曾经赋值过，但目前没有值
- undefined: 指没有值(missing value), 从未赋值

**`undefined`**

非严格模式 undefined 可以重新声明和赋值，但**不要这么做**

`void` 可以返回 `undefined`
`void` 后接任何东西都不影响其返回，这样我们可以利用其精简代码结构

``` js
const dothing = () => { doSomething() }
const dothing = () => void doSomething()
```


**`null`**

### 值和引用

简单值（即标量基本类型值，scalar primitive）总是通过**值复制**的方式来赋值 / 传递，包括 null、undefined、字符串、数字、symbol。

复合值（compound value）——对象和函数，则总是通过**引用复制**的方式来赋值 / 传递。

::: info
- 所有变量会指向值本身，并不会出现其他语言的指向**值的引用**这种情况
- 简单值是值传递，复合值是引用传递
:::

## 原生函数

常见的原生函数(native function) 也称内建函数(built-in function)

> `String()`,`Number()`,`Boolean()`,`Array()`,`Object()`,`Function()`,`RegExp()`,`Date()`,`Error()`,`Symbol()`

``` js
var a = new String('xyz') // String{'xyz'}
var b = String('xyz') // 'xyz'

typeof a // 'object'
typeof b // 'string'

Object.prototype.toString.call(a) // [object String]
Object.prototype.toString.call(b) // [object String]
```

::: info
对**基本类型**进行构造，被称为包装(boxing), 包装类为基本类型提供属性和方法. 引擎会自动优化包装行为不需要使用 `new String('abc').toUpperCase()`
:::

### 拆封

得到封装对象中的基本类型值，可以使用 valueOf() 函数

``` js
var a = new String( "abc" );
var b = new Number( 42 );
var c = new Boolean( true );

a.valueOf(); // "abc"
b.valueOf(); // 42
c.valueOf(); // true
```

**隐式拆封**

``` js
var a = new String( "abc" );
var b = a + ""; // b的值为"abc"

typeof a;       // "object"
typeof b;       // "string"
```

### 原生函数作为构造函数

尽量使用文字形式创建，避免使用构造函数

#### Array

``` js
var a = new Array(3) // [empty, empty, empty]
var b = [undefined, undefined, undefined]
var c = []
c.length = 3 // [empty, empty, empty]

delete b[1] // [undefined, empty, undefined]

a.map(x => console.log(x)) // 执行0次
b.map(x => console.log(x)) // 执行两次
c.map(x => console.log(x)) // 执行0次
```

::: warning
`map` 等迭代函数会自动跳过空单元 `empty slot`。永远不要创建和使用空单元数组
:::

比较好的创建稀疏数组的方法

``` js
var a = Array.apply( null, { length: 3 } )
var a = Array.from({ length: 3 })
```

### Object

`var a = new Object()`

一般不会使用，无法像文字形式那样一次设定多个属性，而必须逐一设定

### Function 

动态函数体是很危险的，不要把它当做 eval 的替代品

### RegExp

在动态定义正则表达式时十分有用

```js
var name = "Kyle";
var namePattern = new RegExp( "\\b(?:" + name + ")+\\b", "ig" );

var matches = someText.match( namePattern );
```

### Date

- `new Date()` 返回日期对象
- `Date()` 返回日期字符串，形式不固定（慎用）


### Error

``` js
function foo(x) {
    if (!x) {
        throw new Error( "x wasn't provided" );
    }
    // ..
}
```

### Symbol

- 不能使用 `new` 创建
- 符号可以用作属性名，但无论是在代码还是开发控制台中都无法查看和访问它的值，只会显示为诸如 Symbol(Symbol.create) 这样的值。
- 它却主要用于私有或特殊属性。很多开发人员喜欢用它来替代有下划线（_）前缀的属性，而下划线前缀通常用于命名私有或特殊属性

``` js
obj[Symbol.iterator] = function(){ /*..*/ };


var mysym = Symbol( "my own symbol" );
mysym;              // Symbol(my own symbol)
mysym.toString();   // "Symbol(my own symbol)"
typeof mysym;       // "symbol"

var a = { };
a[mysym] = "foobar";

Object.getOwnPropertySymbols( a );
// [ Symbol(my own symbol) ]
```

::: info
字面量声明是 JavaScript 的特色和优势。JavaScript引擎会对其做很多优化
:::

## 强制类型转换

- 隐式类型转换 `12 + ''`
- 显式类型转换 `String(12)`


::: info
从最佳实践来看
- 永远不要使用 `==`. 否则你就要记住很多东西
- JavaScript 引擎会针对变量类型进行优化，所以尽量不要修改变量类型
:::

``` js
"0" == null;           // false
"0" == undefined;      // false
"0" == false;          // true -- 晕！
"0" == NaN;            // false
"0" == 0;              // true
"0" == "";             // false

false == null;         // false
false == undefined;    // false
false == NaN;          // false
false == 0;            // true -- 晕！
false == "";           // true -- 晕！
false == [];           // true -- 晕！
false == {};           // false

"" == null;            // false
"" == undefined;       // false
"" == NaN;             // false
"" == 0;               // true -- 晕！
"" == [];              // true -- 晕！
"" == {};              // false
"" == [0];             // false
"" == [false];         // false
"" == [null]           // true -- 晕！
"" == [undefined]      // true -- 晕！
"" == [""]             // true -- 晕！

0 == null;             // false
0 == undefined;        // false
0 == NaN;              // false
0 == [];               // true -- 晕！
0 == {};               // false

// 数组在隐式转化的时候会字符串化，即[2].toString() === '2' 
// 所以实际进行的比较是 '' == '', 3 == '2', 2 == '2'
[] == ![];             // true -- 晕！
3 == [2];              // false
2 == [2];              // true -- 晕！

```


## 表达式

### 表达式的副作用

**=**

``` js
if (str && (matches = str.match( /[aeiou]/g ))) {
    return matches;
}
```

**++**

``` js
var a = 3
var b = a++
var c = (a++, a)
a // 5
b // 3
c // 5
```

**delete**

``` js
function deleteProperty (obj, propertyName) {
    // true or false
    return delete obj[propertyName]
}
```

特殊情况 

``` js
[] + {} // "[object Object]" 可以理解为 '' + {} {} 被理解成空对象是一个值
{} + [] // 0 可以理解为 {} 是一个空代码块不执行任何操作，而+[] 是对[]的强制类型转换
```

else if 不是 JavaScript 内置语法，只是我们利用了简便写法

``` js
if (true) { console.log('x')}
if (true) console.log()

if (a) {
    doSomething(a)
} else {
    if (b) {
        doSomething(b)
    }
    else {
        doNothing()
    }
}

if (a) doSomething(a)
else if (b) doSomething(b)
     else doNothing()
```

try finally 

``` js
function foo() {
  try {
    return 42;
  }
  finally {
    console.log( "Hello" );
  }

  console.log( "never runs" );
}

console.log( foo() );
// Hello
// 42
```

::: info
- finally 的代码会始终执行，
- 如果 finally 中抛出异常 try 的返回值会被抛弃
- finally 中的返回值会覆盖 try 中的返回值
:::