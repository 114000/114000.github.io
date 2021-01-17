---
title: 【归档】Dart
date: 2018-08-05
categories:
- [编程语言, Dart]
tags:
- 归档
---

::: danger

2020-11-17 

感觉是注定会消逝的语言，Flutter 的败笔选择。等有机会再捞这语言吧。先归档了
:::


## 注释

```dart
// 单行注释

/*
 * 多行注释
 */
```

## 变量

未赋值的变量默认值为 `null` 即便声明的类型为 int double

``` dart
// 可以用类型声明变量
int age = 12;
String color = 'red';

// name 被推断为 String 类型
var name = 'Misha';

// 用 dynamic 声明的变量可以改变类型 
dynamic x = '8';
x = 8;

// 用 final 声明恒量
final area = 'Asia';
final String country = 'China';
final val = returnAValue();

// 用 const 声明编译时恒量, 编译时就能确定的值，不能是函数返回值
static const a = 12 * anotherConstInt; // 类变量需要指定 static

// const 还可以指定对象不可变
// 这种方式是将变量引用和实例区分开的
// a 可以更换引用地址，但不能更换类型
var a = const [1, 2];
a[1] = 3;       // Error


a = [2, 3]      // [2, 3]
a = ['a', 'b']; // Error

```

## 类型

### 数字

``` dart

int x = 1;
int hex = 0xEADBEF;

1.toString() // '1'

double y = 1.1;
double exponents = 1.42e5;

3.14159.toStringAsFixed(2) // 3.14
```


### 字符串

``` dart
String s1 = '单引号可以声明字符串';
String s2 = "双引号也可以声明字符串";
String s3 = 'It\'s 转义 """""" ';
String s4 = "he say: \"hola\" 转义 '''''";

// 模板字符串
// 单变量可省略花括号
String s = 'what';

String one = '你说$s'; // '你说what'
String another = '大写${s.toUpperCase()}'; // '大写WHAT'


// 字符串连接
String all = one + another // '你说what大写WHAT'

// 像JS中那样, 字符串可以作为 key 在 map 中添加和读取字符串
Map<String, String> upperLetter = {'a': 'A' };
upperLetter['b'] = 'B';
upperLetter.length; // 2
upperLetter['c'];  // null 

// 字符串转数字
int.parse('1'); // 1
double.parse('1.1'); // 1.1

// == 可判断两个字符串相等
'1' + '1' == '11';

// 多行字符串
'''
多
行
''';

"""
多
行
""";

// raw string
r'path\new';
'path\new';

var emmm = 'a'
  ' very'
  ' long'
  ' string'; // 'a very long string'
```

### 布尔 

true or false, dart 是类型安全的语言，所以不能用非布尔进行 if assert 等条件判断

``` dart
aString.isEmpty
aInt < 0
aNumber.isNaN

```


### 列表（数组）

``` dart
var list = [1, 2];
var list = <int>[1, 2];
List<int> list = [1, 2];
var list = new List<int>(2); // [null, null]



// 读取 索引从 0 开始
list[0];     // 1
list[2];     // Index out of rang
list.length; // 2

// 设置
list[1] = 1; // [1, 1]
list[2] = 5; // Index out of rang

// ??? 莫非是动态类型列表 ???
var list = [];
var list = List();
list.addAll([1, 2]); // [1, 2]
list[0] = 'a';       // ['a', 2]
list[0] = 1.2;       // [1.2, 2]
```

### 图

``` dart
var map = { 'a': 'A' };
var map = <String, String>{ 'a' : 'A' };
Map<String, String> map = { 'a', 'A' };
var map = new Map<String, String>(); // {}

// 读取
map['a'] // 'A'
map['x'] // null
map.length // 1
// 设置
map['b'] = 'B'; // {'a': 'A', 'b': 'B'}

// 
var map = Map();
map[1] = 'A';
map['b'] = 2;
// {1: 'A', 'b': 2}
```

### Rune


### Symbol


### 运算符

|||
|---|---|
|一元后缀|`expr++` `expr--` `()` `[]` `.`  `?.`|
|一元前缀|`-expr` `!expr` `~expr` `++expr` `--expr`|
|乘性|`*` `/` `%` `~/`|
|加性|`+` `-`|
|位移|`<<` `>>`|
|位与|`&`|
|位或|`|`|
|位异或|`^`|
|关系与类型测试|`>=` `>` `<` `<=` `as` `is` |
|相等性|`==` `!=`|
|与|`&&`|
|或|`||`|
|判断 null| `??` |
|流式调用|`..`|
|三目|`expr1 ? expr2 : expr3`|
|赋值|`=` `*=` `/=` `~/=` `%=` `+=` `-=` `<<=` `>>=` `&=` `^=` `|=` `??=`|



``` dart
!null  // true
3 ~/ 4 // 0
4 ~/ 3  // 1

~1 // 4294967294 一元求逆 

int a;
int b = a ?? 1; // a: null b: 1;
a ??= 1;  // a: 1

3 << 1 // 0011 0110   6
3 >> 1 // 0011 0001   1
3 | 1  // 0011 | 0100 7
```

## 控制流

### 条件

``` dart
if (aBoolCondition) {

}
else if (anotherBoolCondition) {

}
else {
  
}
```


## 函数

方法参数 getField

## import

``` dart
// 引用包 
// 包需要在 pubspec.yaml 中配置并安装才能使用
import 'package:flutter/material.dart';

// 引用其他类
import 'App.dart';
```

### 单例

``` dart
class Singleton {
  static Singleton _s;

  static get instance => _s ?? (_s = new Singleton._internal());

  Singleton._internal () { /* code */ };
}

// get 
Singleton.instance;

// or factory
class Singleton {
  static Singleton _s;

  factory Singleton () => _s ?? (_s = new Singleton._internal());

  Singleton.internal ();
}

// get
new Singleton();
```


## VSCode Snippets



### Flutter Statefull Widget

``` json
{
  "Flutter Statefull Widget": {
    "prefix": "fltStatefullWidget",
    "body": [
      "class $1 extends StatefulWidget {",
      "  @override",
      "  createState () => new _$1State();",
      "}",
      "",
      "class _$1State extends State<$1> {",
      "",
      "  @override",
      "  build (BuildContext content) {",
      "    $3",
      "    return $4;",
      "  }",
      "}"
    ]
  }
}
```

### exec end

``` json
{
  "exec end": {
    "prefix": "()",
    "body": [
      "($1);",
      "$2"
    ]
  }
}
```