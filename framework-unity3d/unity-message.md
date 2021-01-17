---
title: 广播消息
date: 2016-10-27
updated: true
tag:
- unity3d
---


> 2016.10.27 更新: 这种方式在实践中得知，效率比较低，主要用在与原生代码通信上，正常开发中，简单项目可以考虑使用单例存储或读取数据，复杂项目可以考虑使用 UniRx(github)。

Unity 中广播消息的方法有三个，**SendMessage**、**BroadcastMessage** 和 **SendMessageUpwards**。学习一下用法和区别。

## 区别

先假设有这样一个游戏对象结构，Root 上挂载了 n 个组件。他子级的游戏对象都挂载 1 个组件。所有组件都含有一个名为 `Foo` 的方法。

```
- Root<Root, AnotherRoot, Roots, LastRoot, ... n ...>

    - Middle0<Middle>
    
        - Child0<Child>
        - Child1<Child>
        
    - Middle1<Middle>
    
        - Child0<Child>
```

``` csharp
void Foo (string message) {
    Debug.Log(message);
}
```

ps: 如何在 Root 中添加一个 Middle0 游戏对象？

``` csharp
// 创建游戏对象
GameObject middle0 = new GameObject("Middle0");

// 添加组件
middle0.AddComponent<Middle>();

// 放到 Root 中
middle0.transform.parent = transform;
```

### SendMessage

**游戏对象为自己身上不同组件发送消息** 

当 Root 上某一个组件调用了 `SendMessage("Foo", "Root Send Message")` 时，所有 n 个组件中的 `Foo` 函数都会被调用。

---
### BroadcastMessage

**向子级广播消息**

Middle0 使用此方法时，Middle0 和它子级 Child0，Child1 中的 `Foo` 会被触发。触发3个函数；

Root 使用该方法则触发 n + 6 个函数。

---

### SendMessageUpwards

**向父级发送消息**

Middle1 中的 Child0 使用该方法时，Middle1-Child0 和父级 Middle1，Root 上所有组件上的 `Foo` 函数都会被触发。共触发 n + 2 次；

---

## 参数

这三个方法拥有同样形式的参数，用 SendMessage 举例。

``` csharp
// 两个参数
public void SendMessage(
    string methodName, 
    SendMessageOptions options
);

// 三个参数
public void SendMessage (
    string methodName, 
    object parameter = null, 
    SendMessageOptions options = SendMessageOptions.RequireReceiver
);
```

|参数|类型||
|:--|:---:|:----|
|methodName|`string`| 被触发方法名，"Foo"|
|parameter|`object`| 被触发函数接收的参数，"Root Send Message" |
|options|`SendMessageOptions`|包含两个静态属性，<br> - 设置为 SendMessageOptions.RequireReceiver（既默认情况），当没有 Foo 函数被触发时，Unity 会报错 <br> <br> - 设置为 SendMessageOptions.DontRequireReceiver，没有 Foo 函数被触发不会报错|


## 注意

写方法名的时候不要嫌长，要不然会被莫名其妙地触发。前面可以加个类似 `receive` 前缀啥的。