---
layout: post
title: "Unity (C#) 使用 LitJson 处理 JSON 数据"
date: 2016-10-24
categories: Unity3D
tag:
  - Unity3D
  - csharp
---

## 相关链接
1. [dll 文件，点击即下载](https://github.com/lbv/litjson/releases/download/v0.9.0/LitJson.dll)
2. [LitJson 官网](http://lbv.github.io/litjson/)

## 声明命名空间

``` csharp
using LitJson;
```

ps:  直接将 `.dll` 文件拖入 Unity 的 Assets 目录中便可以使用了

## 转换

1. 实例转换为JSON

  ``` csharp
  public class Pet {
    public string name;
    public int age;
    string color;
    public void Bark () {/***/}
  }

  /*-------------*/
  using LitJson;
  ...
  JsonMapper.ToJson(new Pet());
  // => string: "{ 'name': null, 'age': 0 }"
  ```

PS: 实例方法和未公开的属性不会被转化

2. 嵌套实例对象转换为JSON

  ``` csharp
  public class PetColor {
    public int r;
    public int g;
    public int b;
  }

  public class Pet {
    public string name;
    public int age;
    public PetColor color;
  }
  ```

  ``` csharp
  var petA = new Pet();
  petA.name = "Leokk";
  petA.age = 12;
  petA.color = new PetColor();
  JsonMapper.ToJson(petA);
  // => string: 
  // "{'name':'Leokk', 'age':12, 'color': {'r':0, 'g':0, 'a':0}}"
  ```

3. 常用类型转JSON

 交错数组转JSON

  ``` csharp
  var array = new string[][] { 
    new string[]{ "bar", "foo" }, 
    new string[]{ "baz" }
  };
  JsonMapper.ToJson(array);
  // => string: "[["bar","foo"],["baz"]]"
  ```

 二维数组转JSON

  ``` csharp
  var array = new int[,] { 
    { 1, 2, 3 }, { 55, 56, 57 }
  };
  JsonMapper.ToJson(array);
  // => string: "[1, 2, 3, 55, 56, 57]"
  ```

 列表转JSON

  ``` csharp
  var list = new List<bool>(new bool[]{ true, false });
  JsonMapper.ToJson(list);
  // => string: "[true, false]"
  ```

4. JSON 字符串转为特定类的实例

  ``` csharp
  class Pet { 
    public string name; 
    public int age;
  }

  var b = "{ 'name': 'Misha', 'age': 3 }";
  var petB = JsonMapper.ToObject<Pet>(b);
  // => Pet: { name: "Misha", age: 3 }
  ```

为静态方法 JsonMapper.ToObject 指定**泛型**即可。注意属性要一一对应。

5. 使用泛型将JSON 转为常用的类型

  ``` csharp
  string arrayStr = "[1, 2, 3, 11, 12, 13]";
  JsonMapper.ToObject<int[]>(arrayStr)[3];
  // => int: 11
  ```

  ``` csharp
  var arrayStr = "[['foo', 'baz'], ['bar']]";
  var array = JsonMapper.ToObject<string[][]>(arrayStr);
  array[1][0];
  // => string: "bar"
  ```

ps: 使用泛型时 `ToObject` 的参数只能为字符串形式，而不能以JsonData 类型的变量作为参数

不能将 `List<int[]>` 转换为交错数组

## 创建 JsonData 实例
1. 创建字典型实例

  ``` csharp
  var petC = new JsonData();
  
  petC["name"] = "Huffer";
  petC["age"] = 4;

  petC.ToJson();
  // => string: "{ 'name': 'Huffer', 'age': 4 }"
  ```

2. 创建数组型实例，使用了实例方法 `Add`

  ``` csharp
  var rexxarsPets = new JsonData();
  
  rexxarsPets.Add(petCA);
  rexxarsPets.Add(petCB);
  rexxarsPets.Add(petC);

  rexxarsPets.ToJson();

  /* => string:
  "[
    { 'name': 'Leokk', 'age': 2 },
    { 'name': 'Misha', 'age': 3 },
    { 'name': 'Huffer', 'age': 4 }
  ]"
  */
```
一旦将 JsonData 实例使用上述一种方式向内部添加元素之后，便不能再使用另一种方法进行添加了，即使使用下面的方法清空了实例也不行。



### 循环

1. 使用属性 `Count` 配合 `for` 关键字循环，可以用来循环像数组结构的 JsonData 实例。
  
  ``` csharp
  string  nameArrayString = "['Leokk', 'Misha']";
  JsonData nameArray = JsonMapper.ToObject(nameArrayString);

  for (int i = 0; i < nameArray.Count; i++) {
    (string)nameArray[i];
  }
  // "Leokk"
  // "Misha"
  ```

  也可以用来循环正常的 JsonData 实例。

  ``` csharp
  for (int i = 0; i < petA.Count; i++) {

    JsonData item = jsonDataA[i];

    if (item.IsString)
      Debug.Log((string)item);
    else if (item.isInt)
      Debug.Log((int)item)
  }
  // "Leokk"
  // 2
  ```

实例自带一些布尔类型的属性，用来判断当前键值的类型
`IsArray`，`IsBoolean`，`IsDouble`，`IsInt`，`IsLong`，`IsObject`，`IsString`

2. 使用属性 `Keys` 配合 `foreach` 关键字进行循环，JsonData 实现了 `IDictionary`  接口。此方法不能循环数组形式的 JsonData 实例。

  ``` csharp
  foreach (string key in jsonDataA.Keys) {
    key;
    (string)jsonDataA[key];
    jsonDataA[key].ToJson();
  }
  // "name" "Leokk" "Leokk"
  // "age" Error int 不能转为 string "2"
  ```

在第二次循环中，试图将数字 2 强制转换为 `string` 所以会报错。


## 访问属性

1. JSON 字符串转换为 JsonData 实例

  ``` csharp
  petA["name"]; // JsonData 类型 Leokk
  
  petA["name"].ToJson(); // "Leokk"
  petA["age"].ToJson();  // "2"
  
  (string)jsonDataA["name"];  // "Leokk"
  (int)jsonDataA["age"]       // 2
  ```

3. JsonData /  类实例转换为 JSON 字符串

  ``` csharp
  string reloadA = JsonMapper.ToJson(jsonDataA);
  string reloadA = jsonDataA.ToJson();

  // "{ 'name': 'Leokk', 'age': 2 }"
  
  string reoloadB = JsonMapper.ToJson(petB);  
  
  // "{ 'name': 'Misha', 'age': 3 }"
  ```
  这里需要注意一点，JsonData 实例自带 `ToJson` 方法将自身转为字符串。静态方法 `JsonMapper.ToJson` 主要用于将其他的类实例（如：`petB`）转化为 JSON 字符串.

## 清空

实例方法 `.Clear` 用于清空实例内部全部属性。返回 `[]` 或 `{}`。暂没发现有删除单个属性的方法。

## 最后

命名空间中还有 `JsonReader`，`JsonWriter` 类，用法参考[链接](http://www.cnblogs.com/peiandsky/archive/2012/04/20/2459219.html) 是ToJson, ToObject 的具体实现方法。