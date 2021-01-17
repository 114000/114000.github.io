---
layout: post
title:  vue2 源码 - core/util
date:   2016-08-26
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
vue core 的通用代码

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

<!-- toc -->

### debug.js

非生产环境下，会导出两个函数 formatComponentName 和 warn

#### [fn]formatComponentName

返回组件的名字。可能的情况有：根实例，有名字的组件，匿名组件

``` javascript
formatComponentName = vm => {
  if (vm.$root === vm) {
    return 'root instance'
  }
  const name = vm._isVue
    ? vm.$options.name || vm.$options._componentTag
    : vm.name
  return name ? `component <${name}>` : `anonymous component`
}
```

#### [fn]warn

打印错误信息和位置。

``` javascript
const hasConsole = typeof console !== 'undefined'

warn = (msg, vm) => {
  // console 存在，非静默
  // 在 core/config.js 中配置
  if (hasConsole && (!config.silent)) {
    console.error(`[Vue warn]: ${msg} ` + (
      vm ? formatLocation(formatComponentName(vm)) : ''
    ))
  }
}
// 未暴露函数
const formatLocation = str => {
  if (str === 'anonymous component') {
    str += ` - use the "name" option for better debugging messages.`
  }
  return `(found in ${str})`
}
```
### env.js

全局的变化监听

#### [string] UA
``` javascript
const UA = inBrowser && window.navigator.userAgent.toLowerCase()
```
#### [boolean] hasProto/inBrowser/devtools

``` javascript
// 是否可以使用 __proto__
const hasProto = '__proto__' in {}

// 是否运行在浏览器中
const inBrowser =
  typeof window !== 'undefined' &&
  Object.prototype.toString.call(window) !== '[object Object]'

// 检查 devtools
const devtools = inBrowser && window.__VUE_DEVTOOLS_GLOBAL_HOOK__

```
### [fn] nextTick

