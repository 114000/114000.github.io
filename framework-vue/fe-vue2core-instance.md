---
layout: post
title:  vue2 源码 - core/instance
date:   2016-08-30
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
这块代码主要作用
1. 初始化字段选项
2. 为 Vue 添加实例方法
3. 添加生命周期钩子函数

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

<!-- toc -->

## index.js

``` javascript
import { initMixin } from './init'
import { stateMixin } from './state'
import { renderMixin } from './render'
import { eventsMixin } from './events'
import { lifecycleMixin } from './lifecycle'

function Vue (options) {
  this._init(options)
}

// 添加 Vue.prototype._init
initMixin(Vue)

// 添加 Vue.prototype.$data/$watch/$set/$delete      
stateMixin(Vue)

// 添加 Vue.prototype.$on/$off/$once/$emit
eventsMixin(Vue)

// 添加 Vue.prototype._mount/_update/_updateFromParent/$forceUpdate/$destroy  
lifecycleMixin(Vue)

// 2.0 新增 render 选项

renderMixin(Vue)

// 导出 Vue 构造函数
export default Vue
```

## init.js

### [fn] initMixin

为 Vue 的实例添加 \_init 函数，这个函数接收一个 options[object] 作为参数，将其合并到原始的 options 上后进行初始化操作。

``` javascript
function initMixin (Vue: Class<Component>) {
  Vue.prototype._init = function (options?: Object) {
    const vm: Component = this

    // 唯一的 uid
    vm._uid = uid++

    // 防止被观察（observed）的标记
    vm._isVue = true

    // 合并配置项
    if (options && options._isComponent) {

      // 优化内部组件实例，因为动态的配置项合并相当慢
      // 内部的组件配置项并不需要特殊处理 🔽🔽🔽 函数实现在下面
      initInternalComponent(vm, options)

    } else {
      // 没有传入配置项 || 传入的配置项不是组件
      vm.$options = mergeOptions(
        resolveConstructorOptions(vm), // 解析构造函数配置项 🔽🔽🔽 函数实现在下面
        options || {},
        vm
      )
    }

    if (process.env.NODE_ENV !== 'production') {
      initProxy(vm)
    } else {
      vm._renderProxy = vm
    }
    // expose real self
    vm._self = vm
    initLifecycle(vm)
    initEvents(vm)
    callHook(vm, 'beforeCreate')
    initState(vm)
    callHook(vm, 'created')
    initRender(vm)
  }

  function initInternalComponent (vm: Component, options: InternalComponentOptions) {
    const opts = vm.$options = Object.create(resolveConstructorOptions(vm))
    // 这样做比动态枚举更快
    opts.parent = options.parent
    opts.propsData = options.propsData
    opts._parentVnode = options._parentVnode
    opts._parentListeners = options._parentListeners
    opts._renderChildren = options._renderChildren
    opts._componentTag = options._componentTag
    if (options.render) {
      opts.render = options.render
      opts.staticRenderFns = options.staticRenderFns
    }
  }

  function resolveConstructorOptions (vm: Component) {
    const Ctor = vm.constructor
    let options = Ctor.options
    if (Ctor.super) {
      const superOptions = Ctor.super.options
      const cachedSuperOptions = Ctor.superOptions
      if (superOptions !== cachedSuperOptions) {
        // 根组件配置项改变
        Ctor.superOptions = superOptions
        // /core/util/[fn]merageOptions
        options = Ctor.options = mergeOptions(superOptions, Ctor.extendOptions)
        if (options.name) {
          // 如果有组件名
          options.components[options.name] = Ctor
        }
      }
    }
    return options
  }
}

```

## state.js

### [fn] initState

在 Vue.prototype.\_init 被调用，初始化组件的选项

``` javascript
function initState (vm: Component) {
  vm._watchers = []
  initProps(vm)
  initData(vm)     
  initComputed(vm)
  initMethods(vm)
  initWatch(vm)
}
```

### [fn] stateMixin

