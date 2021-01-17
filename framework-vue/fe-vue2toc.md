---
layout: post
title:  vue2 源码 - 目录
date:   2016-08-31
categories: 前端
tag:
- Vue
- Javascript

thumbnailImage: http://cn.vuejs.org/images/logo.png
---
闲下来了学习一下源码

<!-- more -->

**注意**：这里只是将源码拆分成细碎部分进行学习，一些细节不一定能很好的展示出来（例如变量的作用域），
建议对照源码。版本：2.0.0-rc3，`npm i vue@next`。

由于代码比较多，大家可以根据下面的目录结构在其他文章中找到对应的代码。

- core/
  * {% post_link fe-vue2core-util util/ %}
  * {% post_link fe-vue2core-globalApi global-api/ %}
  * {% post_link fe-vue2core-instance instance/ %}
  * {% post_link fe-vue2core-components components/ %}
  * {% post_link fe-vue2core-observer observer/ %}
  * {% post_link fe-vue2core-vdom vdom/ %}
- {% post_link fe-vue2shared-util shared/util.js %}
- {% post_link fe-vue2sfc-parser sfc/parser.js %}

## 目录结构

``` diff
+ compiler/
+   |- codegen/
    |   |- events.js
    |   |- index.js
+   |- directives/
    |   |- bind.js
    |   |- index.js
+   |- parser/
    |   |- entity-decoder.js
    |   |- filter-parser.js
    |   |- html-parser.js
    |   |- text-parser.js
    |   |- index.js
    |- error-detector.js
    |- helpers.js
    |- optimizer.js
    |- optimizer.js
+ core/
+   |- components/
    |   |- keep-alive.js                  // 指令 keep-alive 的实现
    |   |- index.js                       // 导出
+   |- global-api/
    |   |- assets.js                      // Vue.component/directive/filter
    |   |- extend.js                      // Vue.extend
    |   |- mixin.js                       // Vue.mixin
    |   |- use.js                         // Vue.use
    |   |- index.js                       // 初始化全局 api
+   |- instance/
    |   |- events.js                      // $on $off $once $emit
    |   |- init.js                        // Vue.prototype._init 初始化
    |   |- lifecycle.js                   // 实现生命周期
    |   |- proxy.js
    |   |- render.js                      // render 选项
    |   |- state.js                       // props/data/computed/methods/watch
    |   |- index.js                       // 导出 Vue 将各文件实例方法合并
+   |- observer/
    |   |- array.js                       // 实现一个能通知变化的新的 Array
    |   |- dep.js                         // Dep 类, 监视变动的依赖项
    |   |- watcher.js                     // Watcher 类
    |   |- scheduler.js                   // Observer 类
    |   |- index.js
+   |- util/
    |   |- debug.js                       // warn formatComponentName 两个调试函数
    |   |- env.js                         // 检测环境，实现兼容的 nextTick 和 _Set
    |   |- lang.js                        // 作用于变量的工具函数
    |   |- options.js                     // 对配置项进行操作
    |   |- props.js                       // 验证组件的属性
    |   |- index.js                       // 导出
+   |- vdom/
+   |   |- modules/
    |   |   |- directives.js
    |   |   |- ref.js
    |   |   |- index.js
    |   |- create-component.js
    |   |- create-element.js
    |   |- helpers.js
    |   |- patch.js
    |   |- vnode.js
    |- index.js
+ entries/
    |- web-compiler.js
    |- web-runtime-with-compiler.js
    |- web-runtime.js
    |- web-server-renderer.js
+ server/
    |- create-bundle-renderer.js
    |- create-renderer.js
    |- render-stream.js
    |- render.js
    |- run-in-vm.js
    |- write.js
+ sfc/
    |- parser.js                          // 解析 .vue 文件
+ shared/
    |- util.js                            // 共用的一些工具函数
+ platforms/
+   |- web/
+   |   |- compiler/
+   |   |   |- directives/
    |   |   |   |- html.js
    |   |   |   |- model.js
    |   |   |   |- text.js
    |   |   |   |- index.js
+   |   |   |- modules/
    |   |   |   |- class.js
    |   |   |   |- style.js
    |   |   |   |- index.js
    |   |   |- index.js
+   |   |- runtime/
+   |   |   |- directives/
    |   |   |   |- model.js
    |   |   |   |- show.js
    |   |   |   |- index.js
+   |   |   |- modules/
    |   |   |   |- attrs.js
    |   |   |   |- class.js
    |   |   |   |- dom-props.js
    |   |   |   |- events.js
    |   |   |   |- style.js
    |   |   |   |- transition.js
    |   |   |   |- index.js
+   |   |   |- components/
    |   |   |   |- transition-group.js
    |   |   |   |- transition.js
    |   |   |   |- index.js
    |   |   |- class-util.js
    |   |   |- node-ops.js
    |   |   |- path.js
    |   |   |- transition-util.js
+   |   |- server/
+   |   |   |- directives/
    |   |   |   |- show.js
    |   |   |   |- index.js
+   |   |   |- modules/
    |   |   |   |- attrs.js
    |   |   |   |- class.js
    |   |   |   |- dom-props.js
    |   |   |   |- style.js
    |   |   |   |- index.js
+   |   |- util/
    |   |   |- attrs.js
    |   |   |- class.js
    |   |   |- element.js
    |   |   |- index.js
```
---

## 总结
项目整体使用了 [flow](https://flowtype.org/) 来做类型检查。是不同于 Typescript 方案的另一种大型项目构建的出路。其实还有很多地方没有理解，但随着源码学习的深入，这些问题也将渐渐解开，文章也会持续更新。一起努力吧！欢迎留言批评指教。
