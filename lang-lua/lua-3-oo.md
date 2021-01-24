---
title: Lua 快速笔记(三) OO
date:  2017-07-19
tag:
- lua
---

## class

``` lua
Animal = { name = "", age = 0 }

function Animal:new (o) 
  o = o or {}
  setmetatable(o, self)
  self.__index = self
  return o
end

function Animal:bark () 
  print(self.name .. ': waor')
end


misha = Animal:new({ name = 'Misha', age = 12 })

misha:bark()

-- string: 'Misha: waor'
```

ps: 如果要使用self 关键字。new方法必须使用 `:` 声明。并且调用的时候也要记得用 `:`

## extends

``` lua
Cat = Animal:new()

function Cat:bark ()
  print(self.name .. ': miao')
end

cat = Cat:new {name = 'as', age = 6 }

cat:bark()


```

## VS Code snippet

``` json
"new class": {
	"prefix": "newclass",
	"body": [
	  "$1 = { $2 }",
	  "",
	  "function $1:new (o)",
	  "  o = o or {}",
	  "  setmetatable(o, self)",
	  "  self.__index = self",
	  "  return o",
	  "end",
	  "",
	  "$3"
  ]
}
```


[lua 在线调试](https://tool.lu/coderunner/)
[sort](https://www.cnblogs.com/singledigit/p/6415902.html)