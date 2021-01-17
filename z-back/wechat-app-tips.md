---
title: 【归档】微信小程序 tips
date: 2018-06-08
tag:
- 归档
---


::: danger
2019-12-16: 留档 
最近不写小程序了，先归档吧
:::


> 记录一些小程序开发时可能的问题

1. 小程序 wx.request 需要接口支持HTTPS，开发时可以选择不校验域名 右上角`详情`按钮 - `不校验合法域名、web-view（业务域名）、TLS 版本以及 HTTPS 证书` 选项，但是不支持真机调试
- [文档说明](https://developers.weixin.qq.com/miniprogram/dev/api/api-network.html)

2. 修改 data 中值时要使用 `this.setData({ key: value })`，否则不会触发页面的渲染

3. wxml 不能给绑定事件传参（如vue 中的 `@click="tap(12)"`），可以通过设置标签的 data-xxx-yyy 属性，再绑定从事件对象中获取 event.currentTarget.dataset.xxxYyy，这里推荐使用 currentTarget 而不是 target，由于事件机制，并不能保证点击的 target 是绑定了 data-xxx-yyy 的元素(一般是点击到的子元素)，因此可能会无法获取数据

4. TabBar, 以及 Page 的backgroundColor 只能设置为16进制颜色值（#ffffff），真机调试不识别rgb, rgba, 颜色名，会默认显示黑色

5. Text 标签默认会有高度，并不贴合文字

6. vscode 启用 emmet 

    ``` json
    "emmet.triggerExpansionOnTab": true,
    "emmet.includeLanguages": {
      "wxml": "html",
      "wxss": "css"
    },
    ```

7. 让设计出 750 px iphone 设计稿， 然后里面用 rpx 做单位，编译时自动转换

8. 自定义组件的 properties 的值需要设置为 object, 并且不能用 id 作为 key,外部无法赋值

    ```js
    Component({
      properties: {
        foo: { type: String, value: '' }
        // 不能用 id 做 [key] 外部无法赋值
      }
    })
    ```

9. navgator的传参规则 `url="/pages/*?paramA=foo&paramsB=bar"` navigator 传递的路径参数在对应页面的 onLoad 函数的 options 参数中

10. 获取App实例 `const root = getApp()`

11. navigator 组件会添加默认的点击高亮，可以设置标签的 `hover-class="none"` 来取消

12. 容器使用圆角时，内部如果有图片，则需要使用 `overflow: hidden;` 样式

---

