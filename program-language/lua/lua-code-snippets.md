---
title: Lua VSCode 代码片段
date:  2018-08-12
tag:
- lua
---

### 结尾 

``` json
{
  "end": {
    "prefix": "ee",
    "body": [
      "",
      "  $1",
      "end"
    ]
  },
}
```

### 函数

``` json
{
  "function end": {
  "prefix": "fe",
  "body": [
      "function $1 ($2)",
      "  $3",
      "end"
    ]
  },
}
```

### 创建类 

``` json
{
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
}
```