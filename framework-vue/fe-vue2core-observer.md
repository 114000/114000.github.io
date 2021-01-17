---
layout: post
title:  vue2 源码 - core/observer
date:   2016-08-31
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---

观察者

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

<!-- toc -->

## index.js

### [object] observerState
默认情况下，当设置一个响应值时，这个值就会被转化成可响应的。但是当向下传递 props 的时候，由于它可能被嵌套在一个不可变的数据结构中，因此我们可能不想转化它。因为转化它会影响性能。

``` javascript
const observerState = {
  shouldConvert: true,
  isSettingProps: false
}
```

### [class] Observer
Observer 类被绑定到每一个观测对象上，只要绑定一次，实例就会将目标对象的属性都转化为 getter/setter 形式，这样就可以收集依赖，并派发更新了。[`Object.getOwnPropertyNames`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)返回一个由指定对象的所有自身属性的属性名（包括不可枚举属性）组成的数组。
``` javascript

const arrayKeys = Object.getOwnPropertyNames(arrayMethods)

class Observer {
  constructor (value: any) {
    this.value = value
    this.dep = new Dep()
    this.vmCount = 0 // 有几处 vms 将这个对象作为根 $data

    // 将 Observer 的实例赋值给被观测对象的 __ob__ 属性
    def(value, '__ob__', this)

    if (Array.isArray(value)) {
      // core/util/env.js 能否是用 __proto__
      // ./array.js arrayMethods
      const augment = hasProto
        ? protoAugment // 🔽
        : copyAugment // 🔽
      augment(value, arrayMethods, arrayKeys)
      this.observeArray(value)
    } else {
      this.walk(value)
    }
  }

  // 将每一个属性转化为 getter/setter 形式
  // 这个方法的参数类型只能为 Object
  walk (obj: Object) {
    const val = this.value
    for (const key in obj) {
      // 定义可响应的属性值
      defineReactive(val, key, obj[key])
    }
  }

  // 观测数组中的所有项
  observeArray (items: Array<any>) {
    for (let i = 0, l = items.length; i < l; i++) {
      observe(items[i])
    }
  }
}

// 使用 __proto__ 拦截原型链来达到增强目标对象/数组的目的（arrayMethods）
function protoAugment (target, src: Object) {
  target.__proto__ = src
}

// 定义隐藏的属性值来达到增强目标对象/数组的目的（arrayMethods）
function copyAugment (target: Object, src: Object, keys: Array<string>) {
  for (let i = 0, l = keys.length; i < l; i++) {
    const key = keys[i]
    def(target, key, src[key])
  }
}
```

### [fn] defineReactive

在对象上定义一个可响应的属性， 函数 [`Object.getOwnPropertyDescriptor`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor) 返回一个描述当前属性（obj[key]）特性的对象

``` javascript
export function defineReactive (
  obj: Object,
  key: string,
  val: any,
  customSetter?: Function
) {
  const dep = new Dep()
  const property = Object.getOwnPropertyDescriptor(obj, key)
  // 属性可以配置（改变或删除）
  if (property && property.configurable === false) {
    return
  }

  // 之前定义过的 getter/setter
  const getter = property && property.get
  const setter = property && property.set

  let childOb = observe(val)
  Object.defineProperty(obj, key, {
    enumerable: true, // 可枚举
    configurable: true, // 可改变可删除
    get: function reactiveGetter () {
      // getter 返回值
      const value = getter ? getter.call(obj) : val
      if (Dep.target) {
        // 为当前唯一 watcher（Dep.target） 添加观察依赖项
        dep.depend()
        if (childOb) {
          // 为当前唯一 watcher（Dep.target） 添加观察依赖项
          childOb.dep.depend()
        }
        if (Array.isArray(value)) {
          for (let e, i = 0, l = value.length; i < l; i++) {
            e = value[i]
            // 为当前唯一 watcher（Dep.target） 添加观察依赖项
            e && e.__ob__ && e.__ob__.dep.depend()
          }
        }
      }
      return value
    },
    set: function reactiveSetter (newVal) {
      const value = getter ? getter.call(obj) : val

      if (newVal === value) {
        // 新值与旧值相等
        return
      }
      if (process.env.NODE_ENV !== 'production' && customSetter) {
        // 非生产环境下自定义执行
        customSetter()
      }
      if (setter) {
        setter.call(obj, newVal)
      } else {
        val = newVal
      }
      // 观测新的值
      childOb = observe(newVal)
      // 通知属性值已经改变
      dep.notify()
    }
  })
}
```

