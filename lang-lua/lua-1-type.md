---
title: Lua 快速笔记(一) type
date:  2017-07-19
tag:
- lua
---

参考
[programing in lua](http://www.centoscn.com/uploads/file/20130903/13781389409335.pdf)

- [注释](#comment)
- [值和类型](value_type)
- [运算符](#operator)
- [表](#table)
- [赋值](#assignment)

## 注释

```lua
-- 单行注释

--[[
    多行注释
--]]
```

## 值和类型

### nil

1. 未初始化的变量值为 nil
2. nil 只与自己相等

### boolean

> true / false

### number

1. 不区分整型和浮点型
2. 0 被判定为真
3. `tostring(number)` 方法用于将数字转化为字符串

### string

1. 单双引号都可以用于声明字符串 `'hello'` `"haloo"`
2. 两对中括号可以用于声明多行字符串 ``[[多行字符串]]``
3. `..` 是字符串链接符，不同与其他语言 `+` 作为单纯的算数运算符。
4. 转义字符串**未完成**


```lua

local mutiString = [[
    111
    223123
]]

print('10' + 1) -- number: 11
print(10 .. 22) -- string: '1022'
```

### function

lua中函数是第一类值，可以存储到变量中，也何以作为函数的返回值

### UserData

**later**

### Thread

**later**


## 运算符

### 算数运算符

1. 二元运算符: `+`,`-`,`*`,`/`,`^`,`%` 加，减，乘，除，幂，模
2. 一元运算符: `-` 负

### 关系运算符

`<` `>` `<=` `>=` `==` `~=` 

1. 关系运算符返回 boolean 类型（true/false）
2. == 比较地址， ~= 比较值

### 逻辑运算符

`and`, `or`, `not`

用法对应其他语言的 `&&`, `||`, `!`，and 优先级高于 or

``` lua
-- 1. 三元运算
a and b or c

b 为 nil 时会返回 c, 正确三目为 (a and {b} or {c})[1]

-- 2. 判断真

func1 and func1() -- func1 不为假执行

x = x or y
-- 等于
if not x then
    x = y 
end

```

### 运算符优先级

level|-
:---:|:---
1|`^`
2|`not` `-` (unary 一元)
3|`*` `/`
4|`+` `-`
5|`..`
6|`<` `>` `<=` `>=` `~=` `==`
7|`and`
8|`or`

除了`^`和`..`外所有的二元运算符都是左连接的。



## 表 table

### 1. 创建

``` lua
-- 类数组
days = { 
  "Sunday", "Monday", "Tuesday", "Wednesday",
  "Thursday", "Friday", "Saturday"
}

-- 类对象
pet = { name = "Misha", age = 12 }

-- 混合

foo = {
  date = "2017-07-19",
  worklist = { "lua", "csharp" },
  pet = pet
}

```

ps:

1. 数组风格是对象风格的特例

  ``` lua
  {"red", "green", "blue"}
  -- 相当于
  {[1] = "red", [2] = "green", [3] = "blue"} 

  ```

2. 数组风格下标从1开始，可以规定从0开始，但很多标准库不能使用

  ``` lua
  {[0] = "red", "green", "blue"}
  ```
3. 在构造函数的最后的"`,`"是可选的，可以方便以后的扩展。
  
  ```lua
    {"red", "green", "blue",}
  ```
  
4. 在构造函数中域分隔符逗号（","）也可以用分号（";"）替代。

### 2. 读取

``` lua
foo.data        -- string: '2017-07-19'
foo.worklist[1] -- string: 'lua' 注意：下标从1开始
foo.pet.age     -- number: 12
```

### 3. 修改

``` lua
foo.data        -- string: '2017-07-19'
foo.data = 20170719
foo.data        -- number: 20170719
```

### 4. 删除

赋值为 nil


<h2 id="assignment">赋值</h2>

1. 多变量赋值
  
  ```lua
  a, b = 10, 2 * x
  -- a: 10, b: 2 * x
  
  a, b, c = 0
  -- a: 0, b: nil, c: nil
  
  a, b, c = 3, 4, 5, 6
  -- a: 3, b: 4, c: 5;    6被忽略
  
  function f () 
    return 10, 20
  end
  
  a, b = f()
  ```

2. 交换赋值 
  
  ```lua
  x, y = y, x
  a[i], a[j] = a[j], a[i]
  ```

3. 值的个数与变量个数不一致遵循：
  - 变量个数 > 值的个数：按变量个数补足 nil 
  - 变量个数 < 值的个数： 多余的值会被忽略

### require

模块中声明为 local，并 `return` 的变量。在其他模块中引用时使用 `local foo = require 'foo'`

模块中声明的全局变量，只要被其他任意一个模块引用时，即载入到 _G中，别的模块即可任意调用
