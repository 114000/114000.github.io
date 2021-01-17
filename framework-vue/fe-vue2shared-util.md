---
layout: post
title:  vue2 源码 - shared
date:   2016-08-26
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
先从简单的地方开始吧，shared是公用的目录

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

## shared/util.js

这个目录就只有 `util.js` 一个文件。它暴露了一些工具函数给其他部分用。我们来看一下

### \_toString

``` javascript
function _toString (val: any): string {
  return val == null
    ? ''
    : typeof val === 'object'
      ? JSON.stringify(val, null, 2)
      : String(val)
}
```

接收任何类型的参数并转化为字符串返回。null 返回空字符串，对象则返回缩进为2的对象型的字符串。

### toNumber

``` javascript
function toNumber (val: string): number | string {
  const n = parseFloat(val, 10)
  return (n || n === 0) ? n : val
}
```

将字符串转化为数字并返回，如果转化后的逻辑值为假则返回原字符串。

### makeMap

``` javascript
function makeMap (
  str: string,
  expectsLowerCase?: boolean
): (key: string) => true | void {
  // 创建一个继承自 null 的 map
  const map = Object.create(null)
  const list: Array<string> = str.split(',')
  for (let i = 0; i < list.length; i++) {
    map[list[i]] = true
  }
  return expectsLowerCase
    ? val => map[val.toLowerCase()]
    : val => map[val]
}

```
将以逗号分隔的字符串转化成 map。并返回一个函数，这个函数接收一个字符串，判断这个字符串是否在这个 map 中。具体可以参考下面这个函数的用法

### isBuiltInTag

``` javascript
const isBuiltInTag = makeMap('slot,component', true)
```

查询是否为嵌套标签（`<slot></slot>`，`<component></component>`）:

``` javascript
isBuiltInTag('SLOT') // => true
isBuiltInTag('a') // => false
```

### remove

从数组（第一个参数）中删除一项（第二个参数）。

``` javascript
function remove (arr: Array<any>, item: any): Array<any> | void {
  if (arr.length) {
    const index = arr.indexOf(item)
    if (index > -1) {
      return arr.splice(index, 1)
    }
  }
}
```



### hasOwnProperty、hasOwn

``` javascript
const hasOwnProperty = Object.prototype.hasOwnProperty
function hasOwn (obj: Object, key: string): boolean {
  return hasOwnProperty.call(obj, key)
}
```

查看一个对象（第一个参数）是否有某种属性（第二个参数）

### isPrimitive

``` javascript
function isPrimitive (value: any): boolean {
  return typeof value === 'string' || typeof value === 'number'
}
```

判断是否为原始类型

### cached

``` javascript
function cached (fn: Function): Function {
  const cache = Object.create(null)
  return function cachedFn (str: string): any {
    const hit = cache[str]
    return hit || (cache[str] = fn(str))
  }
}
```

使用闭包在内存中缓存一个纯函数，重复使用时速度更快。（待解）

### camelize

``` javascript
const camelizeRE = /-(\w)/g
const camelize = cached((str: string): string => {
  return str.replace(camelizeRE, (_, c) => c ? c.toUpperCase() : '')
})
```

将连字符形式的字符串转化为驼峰命名形式的字符串

### capitalize

``` javascript
const capitalize = cached((str: string): string => {
  return str.charAt(0).toUpperCase() + str.slice(1)
})
```

返回一个首字母大写的字符串


### hyphenate

``` javascript
const hyphenateRE = /([^-])([A-Z])/g
const hyphenate = cached((str: string): string => {
  return str
    .replace(hyphenateRE, '$1-$2')
    .replace(hyphenateRE, '$1-$2')
    .toLowerCase()
})
```

将以驼峰形式命名的字符串转化为连字符形式

### bind

``` javascript
function bind (fn: Function, ctx: Object): Function {
  function boundFn (a) {
    const l: number = arguments.length
    return l
      ? l > 1
        ? fn.apply(ctx, arguments)
        : fn.call(ctx, a)
      : fn.call(ctx)
  }
  // record original fn length
  boundFn._length = fn.length
  return boundFn
}
```

简单的绑定，比原生的要快（待解）

### toArray

``` javascript
function toArray (list: any, start?: number): Array<any> {
  start = start || 0
  let i = list.length - start
  const ret: Array<any> = new Array(i)
  while (i--) {
    ret[i] = list[i + start]
  }
  return ret
}
```

将类似数组对象转化为真实的数组，可以指定转化的起始位置

### extend

``` javascript
function extend (to: Object, _from: ?Object): Object {
  for (const key in _from) {
    to[key] = _from[key]
  }
  return to
}
```

将某个对象上属性扩展到到目标对象上


### isObject

``` javascript
/**
 * Quick object check - this is primarily used to tell
 * Objects from primitive values when we know the value
 * is a JSON-compliant type.
 */
function isObject (obj: any): boolean {
  return obj !== null && typeof obj === 'object'
}
```

用于快速检查类型是否为 'object' （待解）

### isPlainObject

``` javascript
const toString = Object.prototype.toString
const OBJECT_STRING = '[object Object]'
function isPlainObject (obj: any): boolean {
  return toString.call(obj) === OBJECT_STRING
}
```

检查是否是纯 js 对象，即含有0个及以上键值对的对象，`toString.call(null) => [object, Null]`


### toObject

``` javascript
function toObject (arr: Array<any>): Object {
  const res = arr[0] || {}
  for (let i = 1; i < arr.length; i++) {
    if (arr[i]) {
      extend(res, arr[i])
    }
  }
  return res
}
```

将数组中所有对象合并到单独的一个对象上

### noop

``` javascript
function noop () {}
```

不执行任何操作

### no

``` javascript
export const no = () => false
```

总返回 false

### genStaticKeys

``` javascript
function genStaticKeys (modules: Array<ModuleOptions>): string {
  return modules.reduce((keys, m) => {
    return keys.concat(m.staticKeys || [])
  }, []).join(',')
}
```

从编译器模块中生成一个静态的字符串密钥（待解）
