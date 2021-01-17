---
title: JSON Schema
---

- [官方文档](https://json-schema.org/)


### 在 VSCode 中配置 json schema

1. 在JSON 文件中直接指定

``` json
{
  "$schema": "http://json.schemastore.org/babelrc"
}
```

2. 在个人设置, 工作区设置中

```js
// settings.json or /.vscode/setting.json

// 通过网络资源配置 JSON Schema 
{
  "json.schemas": [ 
    { 
      "fileMatch": ["/.babelrc"], 
      "url": "http://json.schemastore.org/babelrc" 
    }
  ]
}

// 本地配置JSON Schema 
{
  "json.schemas": [ 
    { 
      "fileMatch": ["/.myconfig"], 
      "schema": {
        "type": "object", 
        "properties": { 
          "name" : { 
            "type": "string", 
            "description": "The name of the entry" 
          } 
        } 
      } 
    }
  ]
}
```