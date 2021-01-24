---
title: C#6.0 in a Nutshell
date: 2017-05-15
tag:
- csharp
---

## chapter 1.Introducing C# and the .NET Framework
### words
- *object orientation*: 面向对象；
- *encapsulation*: 封装；
- *inheritance*: 继承；
- *ploymorphism*: 多态；
- *explicitly*: 显式地；
- *perform*: 执行；
- *performance*: 性能；

### a

Encapsulation means creating a boundary around an *object*, to separate its external(public) behaviour from its internal(private) implementation detail.


### 面向对象 Object Orientation

c# 不同于其他面向对象语言的特点

1. 统一的类型系统 *Unified type system*
2. 实现了类和接口 *Classes and interfaces*
3. 拥有属性，方法，事件 *Properties, methods and event*
4. 函数可以进行值传递 *Function can be treated as values*
5. 支持纯净模式 *C# supports patterns for purity*

### 类型安全 Type Salfty

### 内存管理 Memory Management

c# 依靠运行时执行自动的内存管理。
c# 没有废弃指针,而仅使他们对大多数程序无效，对于性能要求更高的热点和交互操作，指针仍可以被使用。但在这些使用了指针的区域，会被显式地标记为不安全的（unsafe）

### 平台支持 Platform Support

Xamarin cross platform

### c# 与 CLR 的关系 C#'s Relationship with the CLR

CLR: Microsoft's Common Language Runtime
JIT: CLR's JIT(just in time) compiler

## chapter 2 C# Language Basic

### word

- *inferred*: 推断；
- *implicitly*: 隐式地；
- *precision*: 精度；


### 数字类型

|c# type|system type|suffix|size|Range|
|:--|:--|:--|:--|:--|
|integral-signed|
|sbyte|SByte||8bits|-2^7 - 2^7 -1 |
|short|Int16||16bits|-2^15 - 2^15 -1 |
|int|Int32||32bits|-2^31 - 2^31 -1 |
|long|Int64|L|64bits| -2^63 - 2^63 -1 |
|integral-unsigned|
|byte|Byte||8bits|0 - 2^8 - 1 |
|ushort|UInt16||16bits|0 - 2^16 - 1 |
|uint|UInt32|U|32bits|0 - 2^32 - 1 |
|ulong|UInt64|UL|64bits|0 - 2^64 - 1 |
|Real|
|float|Single|F|32bits| +-(~10^-45 - 10^38 ) |
|double|Double|D|64bits| +-(~10^-324 - 10^308 ) |
|decimal|Decimal|M|128bits| +-(~10^-28 - 10^28 )|

整数可以使用10进制和16进制，16进制以 `0x` 开头

``` csharp
int x = 127;
long y = 0x7F;
```

实数可以使用 `decimal` 或者指数表示。

``` csharp
double d = 1.5;
double million = 1E06;
```

### 数字后缀

|Category|C# type|Example|
|:--|:--|:--|
|F|float| float f = 1.0f;|
|D|double|double d = 1D;|
|M|decimal| decimal d = 1.0M;|
|U|uint| uint i = 1U;|
|L|long| long i = 1L;|
|UL|ulong| ulong i = 1UL;|

后缀 `U` 和 `L` 很少被使用，因为 uint, ulong, long通常会从 int 推断或隐式转换

``` csharp
long i = 5;
```

后缀 `D` 是技术冗余，所有带小数点的字面量都会隐式转换为 `double`。所以声明 `double` 可以省略后缀 `D`。

``` csharp
double x = 4.0;
```

`float` 和 `decimal` 类型的数字时必须要添加相应的后缀 （`F`、`M`）。否则则无法通过编译。

``` csharp
float f = 4.5f;
float d = -1.23M;
```

个人观点：

1.后缀不限制大小写
2.float 和 decimal 在声明为没有小数点的整数时，可以不用加后缀也能通过编译（？Momo）。类型是 `System.Single` 和 `System.Decimal` 没有转化为 `double` 类型

### 数字类型转换

如果目标类型可以表示源类型的所有可能值会发生隐式转换，否则需要显示（强制）转换

所有整型数字都可以隐式转化为浮点类型数字，反之则必须显示转换

比较大的整型隐式转化为浮点型时可能丢失精度。`System.Convert` 提供了提供了转化不同数字类型的方法。

### 特殊的整数运算 Specialized integral Operations
#### 整数除法 Integral Division

``` csharp
int a = 2 / 3;  // 0
int b = 0;
int c = 5 / b;  // throws DivideByZeroException
```

#### 整数溢出 Integral Overflow

``` csharp
int a = int.MinValue;
a--;
Console.WriteLine(a == int.MaxValue); // True
```

#### 8 和 16 位以下的整数计算 8- and 16-Bit Integral

`byte`、`sbyte`、`short` 和 `unshort` 这些8位与16位以下的数字类型没有自己的运算符号，C# 将他们隐式转化为能够运算的更大的类型。如果试图将以下结果赋值给原来的类型，编译时会抛出错误。

``` csharp
short x = 1, y = 1;
short z = x + y; // Compile-time error
```

此时 x, y 被隐式转化为 `int` 类型。为了通过编译可以修改成以下形式。

``` csharp
short z = (short)(x + y); // OK
```

### 特殊的浮点值与双精度浮点值 Special Float and Double Values

|Special Value|Double constant|Float constant|
|:--|:--|:--|
|NaN|double.NaN|float.NaN|
|+∞|double.PositiveInfinity|float.PositiveInfinity|
|-∞|double.NegativeInfinity|float.NegativeInfinity|
|-0|-0.0|-0.0f|

非零除以零得无穷

``` csharp
Console.WriteLine(1.0 / 0.0);  // Infinity
Console.WriteLine(-1.0 / 0.0); // -Infinity
```

零除以零，无穷相减得非数字

``` csharp
Console.WriteLine(0.0 / 0.0); // NaN
Console.WriteLine((1.0 / 0.0) - (-1.0 / 0.0)) // NaN
```

NaN 互不相等，以及判断 NaN 的两种方式

``` csharp
Console.WriteLine(0.0 / 0.0 == double.NaN); // False
Console.WriteLine(double.IsNaN(0.0 / 0.0)); // True
Console.WriteLine(object.Equals(0.0 / 0.0, double.NaN)); // True
```

#### double 类型与 decimal 类型

double 对科学计算更有帮助（例如计算空间坐标），而 decimal 更善于表示金融和“人造”的数字。

|Category|double|decimal|
|:--|:--|:--|
|内部表示|基于2进制|基于10进制|
|小数精度|15-16位有效数字|28-29位有效数字|
|范围|+-( ~10^-324 to ~10^308 )|+-( ~10^-28 to ~10^28 )|
|特殊值|+0, -0, +∞, -∞, NaN|无|
|速度|原生处理器|非原生处理器（速度为 double 的 1/10）|


..later
__