### [fn] observe
尝试为 value 创建一个 observer 实例，如果监听成功返回这个新实例。如果 value 已经被观测，则返回已有的 observer 实例
``` javascript
function observe (value: any): Observer | void {
  if (!isObject(value)) {
    return
  }
  let ob: Observer | void
  if (hasOwn(value, '__ob__') && value.__ob__ instanceof Observer) {
    // 如果已经有 observer
    ob = value.__ob__
  } else if (
    observerState.shouldConvert &&
    !config._isServer &&
    (Array.isArray(value) || isPlainObject(value)) &&
    Object.isExtensible(value) &&
    !value._isVue // 不是 Vue 系统值
  ) {
    ob = new Observer(value)
  }
  return ob
}
```

### [fn] set

设置对象的属性值，如果这个属性值之前不存在则添加这个新属性并触发变化通知。

``` javascript
function set (obj: Array<any> | Object, key: any, val: any) {
  if (Array.isArray(obj)) {
    obj.splice(key, 1, val)
    return val
  }
  if (hasOwn(obj, key)) {
    obj[key] = val
    return
  }
  // 是新属性
  const ob = obj.__ob__

  // 不能为 Vue 系统对象或者其根 $data 添加属性
  if (obj._isVue || (ob && ob.vmCount)) {
    process.env.NODE_ENV !== 'production' && warn(
      'Avoid adding reactive properties to a Vue instance or its root $data ' +
      'at runtime - delcare it upfront in the data option.'
    )
    return
  }
  // 为没被监控的对象添加属性
  if (!ob) {
    obj[key] = val
    return
  }
  // 为监控的对象添加可响应的属性值
  defineReactive(ob.value, key, val)
  // 派发通知
  ob.dep.notify()
  return val
}
```

### [fn] del

删除一个属性

``` javascript
function del (obj: Object, key: string) {
  const ob = obj.__ob__
  if (obj._isVue || (ob && ob.vmCount)) {
    process.env.NODE_ENV !== 'production' && warn(
      'Avoid deleting properties on a Vue instance or its root $data ' +
      '- just set it to null.'
    )
    return
  }
  if (!hasOwn(obj, key)) {
    return
  }
  delete obj[key]
  // 如果没有被观测则不通知删除
  if (!ob) {
    return
  }
  ob.dep.notify()
}

```
## array.js

### [object] arrayMethods

实现一个能通知变化的新的 Array

``` javascript
const arrayProto = Array.prototype
export const arrayMethods = Object.create(arrayProto)

// 拦截能改变数组的方法，并派发事件
;[ 'push', 'pop', 'shift', 'unshift', 'splice', 'sort', 'reverse']
.forEach(function (method) {

  // 保存原来的方法 eg: Array.prototype.pop
  const original = arrayProto[method]

  // /core/util/lang.js [obj, key, val]
  def(arrayMethods, method, function mutator () {

    // 避免遗漏参数: http://jsperf.com/closure-with-arguments
    let i = arguments.length
    const args = new Array(i)
    while (i--) {
      args[i] = arguments[i]
    }

    const result = original.apply(this, args)

    // core/observer/index.js
    const ob = this.__ob__
    let inserted
    switch (method) {
      case 'push':
        inserted = args
        break
      case 'unshift':
        inserted = args
        break
      case 'splice':
        inserted = args.slice(2)
        break
    }
    // 如果有新插入的元素[数组]，对其添加监听
    if (inserted) ob.observeArray(inserted)

    // 通知变化
    ob.dep.notify()
    return result
  })
})

```

