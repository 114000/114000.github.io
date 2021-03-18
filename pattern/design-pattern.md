## 一. 设计原则

#### 1.1 开放-关闭原则

- 类应该对拓展开放，对修改关闭 
- 通常会引入新的抽象层次增加代码的复杂度

#### 1.2 最少知识原则 Least Knowledge

- 减少对象之间的交互，只留下必要的东西
- 德墨忒尔法则：Law of Demeter

#### 1.3 单一责任 

- 一个类应该只有一个引起变化的原因
- 类的目的，管理某种聚合，尽量让每个类保持单一的责任。
- __内聚(cohesion)__用来度量一个类或模块是否紧密地达到单一目的或责任

#### 1.4 要依赖抽象，不要依赖具体类。

- 依赖倒置 Dependency Inversion Principle
  1. 变量不可以持有具体类
  2. 不要让类派生自具体类
  3. 不要覆盖基类中的具体方法

- 不能让高层组件依赖底层组件，这两者都应该依赖于抽象

#### 1.5 多用组合，少用继承

- HAS-A(1/n) 比 IS-A(1/1)有更好的适用性


#### 1.6 好莱坞原则 dont call us, we'll call you

- 高层组件控制以及如何让低层组件参与，低层组件不可以直接调用高层组件。减少环形依赖


#### 1.7 找出应用中可能的变化之处，把他们独立出来，不要和那些不需要变化的代码混合在一起

- _me: 对行为进行抽象的意义大于对属性的抽象_

#### 1.8 针对接口编程，而非针对现实编程

#### 1.9 为了交互对象的松耦合设计而努力，将对象之间的相互依赖降到最低

- 松耦合的设计之所以能让我们建立有弹性的oo系统，能够应对变化，是因为对象之间的互相依赖降到了最低

## 二. 基本设计模式

- 模式: 在某情境(context)下, 针对某问题的某种解决方案.
  - **情境**就是应用某个模式的情况, 这应该是会不断出现的情况(e.g. 你有一个对象的集合)
  - **问题**就是你想在某情境下达到的目标, 但也可以是某情境下的约束(你需要注意走访每个对象,而且不需理会该集合的实现)
  - **解决方案**就是你所追求的:一个通用的设计,用来解决约束,达到目标.


- 分类
  - 创建型: 创建型模式涉及到将对象实例化, 这类模式都提供一个方法,将客户从所需要实力化的对象中解耦
  - 结构型: 可以让你把类或对象组合到更大得我结构中
  - 行为型: 只要是行为型模式, 都涉及到类和对象何如交互及分配职责

- 类/对象分类
  - 类模式: 描述类之间的关系如何通过继承定义.类模式的关系是在编译时建立的
    - Template Method, Fatory Method, Adapter, Interpreter
  - 对象模式: 描述对象之间的关系,而且主要是利用组合定义.对象模式的关系通常在运行时建立,而且更加动态,更有弹性

### 2.1 创建型



#### (1)单例 Singleton

> 确保一个类只有一个实例，并提供一个全局访问点

* Keywords: Unique Instance, Lazy Instantiate
* Features:
  - 推迟创建对象（不同于静态类），在C++ 中负责隔绝动态初始化的不可预知性
  - 私有化构造器，使外部无法实例化
* Scenes: 当需要一个“协调者”的时候去使用单例。数据库连接，线程池，对话框，缓存，偏好设置，日志，设备驱动。
* implement: 利用静态变量记录实例，每次调用时检查实例

  ``` java
  public class Singleton {
    private volatile static Singleton uniqueInstance;

    private Singleton () {}
    
    public static Singleton getInstance () {
      if (uniqueInstance == null) {
        // 多线程下的单例, 双重检查锁
        sychronized (Singleton.class) {
          if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
          }
        }
      }

      return uniqueInstance;
    }
  }
  ```

* Note
  - 非OO语言可以使用命名空间实现（闭包可以理解为隔离出全局的命名空间）
  - 可以通过与**工厂模式**的结合，提供该单例的子类化拓展
  - 当单例模式出现时，往往表明系统中的模块可能耦合性比较高，或者逻辑过度分散在代码库。使得单例测试更加困难

#### (2)工厂方法 Factory Method

**(2.1)简单工厂 Simple Factory**

> 工厂方法用来处理对象的创建并将这些行为封装在子类中

* Implement:

  ``` java
  public class SimplePizzaFactory {
    public Pizza createPizza (String type) {
      Pizza pizza = null;

      if (type.equals("cheese"))
        pizza = new CheesePizza();

      else if (type.equals("pepperoni"))
        pizza = new PepperoinPizza();

      else if (type.equals("veggie"))
        pizza = new VeggiePizza();
    
      return pizza;
    }
  }
  ```

**(2.1.1)静态工厂 Static Factory**

> 利用静态方法定义一个简单工厂

* Notes:
  - 不需要使用创建对象的方法来实例化对象
  - 但不能通过继承来改变创建方法的行为。


**(2.2)工厂方法 Factory Method**

> 定义了一个创建对象的接口，但在编写子类时决定要实例化哪一个。工厂方法让类把实例化推迟到了子类

* Implement: 具体实现时分成两种类别，一是创建者（Creator）PizzaStore及其子类，另一种是产品 Pizza及其子类

