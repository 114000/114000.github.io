---
title: csharp tips
date: 2017-05-10
tag:
- csharp

---

#### 6.为数组的每一项赋相同初值

``` csharp
int[] array = Enumerable.Repeat(2, 4).ToArray();
// 数组长度为4, 每一项的值为2
```

#### 5.委托的简单简单写法
``` csharp
using UnityEngine;
public class ShortDelegate {
     delegate int IntegerPipe (int input);
     IntegerPipe AddOne = input => ++input;
     Func<int, int> ReduceOne = input => --input;

     delegate void NoReturnNoInput (); 
     NoReturnNoInput PrintInt = () => { Debug.Log(1); };
     Action PrintString = () => { Debug.Log("1"); };

     delegate bool ReturnBool (int input);
     ReturnBool GetInegerValue = input => input != 0;
     Predicate<string> GetStringValue = input => input != "" && input != null;
 
     /*
     a. Delegate至少0个参数，至多32个参数，可以无返回值，也可以指定返回值类型
     b. Func至少0个参数，至多4个参数，根据返回值泛型返回。必须有返回值，不可void 
     c. Action至少1个参数，至多4个参数，无返回值 
     d. Predicate至少1个参数，至多1个参数，返回值固定为bool
    */
}
```





#### 4.lamada 表达式代替匿名函数

``` csharp
// 无参数，无返回值
() => { int a = 1; }   

// 无参数，有返回值
() => { 
     int a = 1;
     return a;
}
() => int a = 1;

// 有参数，有返回值
(a, b) => { return a + b; }
(a, b) => a + b

// 单参数可省略括号
a => a + 1

/*********/
a => b => a + b
```

#### 3.约束类型

``` csharp
T AddChildComponent<T> (string findPath) where T: MonoBehaviour {
     var childTransform = transform.FindChild(findPath);
     return childTransform.gameObject.AddComponent<T>();
}

```

#### 2.常量

``` csharp
public class Foo {
  // 静态常量: 声明时必须赋值, 只能编译时初始化
  const int MAX_COUNT = 6;

  // 实例常量: 可以在运行时初始化
  readonly Vector3 POSITION = new Vector3(1, 12, 3);
  readonly Color COLOR;
  public Foo (Color color) { COLOR = color; }
}
```


#### 1.获取泛型默认值

``` csharp
public T getDefault<T> () { return default(T); }
```