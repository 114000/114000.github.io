---
title: JavaScript 类型
date: 2020-11-19
---


数据类型 type

- 原始类型 primitive type
  - 数字
  - 布尔
  - 字符串
  - Symbol
- 对象类型 object type
  - 普通对象
    - Date
    - RegExp
    - Error
  - 数组
  - 函数
  - Map
  - Set
- 特殊类型
  - null 
  - undefind

## 数字 Number

### 直接量

- 整数: `[0(xXoObB)(a-fA-F0-9)*][digits]`
- 浮点数: `[digits][.digits][(E|e)[(+|-)]digits]`

```js
0
1
0xff      // 16进制 255
0xCAFE911 // 16进制
3.14      
2345.789
.33333
6.02e23   // 6.02 * 10 ^ 23
1.428E-32 // 1.428 * 10 ^ 32
0o363     // 8进制243
0O363     // 8进制243
0b1110011 // 2进制243
0B1110011 // 2进制243
```

``` js
// 特殊解释
0377      // 旧的8进制 严格模式禁用
// Uncaught SyntaxError: Octal literals are not allowed in strict mode.
-1        // 一元运算，非数字直接表示法
```

### 属性

无

### 方法

number.toExponential
number.toFixed     // 小数部分精度
number.toPrecision // 有效位数
number.toString // 继承自 Object
number.toLocaleString // 继承自 Object
number.valueOf // 继承自 Object

### 静态属性 

POSITIVE_INFINITY
MAX_VALUE
MAX_SAFE_INTEGER
1
EPSILON
MIN_VALUE
0
-1
MIN_SAFE_INTEGER
NEGATIVE_INFINITY
NaN Not a Number "执行数学运算没有成功，这是失败后返回的结果" 它和任何数字进行**逻辑比较始终false**
length (extends Function.length)
name (extends Function.name)

### 静态方法

isFinite false: NaN, Infinity -Infinity true: `others`
isInteger 是否为正数
isNaN 
isSafeInteger 是否为安全整数


### Math

### Tips

1. 浮点数判断相等

IEEE-754浮点数表示法适合表述二进制分数，不能精确表述十进制分数

``` js
function numbersCloseEnoughToEqual(n1,n2) {
    return Math.abs( n1 - n2 ) < Number.EPSILON;
}

var a = 0.1 + 0.2;
var b = 0.3;

numbersCloseEnoughToEqual( a, b );                  // true
numbersCloseEnoughToEqual( 0.0000001, 0.0000002 );  // false
```

2. 特殊值的表述

``` js
1/0 === Infinity === Number.POSITIVE_INFINITY
-1/0 === -Infinity === Number.NEGATIVE_INFINITY
Number.MAX_VALUE + 1 === Number.MAX_VALUE
Number.MAX_VALUE + Math.pow(2, 969) === Number.MAX_VALUE
Number.MAX_VALUE + Math.pow(2, 970) === Number.POSITIVE_INFINITY
Number.MIN_VALUE > 0
Number.MIN_VALUE / 2 === 0 // 下溢
1/Number.POSITIVE_INFINITY === 0
-1/Number.POSITIVE_INFINITY === -0
1/Number.MAX_VALUE > 0
Number.POSITIVE_INFINITY/Number.POSITIVE_INFINITY // NaN
```

3. 特殊值从大到小排序

```js
POSITIVE_INFINITY
MAX_VALUE // 最大浮点数 1.798e+308
MAX_SAFE_INTEGER // 最大安全正整数 2^53-1(9007199254740991)
1
EPSILON
MIN_VALUE // 最小的正数，无限趋近与0 5e-324 
0
-1
MIN_SAFE_INTEGER // 最小安全负整数 -2^53+1(-9007199254740991)
NEGATIVE_INFINITY
```

4. 虽然整数的最大范围能达到53位，但是位运算只适用于32位

5. 使用 `Number.isNaN`(es6) 代替 `window.isNaN`

6. 计算结果一旦溢出为无穷数（infinity）就无法再得到有穷数

7. `-0` 

``` js
(-0).toString() // '0'
JSON.stringify(-0) // '0'
+'-0' // -0
JSON.parse('-0') // -0
Number('-0') // -0
-0 === 0 // true

function isNegZero(n) {
    n = Number( n )
    return (n === 0) && (1 / n === -Infinity)
}

Object.is(0, -0) // false
Object.is(1/'foo', Number.NaN) // true
```

> 有些应用程序中的数据需要以级数形式来表示（比如动画帧的移动速度），数字的符号位（sign）用来代表其他信息（比如移动的方向）。此时如果一个值为 0 的变量失去了它的符号位，它的方向信息就会丢失。所以保留 0 值的符号位可以防止这类情况发生。

ES 新规范bigNumber

## 字符串 String

16位值组成的不可变有序序列

### 直接量 

``` js

```