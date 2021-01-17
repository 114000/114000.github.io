---
title: cpp
date: 2019-01-01
---

### install

<https://test482.github.io/How-use-VSCode-write-C/>

- download link

### normal

``` c++
#include <cmath>      // C math function
#include <iostream>
#include <climits>    // 关于整型的限制信息
```

### iostream

```cpp
cont << 'a word';        // print a string as a stream
cont << endl;            // new line. cont << '\n', endl 确保程序执行前可以输出，\n 则不能

cont << 'a word' << endl; // print a string and enter
cont << 'a word\n'

int count;

cont << 'please enter a number' << endl;
cin >> count;

cont << 'now count is' << count << endl;

```

### climits

```cpp
int n_int = INT_MAX;  // initialize n_int to max int value
short n_short = SHRT_MAX;
long n_long = LONG_MAX;
long long n_llong = LLONG_MAX;

cout << 'Minimum int value = ' << INT_MIN << endl;
cout << 'Bits per byte = ' << CHAR_BIT << endl;

cout << 'int is ' << sizeof (int) << 'bytes.' << endl;
cout << 'short is ' << sizeof n_short << 'bytes.' << endl;
cout << 'short is ' << sizeof (n_short) << 'bytes.' << endl;

```

|type|const|
|:---|:---|
|`char`|`CHAR_BIT`, `CHAR_MAX`, `CHAR_MIN`|
|`signed char`|`SCHAR_MAX`, `SCHAR_MIN`|
|`unsigned char`|`UCHAR_MAX`|
|`short`|`SHRT_MAX`, `SHRT_MIN`|
|...|...|

---
### comment

```cpp
// comment
/* a C-style comment */
```

### namespace

```cpp
#include <iostream>

/* way 1 */
using namespace std; // compile director `using`
cout << "a word";

/* way 2 */
std::cout << "a word";

/* way 3 */
using std::cout;
cout << "a word";

```

- note: `using` 函数内外均可使用


### definition

``` cpp
int count;
double side = sqrt(area);
int emus{7};       // 7
int rheas = {12};  // 12
int rocs = {}      // 0
int psychics{}     // 0

unsigned int rovert;
unsigned quarterback;
// unsigned == unsigned int 

unsigned short change;
unsigned long gone;
unsigned long long lang_lang; 

const int Months = 12;
```

note:
- 以两个下划线和一个下划线加大写字母开头的变量尽量保留给编译器及其资源使用
- 以一个下划线开头的变量尽量保留给全局标识符使用

### opeator

``` cpp
count = 12;

9 / 5 // 1
9.0/5 // 1.800000
```

### function

``` cpp
double sqrt (double); // function prototype
void simon (int); 
void random (void);
int add (int, int);

int add (int n, int m) {
  return n + m;  
}

```

note:
- 函数内不能声明函数

---

## 基本类型

### 整型

|key|width|intro|
|:---|---:|:---|
|`char`||常用来表示字符而不用来表示数字|
|`short`|>= 16||
|`int`|>= short||
|`long`|>= int||
|`long long`|>= long||

确保最小长度，而不是限定长度。以获得最大的兼容性

``` cpp
wchar_t bob = L'P';
wcout << L'tall' << endl;

char16_t ch1 = u'q'; // basic character in 16-bit form
char32_t ch2 = U'\U0000222B'; // universal character name in 32-bit form

```

### string

```cpp
"a word";
```

### number

``` cpp
float tub = 10.0 / 3.0;
double mint = 10.0 / 3.0;

1.2354f; // a float constant
2.45E20F; // a float constant
3.456789e28; // a double constant
2.2L; // a long double constant
```

### cpp reources


- [CodeCademy 的 C++ 在线课程。](https://www.codecademy.com/learn/learn-c-plus-plus)
- [C++ 网页编辑器](http://emun.ro/workspace)
- [Nana 一个跨平台的 C++ 图形界面组件库。](http://nanapro.org/en-us/)
- [计算机图形学教程 从数学基础开始教起的图形学教程，包含 C++ 源码。](http://www.scratchapixel.com/)
- [C/C++ 面向 wasm 编程---- Emscripten 工程实践](https://github.com/3dgen/cppwasm-book)
- [kbd-audio C++ 这个库可以根据击打键盘的声音，分析用户的输入内容。](https://github.com/ggerganov/kbd-audio)
- [Skia 图形库 - Skia 是一个由C++编写的开源图形库，能在低端设备如手机上呈现高品质的2D图形。截至2017年，它已被应用于 Mozilla Firefox、Google Chrome、Chrome OS、Sublime Text、Android、Flutter 框架，作为底层图形库](https://skia.org/) 
- [dust3d](https://github.com/huxingyi/dust3d)
- [BaiduPCS-Go 百度网盘的命令行客户端，使用 Go 语言开发](https://github.com/iikira/BaiduPCS-Go)
- [ferret - Go 语言写的 web scraping 工具，主要特点是操作过程是声明式的，非常易写。](https://github.com/MontFerret/ferret)
- [go-pry - Go 语言互动式的 REPL 环境，可以直接运行 Go 脚本。](https://github.com/d4l3k/go-pry)
- [Vugu - 一个使用 Go 语言写 HTML 前端页面的工具。完全不用 JavaScript，就能写出前端页面。未来的全栈将不再限于 JS，后端语言都可以写前端。](https://www.vugu.org/doc/start)
- [Java 线程与 Go 线程的根本差异 - 作者注意到一个现象，同一台机器，Java 线程最多只能建几千个，但是 Go 线程可以建数百万个。他研究后发现，这跟线程的内存占用有关，每个 Go 线程竟然只占用4KB。](https://rcoh.me/posts/why-you-can-have-a-million-go-routines-but-only-1000-java-threads/)
- [excelize 一个读写微软 Excel 文件的 Go 语言库。](https://github.com/360EntSecGroup-Skylar/excelize)
[Go 语言为什么快的5个原因](https://dave.cheney.net/2014/06/07/five-things-that-make-go-fast)
[Go by Example](https://gobyexample.com/)
[gameboy.live 一个开源软件，可以启动 Gameboy 服务，使用 Telnet 连线上去玩。](https://github.com/HFO4/gameboy.live)