``` javascript
function stateMixin (Vue: Class<Component>) {
  // flow 会在使用 Object.defineProperty 直接声明定义对象是发生一些问题。
  // 所以我们在这逐步建立对象 ？
  const dataDef = {}
  dataDef.get = function () {
    return this._data
  }
  if (process.env.NODE_ENV !== 'production') {
    dataDef.set = function (newData: Object) {
      warn(
        'Avoid replacing instance root $data. ' +
        'Use nested data properties instead.',
        this
      )
    }
  }
  Object.defineProperty(Vue.prototype, '$data', dataDef)

  // observer/index
  Vue.prototype.$set = set
  Vue.prototype.$delete = del

  // 返回一个可以结束当前 watch 的函数
  Vue.prototype.$watch = function (
    expOrFn: string | Function,
    cb: Function,
    options?: Object
  ): Function {
    const vm: Component = this
    options = options || {}
    // ?
    options.user = true

    // observer/watcher
    const watcher = new Watcher(vm, expOrFn, cb, options)
    if (options.immediate) {
      // 立即执行一次
      cb.call(vm, watcher.value)
    }

    return function unwatchFn () {
      watcher.teardown()
    }
  }
}
```

## events.js

### [fn] initEvents

为组件添加事件功能。`{% post_link vue2shared bind %}` updateListeners 未完成缺链接

``` javascript
function initEvents (vm: Component) {
  vm._events = Object.create(null)
  // 初始化父级的附加事件
  const listeners = vm.$options._parentListeners
  // 定义组件的绑定与解绑的函数
  const on = bind(vm.$on, vm)
  const off = bind(vm.$off, vm)

  // 更新监听函数，具体的添加与删除事件的机制参考上方链接
  vm._updateListeners = (listeners, oldListeners) => {
    updateListeners(listeners, oldListeners || {}, on, off)
  }
  // 如果存在附加事件则在初始化时进行绑定
  if (listeners) {
    vm._updateListeners(listeners)
  }
}
```

### [fn] eventsMixin

这个函数的作用是在 Vue 的原型链上定义了若干事件的方法。使得这些方法可以被实例继承。这些方法均返回组件的实例

#### $on

将同名事件添加到对应的数组中

``` javascript
Vue.prototype.$on = function (event: string, fn: Function): Component {
  const vm: Component = this
  ;(vm._events[event] || (vm._events[event] = [])).push(fn)
  return vm
}
```

#### $once

绑定的事件只执行一次，

``` javascript
Vue.prototype.$once = function (event: string, fn: Function): Component {
  const vm: Component = this
  function on () {
    // 解绑，
    // ？先解绑
    vm.$off(event, on)
    // 执行
    fn.apply(vm, arguments)
  }
  // 存 fn，是为了在从多个函数中解绑一个函数时作判断用
  on.fn = fn
  vm.$on(event, on)
  return vm
}
```

#### $off

解绑事件。

``` javascript
Vue.prototype.$off = function (event?: string, fn?: Function): Component {
  const vm: Component = this
  // 不传参数则解绑全部事件
  if (!arguments.length) {
    vm._events = Object.create(null)
    return vm
  }
  // 指定了事件（event）参数
  const cbs = vm._events[event]
  // 没有需要解绑的事件
  if (!cbs) {
    return vm
  }
  // 事件数组中只有一个函数
  if (arguments.length === 1) {
    vm._events[event] = null
    return vm
  }
  // 指定了对应函数（fn）参数
  // 则查找对应函数并删除
  let cb
  let i = cbs.length
  while (i--) {
    cb = cbs[i]
    if (cb === fn || cb.fn === fn) {
      cbs.splice(i, 1)
      break
    }
  }
  return vm
}
```

#### $emit

触发当前组件实例上的事件。

``` javascript
Vue.prototype.$emit = function (event: string): Component {
  const vm: Component = this
  let cbs = vm._events[event]
  // 如果有同名事件的存放的数组则执行
  if (cbs) {
    cbs = cbs.length > 1 ? toArray(cbs) : cbs
    const args = toArray(arguments, 1)
    for (let i = 0, l = cbs.length; i < l; i++) {
      cbs[i].apply(vm, args)
    }
  }
  return vm
}
```




## lifecycle.js

### [any] activeInstance

用于存储实例

### [fn] initLifecycle

初始化一些生命周期功能

``` javascript
function initLifecycle (vm: Component) {
  const options = vm.$options

  // 找到最近一个非抽象父
  let parent = options.parent
  if (parent && !options.abstract) {
    while (parent.$options.abstract && parent.$parent) {
      parent = parent.$parent
    }
    parent.$children.push(vm)
  }

  vm.$parent = parent
  vm.$root = parent ? parent.$root : vm

  vm.$children = []
  vm.$refs = {}

  vm._watcher = null
  vm._inactive = false
  vm._isMounted = false
  vm._isDestroyed = false
  vm._isBeingDestroyed = false
}
```

