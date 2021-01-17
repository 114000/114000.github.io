---
layout: post
title:  vue2 源码 - core/global-api
date:   2016-08-27
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
/core/global-api 中的代码比较好理解，主要在 Vue 上添加一些公用方法。经过梳理我们大概就知道了。Vue的外围是什么样的。

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

<!-- toc -->

### assets.js - [fn] initAssetRegisters

将 config 中的配置（'component', 'directive', 'filter'）方法注册到 Vue 上

``` javascript
function initAssetRegisters (Vue: GlobalAPI) {
  // config._assetTypes 数组中有
  // 'component', 'directive', 'filter'
  // 将他们注册为 Vue 的全局函数
  config._assetTypes.forEach(type => {
    Vue[type] = function (
      id: string,
      definition: Function | Object
    ): Function | Object | void {
      if (!definition) {
        return this.options[type + 's'][id]
      } else {
        // 判断组件名是否是保留字
        if (process.env.NODE_ENV !== 'production') {
          if (type === 'component' && config.isReservedTag(id)) {
            warn(
              'Do not use built-in or reserved HTML elements as component ' +
              'id: ' + id
            )
          }
        }
        // 组件的定义（definition）是纯 js 对象 => 使用 extend 注册为全局组件
        if (type === 'component' && isPlainObject(definition)) {
          definition.name = definition.name || id
          definition = Vue.extend(definition)
        }
        // 指令的定义（definition）是函数 => 初始化绑定与更新
        if (type === 'directive' && typeof definition === 'function') {
          definition = { bind: definition, update: definition }
        }
        this.options[type + 's'][id] = definition
        return definition
      }
    }
  })
}
```

### extend.js - [fn] initExtend

initExtend 为 Vue 添加一个 extend 函数，注册全局组件。使注册的组件继承自 Vue

``` javascript
function initExtend (Vue: GlobalAPI) {
  // 任何实例构造函数都有唯一的 cid，
  // 这使得我们可以针对原型继承和缓存功能创建可嵌套的“子构造函数”
  Vue.cid = 0
  let cid = 1

  Vue.extend = function (extendOptions: Object): Function {
    extendOptions = extendOptions || {}
    const Super = this
    const isFirstExtend = Super.cid === 0
    if (isFirstExtend && extendOptions._Ctor) {
      return extendOptions._Ctor
    }
    let name = extendOptions.name || Super.options.name
    // 检测组件名是否合法
    if (process.env.NODE_ENV !== 'production') {
      if (!/^[a-zA-Z][\w-]*$/.test(name)) {
        warn(
          'Invalid component name: "' + name + '". Component names ' +
          'can only contain alphanumeric characaters and the hyphen.'
        )
        name = null
      }
    }
    // 创建 VueComponent 使其继承自 Vue
    const Sub = function VueComponent (options) {
      this._init(options)
    }
    Sub.prototype = Object.create(Super.prototype)
    Sub.prototype.constructor = Sub
    Sub.cid = cid++ // 生成唯一的 cid
    Sub.options = mergeOptions(
      Super.options,
      extendOptions // 合并配置
    )
    // 可以使用 super 访问 Vue
    Sub['super'] = Super
    // 允许嵌套扩展
    Sub.extend = Super.extend
    // 创建资源注册机制，使子类也可以拥有私有资源（asset）
    // 'components', 'directives', 'filters'
    config._assetTypes.forEach(function (type) {
      Sub[type] = Super[type]
    })
    // 启用递归查找: 可以通过组件名访问自身
    if (name) {
      Sub.options.components[name] = Sub
    }
    // 在扩展时保留 Vue 配置的引用
    // 在之后的实例化中可以用来检测 Vue 的配置是否发生改变（update）。
    Sub.superOptions = Super.options
    Sub.extendOptions = extendOptions
    // 缓存构造函数
    if (isFirstExtend) {
      extendOptions._Ctor = Sub
    }
    return Sub
  }
}
```

### mixin.js - [fn] initMixin

initMixin 为 Vue 添加一个 mixin 函数，mixin 函数将配置合并到 Vue.options 上。既添加全局混合。

``` javascript
function initMixin (Vue: GlobalAPI) {
  Vue.mixin = function (mixin: Object) {
    Vue.options = mergeOptions(Vue.options, mixin)
  }
}
```

### use.js - [fn] initUse

initUse 为 Vue 添加一个 use 函数，use 函数可以用来添加 Vue 兼容的插件，如 Vuex, VueRouter, VueGesture 等等。
``` javascript
function initUse (Vue: GlobalAPI) {
  Vue.use = function (plugin: Function | Object) {
    // 避免重复注册
    if (plugin.installed) {
      return
    }
    // 将第一个参数替换为 Vue，然后下面将参数数组传递给相应的插件，完成相应的安装
    const args = toArray(arguments, 1)
    args.unshift(this)
    if (typeof plugin.install === 'function') {
      plugin.install.apply(plugin, args)
    } else {
      plugin.apply(null, args)
    }
    plugin.installed = true
    return this
  }
}
```

### index.js - [fn] initGlobalAPI

``` javascript
function initGlobalAPI (Vue: GlobalAPI) {
  // config
  const configDef = {}
  configDef.get = () => config
  if (process.env.NODE_ENV !== 'production') {
    configDef.set = () => {
      util.warn(
        'Do not replace the Vue.config object, set individual fields instead.'
      )
    }
  }
  // Vue.config.get => config /core/config.js
  Object.defineProperty(Vue, 'config', configDef)
  Vue.util = util // 暴露 util /core/util
  Vue.set = set // 设置对象属性函数 /observer/index
  Vue.delete = del // 删除对象属性函数 /observer/index
  Vue.nextTick = util.nextTick // 异步执行一组函数 /core/util/env.js

  // 创建配置对象，用于存储创建的 'component', 'directive', 'filter' 的 id
  Vue.options = Object.create(null)
  config._assetTypes.forEach(type => {
    Vue.options[type + 's'] = Object.create(null)
  })
  // 创建 Vue 自带组件
  util.extend(Vue.options.components, builtInComponents)

  initUse(Vue) // 初始化 Vue.use 方法
  initMixin(Vue) // 初始化 Vue.mixin 方法
  initExtend(Vue) // 初始化 Vue.extend 方法
  initAssetRegisters(Vue) // 初始化 Vue.component Vue.directive Vue.filter
}
```

---