## dep.js

### [class] Dep

Dep 实例是可观察的，可以有多个指令同时订阅它。目标 wather 被置于栈顶

``` javascript
let uid = 0

class Dep {
  constructor () {
    this.id = uid++
    this.subs = []  // 订阅实例的 Watcher 数组
  }
  // 添加订阅
  addSub (sub: Watcher) {
    this.subs.push(sub)
  }
  // 删除订阅
  removeSub (sub: Watcher) {
    // shard/util.js 数组中删除一项
    remove(this.subs, sub)
  }

  depend () {
    if (Dep.target) {
      Dep.target.addDep(this)
    }
  }
  // 通知所有订阅者执行更新操作
  notify () {
    // ？先稳定订阅者列表
    const subs = this.subs.slice()
    for (let i = 0, l = subs.length; i < l; i++) {
      subs[i].update()
    }
  }
}

// 当前目标（target） watcher 处于计算中
// 任何情况下只会有一个 watcher 处于计算状态
// 所有 Dep.target 是唯一的
Dep.target = null

// 目标栈
const targetStack = []

```
### [fn] pushTarget

目标 watcher 入栈

``` javascript
function pushTarget (_target: Watcher) {
  if (Dep.target) targetStack.push(Dep.target)
  Dep.target = _target
}
```

### [fn] popTarget

推出栈顶 watcher

``` javascript
function popTarget () {
  Dep.target = targetStack.pop()
}
```

## scheduler.js

### [fn] queueWatcher

将一个 watcher 推进监视队列，拥有重复 ID 的任务会被跳过，除非当队列正在被刷新是他被推了进去。

``` javascript
const queue: Array<Watcher> = []
let has: { [key: number]: ?true } = {}
let circular: { [key: number]: number } = {}
let waiting = false
let flushing = false
let index = 0

function queueWatcher (watcher: Watcher) {
  const id = watcher.id
  if (has[id] == null) {
    has[id] = true
    if (!flushing) {
      queue.push(watcher)
    } else {
      // if already flushing, splice the watcher based on its id
      // if already past its id, it will be run next immediately.
      let i = queue.length - 1
      while (i >= 0 && queue[i].id > watcher.id) {
        i--
      }
      queue.splice(Math.max(i, index) + 1, 0, watcher)
    }
    // queue the flush
    if (!waiting) {
      waiting = true
      nextTick(flushSchedulerQueue)
    }
  }
}
```

## watcher.js/[class] Watcher

-  `core/instance/state.js` {% post_link vue2core-instance Vue.prototype.$watch %} 由此实现

### 构造函数

``` javascript
class Watcher {
  constructor (
    vm: Component,
    expOrFn: string | Function,
    cb: Function,
    options?: Object = {}
  ) {
    this.vm = vm
    vm._watchers.push(this)
    // options
    this.deep = !!options.deep // boolean 深度监听
    this.user = !!options.user // boolean 用户使用
    this.lazy = !!options.lazy // boolean
    this.sync = !!options.sync // boolean 同步更新
    this.expression = expOrFn.toString() // string
    this.cb = cb    // Function
    this.id = ++uid // number 用于计数
    this.active = true  // boolean
    this.dirty = this.lazy // boolean 脏检查
    this.deps = [] // Array<Dep>
    this.newDeps = [] // Array<Dep>
    this.depIds = new Set() //Set
    this.newDepIds = new Set() // Set

    // 将 expOrFn 转为 getter
    if (typeof expOrFn === 'function') {
      this.getter = expOrFn
    } else {
      // /core/util/lang.js [fn] parsePath
      // 返回一个函数，用于获取传入对象的 expOrFn 路径
      this.getter = parsePath(expOrFn)
      if (!this.getter) {
        this.getter = function () {}
        process.env.NODE_ENV !== 'production' && warn(
          `Failed watching path: "${expOrFn}" ` +
          'Watcher only accepts simple dot-delimited paths. ' +
          'For full control, use a function instead.',
          vm
        )
      }
    }
    this.value = this.lazy
      ? undefined
      : this.get()
  }
  // 实例方法 ...
}
```