### [fn] lifecycleMixin

为 Vue 实例添加了几个方法

#### vm.\_mount

用于装载（载入）组件

``` javascript
Vue.prototype._mount = function (
  el?: Element | void,
  hydrating?: boolean
): Component {
  const vm: Component = this
  vm.$el = el
  if (!vm.$options.render) {
    vm.$options.render = emptyVNode
    if (process.env.NODE_ENV !== 'production') {
      /* istanbul ignore if */
      if (vm.$options.template) {
        warn(
          'You are using the runtime-only build of Vue where the template ' +
          'option is not available. Either pre-compile the templates into ' +
          'render functions, or use the compiler-included build.',
          vm
        )
      } else {
        // 既没有 template 也 没有 render
        warn(
          'Failed to mount component: template or render function not defined.',
          vm
        )
      }
    }
  }
  // 调用 beforeMount 生命周期函数
  callHook(vm, 'beforeMount')

  // /core/observer/Watcher[class]
  vm._watcher = new Watcher(vm, () => {

    // 变动执行函数，🔽🔽🔽 函数实现
    vm._update(vm._render(), hydrating)

  }, noop)
  hydrating = false
  // 根实例需自行调用 mounted 生命周期函数
  // 子组件在自己的钩子中调用了 mounted 函数
  if (vm.$root === vm) {
    vm._isMounted = true
    callHook(vm, 'mounted')
  }
  return vm
}
```

#### vm.\_update

用于更新组件 ？

``` javascript
Vue.prototype._update = function (vnode: VNode, hydrating?: boolean) {
  const vm: Component = this
  if (vm._isMounted) {
    // 如果加载完毕调用 beforeUpdate 生命周期
    callHook(vm, 'beforeUpdate')
  }
  // 存储更新前的信息
  const prevEl = vm.$el
  const prevActiveInstance = activeInstance
  activeInstance = vm
  const prevVnode = vm._vnode
  vm._vnode = vnode

  if (!prevVnode) {
    // Vue.prototype.__patch__ 在入口点已被注入
    // 基于后端如何渲染
    // ?
    vm.$el = vm.__patch__(vm.$el, vnode, hydrating)
  } else {
    vm.$el = vm.__patch__(prevVnode, vnode)
  }
  activeInstance = prevActiveInstance
  // 更新 __vue__ 接口 ？
  if (prevEl) {
    prevEl.__vue__ = null
  }
  if (vm.$el) {
    vm.$el.__vue__ = vm
  }
  // if parent is an HOC, update its $el as well ?
  if (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) {
    vm.$parent.$el = vm.$el
  }
  // 调用钩子函数
  if (vm._isMounted) {
    callHook(vm, 'updated')
  }
}
```

#### vm.\_updateFromParent

从父节点更新 ？

``` javascript
Vue.prototype._updateFromParent = function (
  propsData: ?Object,
  listeners: ?Object,
  parentVnode: VNode,
  renderChildren: ?VNodeChildren
) {
  const vm: Component = this
  const hasChildren = !!(vm.$options._renderChildren || renderChildren)
  vm.$options._parentVnode = parentVnode
  vm.$options._renderChildren = renderChildren
  // update props
  if (propsData && vm.$options.props) {
    observerState.shouldConvert = false
    if (process.env.NODE_ENV !== 'production') {
      observerState.isSettingProps = true
    }
    const propKeys = vm.$options._propKeys || []
    for (let i = 0; i < propKeys.length; i++) {
      const key = propKeys[i]
      vm[key] = validateProp(key, vm.$options.props, propsData, vm)
    }
    observerState.shouldConvert = true
    if (process.env.NODE_ENV !== 'production') {
      observerState.isSettingProps = false
    }
  }
  // 更新事件监听器
  if (listeners) {
    const oldListeners = vm.$options._parentListeners
    vm.$options._parentListeners = listeners
    vm._updateListeners(listeners, oldListeners)
  }
  // 如果有子节点 解析 slots 并强制更新
  if (hasChildren) {
    vm.$slots = resolveSlots(renderChildren)
    vm.$forceUpdate()
  }
}
```

#### vm.$forceUpdate

强制更新

``` javascript
Vue.prototype.$forceUpdate = function () {
  const vm: Component = this
  if (vm._watcher) {
    vm._watcher.update()
  }
}
```

#### vm.$destroy

