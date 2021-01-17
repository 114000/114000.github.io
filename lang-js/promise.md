---
title: 基础 - Promise
date: 2016-04-20
categories:
- [编程语言, JavaScript]

thumbnailImage: https://hd.unsplash.com/photo-1428189923803-e9801d464d76
coverImage: https://hd.unsplash.com/photo-1428189923803-e9801d464d76
---

这篇介绍 es6 的 Promise，由于现在大部分的浏览器已经支持 Promise 的写法（除了 ie），所以没有必要单独去搭建[运行环境](http://114000.github.io/2016/04/10/es2015Class.html#editing-code)。

<!-- more -->
之前的两篇：

1. [ES2015 系列之一 - Module](http://114000.github.io/2016/01/27/es2015Module)
2. [ES2015 系列之二 - Class](http://114000.github.io/2016/04/10/es2015Class)

<!-- toc -->

---

> 我今天想找阿花，李雷，小明一块打麻将。

我们就考虑麻将必须是4个人一起打，而且人总是要一个一个的约，他们有一个人不同意今天的麻将就打不成啦! 我们用代码实现以下：

``` javascript

function gameOver () {
  console.log('game over')
}

function iWannaPlay () {
  invitAHua(function (aHuaCanPlay) { // 邀请阿花
    if (aHuaCanPlay) { // 阿花同意

      invitLiLei(function (liLeiCanPlay) { // 邀请李雷
        if (liLeiCanPlay) { // 李雷同意

          invitXiaoMing(function (xiaoMingCanPlay) { // 邀请小明
            if (xiaoMingCanPlay) { // 小明同意

              wePlayTogether()
            } else { // 小明不同意
              gameOver()
            }
          })
        } else { // 李雷不同意
          gameOver()
        }
      })
    } else { // 阿花不同意
      gameOver()
    }
  })
}

iWannaPlay()


```

## 引

想象以下我们要是踢一场正规的足球赛的话，这代码简直就是不能看了，但如果使用 Promise 就可以大大改善这一现象。

<!-- more -->
### 先介绍一下如何使用 Promise

在实例化 `Promise` 类的时候，我们需要传一个函数（比如是：`handle`）作为构造函数的参数。这个函数（`handle`）会接收两个**函数**，
一个是 `resolve`，一个是 `reject`。像这样：

``` javascript

function handle (resolve, reject) {
  ...
}

const promise = new Promise(handle)

```

`resolve`，`reject` 两个函数我们可以认为一个是**接受**，另一个是**拒绝**，也就是说如果我们执行了 `resolve` 函数，就代表我们认可了某种条件，
反之如果我们执行了 `reject` 就代表我们拒绝了某种条件：

``` javascript

function handle (resolve, reject) {
  invitAHua(function(aHuaCanPlay) {
    aHuaCanPlay ? resolve() : reject()
  })
}

const promise = new Promise(handle)

```

## 实例方法

接下来我们就可以在实例 `promise` 使用 `then` 和 `catch` 这两个实例方法来处理了，`then` 是 `resolve()` 对应调用的函数，`catch` 是 `reject()` 对应调用的函数。他们都接受一个函数作为参数，它就是你处理成功（接受）或失败（拒绝）的函数：

``` javascript

function handle (resolve, reject) {
  invitAHua(function(aHuaCanPlay) {
    aHuaCanPlay ? resolve() : reject()
  })
}

const promise = new Promise(handle)

promise.then(invitLiLei)
promise.catch(gameOver)

```

所以我们只需要记住 `resolve` 方法与 `then` 对应，`reject` 方法与 `catch` 方法对应就可以了，

`then` 和 `catch` 执行结束之后都会返回一个新的 `Promise` 实例，所以我们可以链式调用：

``` javascript

anotherPromise.then().then().catch().then().catch()

```

有一点需要**注意**：如果你在`then`，或 `catch` 接收的函数中返回的不是一个 `Promise`，则他们会用之后介绍的静态方法
[`Promise.resolve`](#promise-resolve) 将其包装成 `Promise` 实例。

我们最后看一下这段代码用 Promise 如何实现：

``` javascript

function gameOver () {
  console.log('game over')
}

function iWantToPlay () {
  return new Promise(function (resolve, reject) {
    invitAHua(function (aHuaCanPlay) {
      aHuaCanPlay ? resolve() : reject()
    })
  })
}

iWantToPlay()
.then(function () {
  return new Promise(function (resolve, reject) {
    invitLiLei(function (liLeiCanPlay) {
      liLeiCanPlay ? resolve() : reject()
    })
  })
})
.then(function () {
  return new Promise(function (resolve, reject) {
    invitXiaoMing(function (xiaoMingCanPlay) {
      xiaoMingCanPlay ? resolve() : reject()
    })
  })
})
.then(wePlayTogether)
.catch(gameOver)

```

再简化一下：

``` javascript

function gameOver () {
  console.log('game over')
}

function invit (invitWho) {
  return new Promise(function (resolve, reject) {
    invitWho(function (canPlay) {
      canPlay ? resolve() : reject()
    })
  })
}

function iWantToPlay () {
  return invit(invitAHua) // 邀请阿花
}

iWantToPlay()
.then(function () {
  return invit(invitLiLei) // 阿花之后邀请李雷
})
.then(function () {
  return invit(invitXiaoMing) // 李雷之后邀请小明
})
.then(wePlayTogether)
.catch(gameOver) // 如果有一个人没接受邀请，我们就玩不成了

```

---

## 静态方法

介绍 `Promise` 类的四个静态方法 `all`、`race`、`resolve` 和 `reject`

### Promise.all

``` javascript
Promise.all([
  request.learn({ act: 'get_config' }),
  request.work({ act: 'get_config' }),
  request.play({ act: 'get_config' })
])
.then(function (results) {
  // results => [learnResult, workResult, playResult]
  console.log('all finished') // 全部 resolve 时才执行 then

})
.catch(function (error) {
  console.log('one unfinished') // 有一个 reject 时就执行 catch
})

```

`Promise.all` 返回的实例的 `then` 方法会在所有的 promise 都 resolve 之后才会执行，它的参数是则是将所有的结果合并成的一个数组。

**需要注意** 的一点是：所有的 promise 不是依次执行的，而是同时执行的。


### Promise.race

``` javascript
Promise.race([
  request.learn({ act: 'get_config' }),
  request.work({ act: 'get_config' }),
  request.play({ act: 'get_config' })
])
.then(function (result) {
  console.log('one finished') // 返回最快的 resolve 的一个
})
.catch(function (error) {
  console.log('one unfinished') // 有一个 reject 时就执行 catch
})

```
`Promise.race` 用法与 [`Promise.all`](#promise-all) 一致，不同的是只要 promise 的数组中有一个达成了 resolve 就执行 `then` 函数，
而 `catch` 则与 [`Promise.all`](#promise-all) 的 `catch` 触发机制相同。

### Promise.resolve

返回一个被 `resolve` 的 promise。

``` javascript

class Promise {
  // 实例方法
  ...
  // 静态方法
  static resolve (sth) {
    return new Promise(function (resolve, reject) {
      resolve(sth)
    })
  }

}

```

``` javascript

// 使用

Promise.resolve('it\'s lovely')
.then(function (res) {
  console.log(res)
})

// string: 'it's lovely'

```

### Promise.reject

返回一个被 `reject` 的 promise。

``` javascript

class Promise {
  // 实例方法
  ...
  // 静态方法
  static reject (sth) {
    return new Promise(function (resolve, reject) {
      reject(sth)
    })
  }

}

```

``` javascript

// 使用

Promise.reject('it\'s ugly')
.catch(function (res) {
  console.log(res)
})

// string: 'it's ugly'

```

以下代码是用类的形式描述了一下 Promise 这个类：

``` javascript

class Promise {

  constructor (handle) {
    handle(this._resolve, this._reject)

  }

  // 实例方法
  then () { }
  catch () { }

  _resolve () { }
  _reject () { }


  // 静态方法
  static all () { }
  static race () { }
  static resolve () { }
  static reject () { }

}
```

## 相关连接

- [《javascript Promise 迷你书》](http://liubin.org/promises-book/)
- [阮一峰《ECMAScript 6 入门》](http://es6.ruanyifeng.com/#docs/promise)

（完）