``` java
// 创建者
public abstract class PizzaStore {
  
  public Pizza orderPizza(String type) {
    Pizza pizza;

    pizza = createPizza(type);
    
    pizza.prepare();
    pizza.bake();
    // ...
    return pizza;
  }
  // 具体的工厂方法由子类实现
  protected abstract Pizza createPizza (String type);
}

public class NewYorkPizzaStore extends PizzaStore {
  public Pizza createPizza (String type) {
    if (type == "cheese") 
      return new NYStyleCheesePizza();
    else if 
      // ...
  }
}

//  产品
public abstract class Pizza {
  // 属性
  // 方法
  void prepare { /* ... */ }
  void bake { /* ... */ }
}

public class NYStyleCheesePizza extends Pizza {
  // ...
}
```

#### (3)抽象工厂 Abstract Factory

> 提供一个接口，用于创建相关或依赖对象的家族，而不明确指定具体类。产品家族集合了相关产品。

* Implements:

  ``` java
  // defind
  public abstract class AbstractDuckFactory {
    public abstract Quackable createMallardDuck();
    public abstract Quackable createRedheadDuck();
  }

  public class Example {
    foo (AbstractDuckFactory duckFactory) {
      Quackable mallardDuck = duckFactory.createMallardDuck();
      Quackable redheadDuck = duckFactory.createRedheadDuck();
    }
  }
  ```



**(2)(3) 工厂模式**

* Keywords: Factory, Creator, Store, no-new

* Scenes: 
  - 当对象或组件设置涉及高复杂性时
  - 当需要根据所在的不同环境轻松生成对象的的不同实例时
  - 当处理很多共享属性的小型对象或组件时，即创建对象时会有很多重复操作
  - 当编写值需要满足一个API契约（鸭子模型）的其他对象的实例对象时。对解耦很有用
  - 编译时不知道具体类型时

* Notes: 
  - 工厂方法将客户代码从需要实例化的具体类中解耦。即使只有一个需要创建的对象，工厂方法依然很有用，因为它帮助我们将产品的“实现”从“使用”中解耦，所以即使**增加产品或改变产品的实现**抽象创建者也不会受到影响。
  - 增加了创建对象的复杂度，也可能对单元测试带来问题

#### (4)原型 Prototype

#### (5)生成器 Builder

### 2.2 结构型

#### (6)装饰器 Decorator 

#### (7)适配器 Adapter
 
#### (8)外观 Facade

#### (9)代理 Proxy

#### (10)组合 Composite

#### (11)享元 Flyweight

#### (12)桥接 Bridge 

通过将实现和抽象放在两个不同的类层次中而使他们可以独立改变

- Features:
  - 将实现予以解耦,让它和界面之间不再永久绑定.
  - 抽象和实现可以独立扩展, 不会影响到对方
  - 对于"具体的抽象类"所做的改变,不会影响到客户
- Notes:
  - 适合使用在需要跨越多个平台的图形和窗口系统上
  - 当需要不同的方式改变接口和实现时,你会发现桥接模式很好用
  - 桥接模式的缺点是增加了复杂度

### 2.3 行为型


#### (13)命令 Command

#### (14)策略 Strategy

#### (15)模板方法 Template Method

#### (16)观察者 Observer

#### (17)状态 State

#### (18)迭代器 Iterator

#### (19)解释器 Interpreter

#### (20)备忘录 Memento

#### (21)中介者 Mediator

#### (22)访问者 Visuitor

#### (23)责任链 Chain if Responsibility


## 复合模式 Compound Pattern

模式通常会在一起使用, 并被组合在同一个设计方案中

> 复合模式在一个解决方案中结合两个或多个模式,以解决**一般或重复发生**的问题. 普通的模式的组合使用不能成为复合模式

### MVC

- 模型: 模型所持所有的数据, 状态和程序逻辑. 模型没有注意到视图和控制器, 虽然它提供了操纵和检索状态的接口,并发送状态改变通知给观察者
  - 模型使用观察者模式,以便观察者更新,同时保持两者之间解耦.
  - 可以用适配器将新的模型适配到原来的视图和控制器上
- 视图: 用来呈现模型. 视图通常直接从模型中取得它需要显示的状态与数据
  - 视图使用组合模式实现用户界面,用户界面通常组合了嵌套的组件,像面板,框架和按钮
- 控制器: 取得用户的输入并解读其对模型的意思. 
  - 是视图和模型的沟通桥梁, **不包含应用逻辑**
  - 控制器并不是彻底的中介者, 视图持有访问模型状态的**模型引用**, 并没有通过控制器获取模型状态. 
  - 控制器是视图的策略,视图可以使用不同的控制器实现,得到不同的行为


## 反模式

采用不好的方案解决一个问题

### 黄金榔头

- 问题: 你需要为你的开发选择技术, 而且你正好有一种技术能够主宰这个架构
- 情境: 你需要开发某个新的系统或者一套软件, 然而此系统或软件却无法和开发团队缩熟悉的技术相吻合.
- 吸引力: 
  - 开发者致力于使用他们所熟悉的技术
  - 开发团队并不熟悉其他技术
  - 采用不熟悉的技术被认为风险比较高
  - 使用熟悉的技术做开发,比较容易规划和预估

- 原本的解决方案: 反正就使用熟悉的技术好了.将熟悉的技术强迫性地用在许多问题上, 甚至在明显不适当的地方也照用
- 重构的解决方案: 开发人员通过教育, 培训和读书会,可以学会新的解决方案
- 例子: 当采用开放源码的代替品时, Web公司依然持续使用并维护他们内部自行开发的缓存系统