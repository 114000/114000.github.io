---
title: 基础 - 正则表达式
date: 2016-09-25
categories:
- [编程语言, JavaScript]

---

描述字符模式的对象

在线测试 [regexr](http://regexr.com/)
[正则常用参考](http://www.cnblogs.com/zxin/archive/2013/01/26/2877765.html)

## 修饰符

- `/foo/i` ignore case: 忽略匹配模式的字母大小写
- `/foo/g` global search: 全局匹配
- `/foo/m` multiline: 转换为多行，分别进行匹配

--- 

## 特殊符号

- `/./` 通配符: 匹配换行符以外的所有字符
- `/png|gif|jpg/` 选择符: 或者

**Note:** 
匹配 `.` 本身需要转义 `/\./`
`/a|ab/g` abc => a

---
## 锚

**不**匹配可见字符，只用来指定匹配发生的位置

```
TypeScript 
CoffeeScript 
Scripting 
ActionScriptEditor
```

- `/^Script/m` : 匹配以 `Script` 开头的字符。`Scripting`
- `/Script$/mg` : 匹配以 `Script` 结束的字符。`TypeScript`，`CoffeeScript`
- `/Script\b/mg` ：字边界。匹配以 `Script` 结尾的单词 `TypeScript`，`CoffeeScript`
- `/Script\B/mg`: 非字边界。匹配单词中含有 `Script` 的单词，但单词不能以 `Script` 结尾。`Scripting`，`ActionScriptEditor`

**Note:** 
以上4例中匹配的结果均为 `Script`，而非某个完整单词
`[\b]` 代表退格符

### 断言

- `(?=foo) ` 零宽正向先行断言：之后的字符要与其匹配，但不包含这些字符

  eg:
  `/\d+(?=px)/` 只匹配后面是px的数字，但匹配结果并不包含 px

  `3px 6em 12px` => `3 12`

- `(?!foo)` 零宽反向先行断言，之后的字符不与其匹配
  eg1:  `/\d+(?!px)(?!\d)/`只匹配不是以 px 结尾的数字
  `3px 6em 12px` => `6`
  eg2: `/\d+(?!px)/` 
  `3px 6em 12px` => `6 1`
  
 
---

## 字符集 `[]`

匹配字符集内的**某一个**字符

### 字符集中的特殊符号

- `/[^abc]/`: 否定，不包含字符集中的任何一个
- `/[a-c]/`: 表示范围。即 `/[abc]/`。

**Note:**
字符集中的 `-` 只要有一侧没有字符就不用转义。eg:`/[-2]/` 匹配 `-` 或 `2`
字符集中的 `.` 不用转义
字符集中的 `\b` 代表退格符

### 转义字符集

- `\d`: digital: 匹配数字。`[0-9]`
- `\D`: 匹配非数字。`[^0-9]`
- `\w`: word: 匹配字母、数字和下划线 `_`（ASCII单词）。`[a-zA-Z0-9_]`
- `\W`: 匹配除字母、数字和下划线以外的字符（非ASCII单词）。 `[^a-zA-Z0-9_]`
- `\s`: space: 空，制表符，以及其他 unicode 空白符` `，tab`\t`，换行符`\n` ，回车符 `\r`。 `[ \t\n\r]`
- `\S`: 非 Unicode 空白符

---

## 重复

`*`: 0个及以上
`+`: 1个及以上
`?`: 1个及以下
`{2}`: 2个
`{2,}`: 2个以上
`{2,4}` 2到4个

### 非贪婪重复

正则的重复规则默认匹配尽量多的字符，使用 ？来匹配尽可能少的字符

`/a+?/` aaa => 第一个 a
`/a+?/g` aaa => 全部3个 a
`/a+?b/` aaaab => aaaab 与贪婪模式一致，正则总是寻找字符串中第一个可匹配的字符进行匹配[1]

---
## 群组 `()`

方便使用重复符号 `/Java(Script)?/`: Java 或者 JavaScript

### 群组的引用

\\ 加上群组的序数

eg: `/<h(\d)>.*<\/h\1>/` 匹配一个闭合标签，`\1`代表前面的群组 `(\d)` 匹配到的数字。

``` diff
+ <h1>h1</h1>   ✅
+ <h2>h2</h2>   ✅
- <h3>xxxx</h4> ❎
```

$ 加上数字可以取得正则表达式匹配结构中的第几个群组，例如 `$1` 在 `/Java(Script)/` 中即为 `Script`，用法参照下方的 string.replace 方法

`$&` 可以获取匹配的整个项目，既上面的 `JavaScript`

`?:`不为群组添加引用 `(?:Script)` 不存储群组的匹配值，既使用 $1 不能得到 `Script`，只能得到字符串形式的 `'$1'`

---
## 字符串中与正则相关的实例方法

- `string.match(regExp) [array/null]` 
  * 返回一个由匹配结果组成的数组，没有匹配项则返回 `null`。
  * 如果有修饰符 g 则数组中包含所有匹配结果；如果没有修饰符 g，返回的数组第一项是匹配结果，而后数组的第n项是 $n。
  * 数组后添加的 index 属性是字符串中匹配的起始位置。
  * 数组后添加的 input 的属性是原始的字符串。

- `string.search(regExp) [number]` 
  * 返回匹配的起始位置，如果不存在匹配字符则返回 -1。
  * 不支持全局检索，即会忽略修饰符 g。
  * 如果传入的参数不是正则实例，则内部使用 RegExp 构造函数先将参数转化为正则实例。

- `string.replace(regExp|string, newString|function) [string]` [3]
  * 第一个参数是匹配的模式，如果是字符串则使用 RegExp 构造函数先将参数转化为正则实例。
  * 第二个参数是替换后的字符，如果参数是函数，那么函数的返回值则是替换的内容
  * 如果用于替换后的字符中包含了未使用的引用，则将其视为原始字符处理 eg4。

  ``` javascript
  'jaVAscriPt'.replace(/javascript/i, 'JavaScript')
  // => JavaScript

  'false can use?'.replace(false, true) 
  // =>'true can use?'
  
  'iOS, windows Phone, Android'.replace(/(ios)(.*)(android)/i, '$3$2$1')
  // => 'Android, windows Phone, iOS'
  
  'iOS, windows Phone, Android'.replace(/(ios)(.*)(android)/i, '$3$2$1$4')
  // => 'Android, windows Phone, iOS$4'

  'phone systems: iOS, windows Phone, Android'.replace(
    /(ios)(.*)(android)/i, 
    function (match, $1, $2, $3, index, input) {
      // match: 'iOS, windows Phone, Android'
      // $1: 'iOS'
      // $2: ', windows Phone, '
      // $3: 'Android'
      // index: 15
      // input: 'phone systems: iOS, windows Phone, Android'
      return 'phone systems: ' + $3 + $2 + $1
    }
  )
  // => 'phone systems: Android, windows Phone, iOS'
  ```

- `string.split(string|regexp) [array]`   [4]
  * 使用参数切分字符串，并将结果保存到数组中返回。
  * 如果字符串最末是切分的标志，则返回的数组最后一项则是空字符串。

``` javascript
'user=jack&id=233&city=beijing'.split('&')
// => ['user=jack', 'id=233', 'city=beijing']

'1w2Y3s4E5'.split(/[a-z]/i)
// => ['1', '2', '3', '4', '5']

'1w2Y3s4E5x'.split(/[a-z]/i)
// => ['1', '2', '3', '4', '5', '']
```
---
## JavaScript 中的正则 RegExp

``` javascript
const pattern = /foo$/
const pattern = new RegExp("foo$")
```

每次使用直接量都会创建新的对象（eg : `/foo/`）

### 实例属性

- `[string] regexp.source` 正则表达式文本，只读
  ``` javascript
  /[^foo]/.source // => "[^foo]" 
  ```
- `[boolean] regexp.ignoreCase` 是否带有 i 修饰符，只读
- `[boolean] regexp.multiline` 是否带有 m 修饰符，只读
- `[boolean] regexp.global` 是否含有 g 修饰符，只读
  ``` javascript
  /foo/i.global // => false
  /baz/g.global // => true
  ```

- `[number] regexp.lastIndex`同一个正则实例会存储上一次匹配正确的位置。为了保证匹配结果容易控制，可以每次使用新的实例来进行匹配，或者使用字符串的实例方法。


  ```javascript
  /** 全局匹配 **/
  const pattern = /\d/g

  pattern.lastIndex    // 0
  pattern.exec('1234') // ["1", index: 0, input: "1234"]
  
  pattern.lastIndex    // 1
  pattern.test('1234') // true
  
  pattern.lastIndex    // 2
  pattern.exec('1234') // ["3", index: 2, input: "1234"]
  
  /** 非全局匹配 **/
  const pattern = /\d/

  pattern.lastIndex    // 0
  pattern.exec('1234') // ["1", index: 0, input: "1234"]
  
  pattern.lastIndex    // 0
  pattern.test('1234') // true
  
  pattern.lastIndex    // 0
  pattern.exec('1234') // ["1", index: 0, input: "1234"]
  ```

### 实例方法

- `regexp.exec(string) [null/Array]` 
  * 匹配失败返回 `null`，匹配成功返回一个数组。但数组总只有一项，既总是只返回匹配到的第一个结果，修饰符 g 此处无效。
  * 数组后添加的 index 属性是字符串中匹配的起始位置。
  * 数组后添加的 input 的属性是原始的字符串。

  ``` javascript
  /\d/.exec('1234')
  // => ['1', index: 0, input: '1234']

  /\d/g.exec('a1234')
  // => ['1', index: 1, input: 'a1234']
  ```

- `regexp.test(string) [boolean]`  regexp.exec()的简单版，只返回一个布尔值。

---

**参考**：
1. 《 Javascript 权威指南（第六版）》第10章
- [宁浩网-正则表达式](http://ninghao.net/course/4020)
- [MDN JavaScript String.prototype.replace](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
- [MDN JavaScript String.prototype.split](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/split)