``` javascript
Vue.prototype.$destroy = function () {
  const vm: Component = this

  // 正在销毁
  if (vm._isBeingDestroyed) {
    return
  }

  // 调用 beforeDestroy 钩子函数
  callHook(vm, 'beforeDestroy')
  vm._isBeingDestroyed = true
  // 从父级中删除
  const parent = vm.$parent
  if (parent && !parent._isBeingDestroyed && !vm.$options.abstract) {
    remove(parent.$children, vm)
  }
  // 拆卸 watchers
  if (vm._watcher) {
    vm._watcher.teardown()
  }
  let i = vm._watchers.length
  while (i--) {
    vm._watchers[i].teardown()
  }
  // 从 data ob 上删除接口
  // 冻结的对象可能没有观察者
  if (vm._data.__ob__) {
    vm._data.__ob__.vmCount--
  }

  vm._isDestroyed = true
  callHook(vm, 'destroyed')
  // 撤销实例上所有的监听器
  vm.$off()
  // 删除 __vue__ 接口
  if (vm.$el) {
    vm.$el.__vue__ = null
  }
}
```

### [fn] callHook

调用一个生命周期函数。

``` javascript
function callHook (vm: Component, hook: string) {
  const handlers = vm.$options[hook]
  if (handlers) {
    for (let i = 0, j = handlers.length; i < j; i++) {
      handlers[i].call(vm)
    }
  }
  // 触发一次事件 eg: 'hook:ready'
  vm.$emit('hook:' + hook)
}
```

## render.js

### [fn] initRender

``` javascript
function initRender (vm: Component) {
  vm.$vnode = null // the placeholder node in parent tree
  vm._vnode = null // the root of the child tree
  vm._staticTrees = null
  vm.$slots = resolveSlots(vm.$options._renderChildren)
  // bind the public createElement fn to this instance
  // so that we get proper render context inside it.
  vm.$createElement = bind(createElement, vm)
  if (vm.$options.el) {
    vm.$mount(vm.$options.el)
  }
}
```

### [fn] renderMixin

添加实例方法

#### vm.$nextTick

``` javascript
Vue.prototype.$nextTick = function (fn: Function) {
  // util/env.js
  nextTick(fn, this)
}
```

#### vm.\_render ？

``` javascript
Vue.prototype._render = function (): VNode {
  const vm: Component = this
  const {
    render,
    staticRenderFns,
    _parentVnode
  } = vm.$options

  if (staticRenderFns && !vm._staticTrees) {
    vm._staticTrees = []
  }
  // set parent vnode. this allows render functions to have access
  // to the data on the placeholder node.
  vm.$vnode = _parentVnode
  // render self
  let vnode
  try {
    vnode = render.call(vm._renderProxy, vm.$createElement)
  } catch (e) {
    if (process.env.NODE_ENV !== 'production') {
      warn(`Error when rendering ${formatComponentName(vm)}:`)
    }
    /* istanbul ignore else */
    if (config.errorHandler) {
      config.errorHandler.call(null, e, vm)
    } else {
      if (config._isServer) {
        throw e
      } else {
        setTimeout(() => { throw e }, 0)
      }
    }
    // return previous vnode to prevent render error causing blank component
    vnode = vm._vnode
  }
  // return empty vnode in case the render function errored out
  if (!(vnode instanceof VNode)) {
    if (process.env.NODE_ENV !== 'production' && Array.isArray(vnode)) {
      warn(
        'Multiple root nodes returned from render function. Render function ' +
        'should return a single root node.',
        vm
      )
    }
    vnode = emptyVNode()
  }
  // set parent
  vnode.parent = _parentVnode
  return vnode
}
```
#### vm.\_h/\_s/\_n/\_m/\_f/\_l/\_b/\_k ？

