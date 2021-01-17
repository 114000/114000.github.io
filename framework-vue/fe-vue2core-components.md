---
layout: post
title:  vue2 源码 - core/component
date:   2016-08-31
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
目前只有 keep-alive 指令的实现

<!-- more -->

> **注意事项及目录结构请参考** `{% post_link fe-vue2toc Vue目录 %}`

<!-- toc -->

## index.js

导出组件

## keep-alive.js

[keep-alive](http://vuejs.org/guide/components.html#keep-alive) 组件的实现

> 如果你想要开关组件的活性，那么你可以添加一个 keep-alive 指令参数来保存组件的状态或者避免组件的重新渲染。- rc.vue.org

``` javascript
<component :is="currentView" keep-alive>
  <!-- inactive components will be cached! -->
</component>
```

``` javascript
export default {
  name: 'keep-alive',
  abstract: true, // 抽象组件
  created () {
    this.cache = Object.create(null)
  },
  render () {
    // getFirstComponentChild => core/vdom/helpers
    // 获取第一个有 componentOptions 子组件
    const vnode = getFirstComponentChild(this.$slots.default)
    if (vnode && vnode.componentOptions) {
      const opts = vnode.componentOptions
      // 缓存用键名
      const key = vnode.key == null
        // 相同的构造函数可能会被注册为不同的局部组件
        // 所以只有 cid 是不够得 (#3269)
        ? opts.Ctor.cid + '::' + opts.tag
        : vnode.key
      if (this.cache[key]) {
        vnode.child = this.cache[key].child
      } else {
        this.cache[key] = vnode
      }
      // ？在哪识别
      vnode.data.keepAlive = true
    }
    return vnode
  },
  destroyed () {
    // 销毁之后销毁子组件
    for (const key in this.cache) {
      const vnode = this.cache[key]
      callHook(vnode.child, 'deactivated')
      vnode.child.$destroy()
    }
  }
}
```


---