nextTick 这是一个立即执行的匿名函数 `(function)()` 返回的函数，所以函数的本体是最后返回的函数。nextTick 是 vue 比较核心的一个函数，作用是**异步推迟**执行一个任务，让细小的任务在一个统一的 tick 中执行。在 [MutationObserver](https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver#MutationObserverInit) 可用的情况下使用 MutationObserver，否则使用定时器来进行异步调用。

``` javascript
// 变动监听在 iOS 9.3 以上并且，没有 IndexedDB 时才可用
const hasMutationObserverBug =
  iosVersion &&
  Number(iosVersion[0]) >= 9 &&
  Number(iosVersion[1]) >= 3 &&
  !window.indexedDB

const nextTick = (function () {
  let callbacks = []  // 所有需要在下一次 tick 中执行的任务都会被放到这个数组中
  let pending = false // 是否推迟执行
  let timerFunc       // 定时器函数

  function nextTickHandler () {
    pending = false
    const copies = callbacks.slice(0)
    // 清空引用，注意这里将任务中的引用都清空了，所以需要才需要传入 ctx 进行绑定
    callbacks = []
    // 在当前 tick 执行所有积攒的任务
    for (let i = 0; i < copies.length; i++) {
      copies[i]()
    }
  }

  /* istanbul ignore else */
  /* 上面一行注释，让之后的 else 不进行测试覆盖率检查 npm: istanbul */

  if (typeof MutationObserver !== 'undefined' && !hasMutationObserverBug) {
    var counter = 1
    var observer = new MutationObserver(nextTickHandler)
    // 文本节点
    var textNode = document.createTextNode(String(counter))
    observer.observe(textNode, {
      characterData: true // 观测目标节点的文本节点 textNode
    })
    timerFunc = function () {
      // 改变 textNode 内部的文本节点，继而触发 observer
      counter = (counter + 1) % 2
      textNode.data = String(counter)
    }
  } else {
    // 原注释：webpack 尝试为立即定时器 setImmediate 注入垫片
    // 如果立即定时器全局可用，我们则需要做一些处理避免捆绑不必要的代码
    var context = inBrowser
      ? window
      : typeof global !== 'undefined' ? global : {}
    timerFunc = context.setImmediate || setTimeout
  }

  // nextTick 本体
  return function (cb: Function, ctx?: Object) {
    const func = ctx
      ? function () { cb.call(ctx) }
      : cb
    callbacks.push(func)
    if (pending) return
    pending = true
    timerFunc(nextTickHandler, 0)
  }
})()
```

#### [set] \_Set

``` javascript
let _Set
/* istanbul ignore if */
// 上面一行注释，让之后的 if 不进行测试覆盖率检查 npm: istanbul

if (typeof Set !== 'undefined' && /native code/.test(Set.toString())) {
  // 检查原生 Set 是否可用
  _Set = Set
} else {
  // 实现一个 key 只支持是原始类型的 set
  _Set = class Set {
    set: Object;
    constructor () {
      this.set = Object.create(null)
    }
    has (key: string | number) {
      return this.set[key] !== undefined
    }
    add (key: string | number) {
      this.set[key] = 1
    }
    clear () {
      this.set = Object.create(null)
    }
  }
}

```

### lang.js

#### [fn]isReserved

检查是否以 $ 和下划线开头

``` javascript
isReserved (str: string): boolean {
  const c = (str + '').charCodeAt(0)
  return c === 0x24 || c === 0x5F
}
```
#### [fn]def

封装了一个为对象添加属性的简化函数

``` javascript
function def (obj: Object, key: string, val: any, enumerable?: boolean) {
  Object.defineProperty(obj, key, {
    value: val,
    enumerable: !!enumerable, // 是否可枚举
    writable: true,
    configurable: true
  })
}
```

#### [fn]parsePath

- `core/observer/watcher.js` {% post_link vue2core-observer Watcher %} 将表达式转化为getter函数

如果字符串中没有非字母，非. 非$，则返回一个函数用于找到某个对象中具体路径

``` javascript
const bailRE = /[^\w\.\$]/
export function parsePath (path: string): any {
  // 包含非字母，非. 非$
  if (bailRE.test(path)) {
    return
  } else {
    const segments = path.split('.')
    return function (obj) {
      for (let i = 0; i < segments.length; i++) {
        if (!obj) return
        obj = obj[segments[i]]
      }
      return obj
    }
  }
}

// eg:
let colorPath = parsePath('$some.color')
colorPath(null) // => undefined
colorPath({ $any: 12, $some: { color: 'red' } }) // => 'red'
```

### options.js

配置项会覆盖父选项和子选项的合并策略

#### [fn]mergeOptions
（待解）

``` javascript
/**
 * 将两个配置对象合并为一个新的配置对象
 * 是核心部分在实例和继承中均能使用
 */
function mergeOptions (
  parent: Object,
  child: Object,
  vm?: Component
): Object {
  normalizeComponents(child)
  normalizeProps(child)
  normalizeDirectives(child)
  const extendsFrom = child.extends
  // 递归合并
  if (extendsFrom) {
    parent = typeof extendsFrom === 'function'
      ? mergeOptions(parent, extendsFrom.options, vm)
      : mergeOptions(parent, extendsFrom, vm)
  }
  // 将子组件的混合项合并到父组件上
  if (child.mixins) {
    for (let i = 0, l = child.mixins.length; i < l; i++) {
      let mixin = child.mixins[i]
      if (mixin.prototype instanceof Vue) {
        mixin = mixin.options
      }
      parent = mergeOptions(parent, mixin, vm)
    }
  }
  const options = {}
  let key
  for (key in parent) {
    mergeField(key)
  }
  for (key in child) {
    if (!hasOwn(parent, key)) {
      mergeField(key)
    }
  }
  function mergeField (key) {
    const strat = strats[key] || defaultStrat
    options[key] = strat(parent[key], child[key], vm, key)
  }
  return options
}
```

#### [fn]resolveAsset
（待解）

### props.js

#### [fn]validateProp

验证 props 中的属性，
（待解）

``` javascript
export function validateProp (
  key: string,
  propOptions: Object,
  propsData: ?Object,
  vm?: Component
): any {
  /* istanbul ignore if */
  if (!propsData) return
  const prop = propOptions[key]
  const absent = !hasOwn(propsData, key)
  let value = propsData[key]
  // handle boolean props
  if (getType(prop.type) === 'Boolean') {
    if (absent && !hasOwn(prop, 'default')) {
      value = false
    } else if (value === '' || value === hyphenate(key)) {
      value = true
    }
  }
  // check default value
  if (value === undefined) {
    value = getPropDefaultValue(vm, prop, key)
    // since the default value is a fresh copy,
    // make sure to observe it.
    const prevShouldConvert = observerState.shouldConvert
    observerState.shouldConvert = true
    observe(value)
    observerState.shouldConvert = prevShouldConvert
  }
  if (process.env.NODE_ENV !== 'production') {
    assertProp(prop, key, value, vm, absent)
  }
  return value
}
```

``` javascript
// 用构造函数检查类型做类型检查以防在不同的 vms / iframes 下检查失败
function getType (fn) {
  const match = fn && fn.toString().match(/^\s*function (\w+)/)
  return match && match[1]
}

// eg:
getType(String) // => 'String'
```

``` javascript
// assertType 函数用于检测类型
assertType(1234, String) // => { valid: false, expectedType: 'string' }
assertType(1234, Number) // => { valid: true, expectedType: 'number' }
assertType(1234, Array)  // => { valid: true, expectedType: 'Array' }
```

### index.js

将所有文件导出，方便外部调用 eg:

``` javascript
import { nextTick } from 'core/util/env'
// 🔽
import { nextTick } from 'core/util'
```

``` javascript
export * from 'shared/util'
export * from './lang'
export * from './env'
export * from './options'
export * from './debug'
export * from './props'
export { defineReactive } from '../observer/index'
```
