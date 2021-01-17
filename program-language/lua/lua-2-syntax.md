---
title: Lua 快速笔记(二) syntax
date:  2017-07-19
tag:
- lua
---


参考
[programing in lua](http://www.centoscn.com/uploads/file/20130903/13781389409335.pdf)

- [语法](#syntax)
- [函数](#function)
- [常用函数](#common_func)

<h2 id="syntax">语法</h2>


### 局部变量和代码块

``` lua
do

  local a = 1

end

print(a) -- nil
```

### 控制语句

1. Lua 认为 false 和 nil 为假

#### if 
```
if a == 0 then

  b = 1
elseif not b then
  
  b = 2
else
  
  b = 3
end
```

#### while

```lua
i = 0

while i < 10 do
  i = i + 1
end
```

### repeat-until

``` lua
i = 10
repeat 
  i = i + 1
until i > 20
```

先判断条件，不满足条件才执行 repeat, 不同于 do-while


### for

```lua
-- 1. 数值 for 循环

for i = 1, 10, 1 do
    print(i)        
end

print(i)            

-- number: 1 - 10
-- nil

-- 2. 范型 for 循环

array = ['Lua', 'CSharp']

for key, value in ipairs(array) do
  print(key .. ':' .. value)
end

-- string '1: Lua'
-- string '2: CSharp'

```

1. 语法中声明的变量为局部变量
2. 语法中的表达式只计算一次
3. 使用break跳出循环
4. 数值 for 循环中，表达式3(步长step)不传默认为1
5. 范型 for 循环中，`ipair` 为Lua 默认提供的迭代函数 ipairs


<h2 id="function">函数</h2>

### 声明

``` lua
function baz (a, b)
  -- function body
end

foo = {
  baz = baz
}

foo.baz = function (a, b) 
  -- 匿名函数
  -- function body
end

function foo.baz (a, b)
  -- function body
end

foo.baz = baz

```


### 调用

```lua
foo.baz(1)      -- a: 1, b: nil
baz(1, 2)       -- a: 1, b: 2
o:baz(1, 2)     -- o.baz(o, 1, 2) 对象方法的调用
```

1. 多余的参数会被忽略，缺少的参数值为 nil
1. ，当函数只有一个参数并且这个参数是字符串或者表构造的时
候，()是可选的

``` lua
print 'Hello World'  -- print("Hello World")
dofile 'a.lua'       -- dofile('a.lua')
print [[a multi-line 
 message]]           -- print([[a multi-line
                     -- message]])
f{x=10, y=20}        -- f({x=10, y=20})
type{}               -- type({}) 
```

### 返回多个值

```lua
s, e = string.find('hello Lua Language', 'lua')

print(s, e)            -- 7, 9

function baz ()
  return 1, 2
end

print(baz())           -- 1, 2

x = baz()              -- x: 1
x, y = baz()           -- x: 1, y: 2
x, y, z = 10, baz()    -- x: 10, y: 1, z: 2
a = { 'lua', baz() }   -- a: {'lua', 1, 2}        
```

### 可变参数

``` lua
function g (a, b, ...) end

--[[
CALL             PARAMETERS
g(3)             a=3, b=nil, arg={n=0}
g(3, 4)          a=3, b=4, arg={n=0}
g(3, 4, 5, 8)    a=3, b=4, arg={5, 8; n=2} 
]]--
```


### 尾调用

尾调用是一种类似在函数结尾的 goto 调用，当函数最后一个动作是调用另外一个函
数时，我们称这种调用尾调用。

``` lua
function f(x)
  return g(x)
end

-- g 的调用是尾调用。
 
```

一些编译器比如 Lua 解释器利用这种特性在处理尾调用时不使用额外的栈，我们称这种语
言支持正确的尾调用。
由于尾调用不需要使用栈空间，那么尾调用递归的层次可以无限制的。例如下面调
用不论 n 为何值不会导致栈溢出。

``` lua
function foo (n)
  if n > 0 then
    return foo(n - 1)
  end
end
```

<h2 id="common_func">常用函数</h2>

1. 排序 table

table.sort(table, sortFunc)

``` lua
table.sort(pet, function (a, b) 
  return a.name > b.name
end)
```

2. 处理异常 

```lua
if pcall(foo) then
  -- no errors while running `foo'
  -- ...
else
  -- `foo' raised an error: take appropriate actions
  -- ...
end

-- or 
local status, err = pcall(function () error({code=121}) end)
print(err.code) --> 121 
 
```