### [fn] watcher.get
执行 getter 并重新依赖
``` javascript
get () {
  // core/observer/dep.js
  pushTarget(this)
  const value = this.getter.call(this.vm, this.vm)
  // "touch" every property so they are all tracked as
  // dependencies for deep watching
  if (this.deep) {
    traverse(value)
  }
  // core/observer/dep.js
  popTarget()
  this.cleanupDeps()
  return value
}
```

### [fn] watcher.addDep

为指令添加一个依赖项

``` javascript
addDep (dep: Dep) {
  const id = dep.id
  if (!this.newDepIds.has(id)) {
    this.newDepIds.add(id)
    this.newDeps.push(dep)
    if (!this.depIds.has(id)) {
      dep.addSub(this)
    }
  }
}
```

### [fn] watcher.cleanupDeps

清空依赖的集合，用新的依赖替换旧的依赖

``` javascript
cleanupDeps () {
  let i = this.deps.length
  while (i--) {
    const dep = this.deps[i]
    if (!this.newDepIds.has(dep.id)) {
      dep.removeSub(this)
    }
  }
  let tmp = this.depIds
  this.depIds = this.newDepIds
  this.newDepIds = tmp // 清除引用
  this.newDepIds.clear()
  tmp = this.deps
  this.deps = this.newDeps
  this.newDeps = tmp // 清除引用
  this.newDeps.length = 0
}
```

### [fn] watcher.update

调度程序接口，当依赖项发生变化时调用

``` javascript
update () {
  if (this.lazy) {
    this.dirty = true
  } else if (this.sync) {
    this.run()
  } else {
    // ./scheduler.js
    queueWatcher(this)
  }
}
```

### [fn] watcher.run

调度程序处理接口，由事务调用

``` javascript
run () {
  if (this.active) {
    const value = this.get()
    if (
      value !== this.value ||
      // Deep watchers and watchers on Object/Arrays should fire even
      // when the value is the same, because the value may
      // have mutated.
      isObject(value) ||
      this.deep
    ) {
      // set new value
      const oldValue = this.value
      this.value = value
      if (this.user) {
        try {
          this.cb.call(this.vm, value, oldValue)
        } catch (e) {
          process.env.NODE_ENV !== 'production' && warn(
            `Error in watcher "${this.expression}"`,
            this.vm
          )
          /* istanbul ignore else */
          if (config.errorHandler) {
            config.errorHandler.call(null, e, this.vm)
          } else {
            throw e
          }
        }
      } else {
        this.cb.call(this.vm, value, oldValue)
      }
    }
  }
}
```

### [fn] watcher.evaluate

计算实例的值，只会被惰性 watcher 调用

``` javascript
evaluate () {
  this.value = this.get()
  this.dirty = false
}
```

### [fn] watcher.depend

用实例依赖所有的依赖集合中的项目

``` javascript
depend () {
  let i = this.deps.length
  while (i--) {
    this.deps[i].depend()
  }
}
```

### [fn] watcher.teardown

将实例从所有的依赖的调度列表中删除

``` javascript
teardown () {
  if (this.active) {
    // remove self from vm's watcher list
    // this is a somewhat expensive operation so we skip it
    // if the vm is being destroyed or is performing a v-for
    // re-render (the watcher list is then filtered by v-for).
    if (!this.vm._isBeingDestroyed && !this.vm._vForRemoving) {
      remove(this.vm._watchers, this)
    }
    let i = this.deps.length
    while (i--) {
      this.deps[i].removeSub(this)
    }
    this.active = false
  }
}
```

---