``` javascript
function renderMixin (Vue: Class<Component>) {




  // shorthands used in render functions
  Vue.prototype._h = createElement
  // toString for mustaches
  Vue.prototype._s = _toString
  // number conversion
  Vue.prototype._n = toNumber

  // render static tree by index
  Vue.prototype._m = function renderStatic (
    index: number,
    isInFor?: boolean
  ): VNode | VNodeChildren {
    let tree = this._staticTrees[index]
    // if has already-rendered static tree and not inside v-for,
    // we can reuse the same tree by indentity.
    if (tree && !isInFor) {
      return tree
    }
    // otherwise, render a fresh tree.
    tree = this._staticTrees[index] = this.$options.staticRenderFns[index].call(this._renderProxy)
    if (Array.isArray(tree)) {
      for (let i = 0; i < tree.length; i++) {
        tree[i].isStatic = true
        tree[i].key = `__static__${index}_${i}`
      }
    } else {
      tree.isStatic = true
      tree.key = `__static__${index}`
    }
    return tree
  }

  // filter resolution helper
  const identity = _ => _
  Vue.prototype._f = function resolveFilter (id) {
    return resolveAsset(this.$options, 'filters', id, true) || identity
  }

  // render v-for
  Vue.prototype._l = function renderList (
    val: any,
    render: () => VNode
  ): ?Array<VNode> {
    let ret: ?Array<VNode>, i, l, keys, key
    if (Array.isArray(val)) {
      ret = new Array(val.length)
      for (i = 0, l = val.length; i < l; i++) {
        ret[i] = render(val[i], i)
      }
    } else if (typeof val === 'number') {
      ret = new Array(val)
      for (i = 0; i < val; i++) {
        ret[i] = render(i + 1, i)
      }
    } else if (isObject(val)) {
      keys = Object.keys(val)
      ret = new Array(keys.length)
      for (i = 0, l = keys.length; i < l; i++) {
        key = keys[i]
        ret[i] = render(val[key], key, i)
      }
    }
    return ret
  }

  // apply v-bind object
  Vue.prototype._b = function bindProps (
    vnode: VNodeWithData,
    value: any,
    asProp?: boolean) {
    if (value) {
      if (!isObject(value)) {
        process.env.NODE_ENV !== 'production' && warn(
          'v-bind without argument expects an Object or Array value',
          this
        )
      } else {
        if (Array.isArray(value)) {
          value = toObject(value)
        }
        const data: any = vnode.data
        for (const key in value) {
          if (key === 'class' || key === 'style') {
            data[key] = value[key]
          } else {
            const hash = asProp || config.mustUseProp(key)
              ? data.domProps || (data.domProps = {})
              : data.attrs || (data.attrs = {})
            hash[key] = value[key]
          }
        }
      }
    }
  }

  // expose v-on keyCodes
  Vue.prototype._k = function getKeyCodes (key: string): any {
    return config.keyCodes[key]
  }
}
```

### [fn] resolveSlots ？

解析 slots

``` javascript
function resolveSlots (
  renderChildren: ?VNodeChildren
): { [key: string]: Array<VNode> } {
  const slots = {}
  if (!renderChildren) {
    return slots
  }
  const children = normalizeChildren(renderChildren) || []
  const defaultSlot = []
  let name, child
  for (let i = 0, l = children.length; i < l; i++) {
    child = children[i]
    if (child.data && (name = child.data.slot)) {
      delete child.data.slot
      const slot = (slots[name] || (slots[name] = []))
      if (child.tag === 'template') {
        slot.push.apply(slot, child.children)
      } else {
        slot.push(child)
      }
    } else {
      defaultSlot.push(child)
    }
  }
  // ignore single whitespace
  if (defaultSlot.length && !(
    defaultSlot.length === 1 &&
    defaultSlot[0].text === ' '
  )) {
    slots.default = defaultSlot
  }
  return slots
}
```

## proxy.js ？

### [fn] initProxy

``` javascript
let hasProxy, proxyHandlers, initProxy

if (process.env.NODE_ENV !== 'production') {
  const allowedGlobals = makeMap(
    'Infinity,undefined,NaN,isFinite,isNaN,' +
    'parseFloat,parseInt,decodeURI,decodeURIComponent,encodeURI,encodeURIComponent,' +
    'Math,Number,Date,Array,Object,Boolean,String,RegExp,Map,Set,JSON,Intl,' +
    'require' // for Webpack/Browserify
  )

  hasProxy =
    typeof Proxy !== 'undefined' &&
    Proxy.toString().match(/native code/)

  proxyHandlers = {
    has (target, key) {
      const has = key in target
      const isAllowed = allowedGlobals(key) || key.charAt(0) === '_'
      if (!has && !isAllowed) {
        warn(
          `Property or method "${key}" is not defined on the instance but ` +
          `referenced during render. Make sure to declare reactive data ` +
          `properties in the data option.`,
          target
        )
      }
      return has || !isAllowed
    }
  }

  initProxy = function initProxy (vm) {
    if (hasProxy) {
      vm._renderProxy = new Proxy(vm, proxyHandlers)
    } else {
      vm._renderProxy = vm
    }
  }
}

export { initProxy }
```
