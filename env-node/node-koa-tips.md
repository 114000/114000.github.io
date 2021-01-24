---
title: Koa tips
date: 2018-06-26
tag:
- node
- koa
---

1. 使用 koa-compose 组合中间件时，同步和异步的不能混合成一组。其中一个会抛弃。（待验证是不是慢的会被抛弃）

2. ctx.throw(500) 与 ctx.status = 500 的区别，前者不可再设置body 的返回值，后者可以。

3. 捕获异常可以在顶层设计中间件
``` javascript
const handler = async (ctx, next) => {
  try { await next() }
  catch (err) {
    ctx.response.status = err.statusCode || err.status || 500
    ctx.response.body = { message: err.message }
  }
}

const main = ctx => ctx.throw(500)

app.use(handler)
app.use(main)
```

4. Koa 处理cookies

``` javascript
const main = ctx => {
  const n = Number(ctx.cookies.get('view') || 0) + 1
  ctx.cookies.set('view', n)
  ctx.response.body = n + 'views'
}
```

5. koa-body 处理post数据 `app.use(koaBody())`

<http://www.ruanyifeng.com/blog/2017/08/koa.html> 最后一个文件上传示例