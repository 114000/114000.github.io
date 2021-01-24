---
title: js 编程实践
---


## JS 编程实践-用 Promise 或 async/await 代替回调函数

避免陷入回调地狱

#### using promise

```js
return functionA()
.then(functionB)
.then(functionC)
.then(functionD)
.catch((err) => logger.error(err))
.then(alwaysExecuteThisFunction)
```

#### using async/await 

``` js
async function executeAsyncTask () {
  try {
    const valueA = await functionA();
    const valueB = await functionB(valueA);
    const valueC = await functionC(valueB);
    return await functionD(valueC);
  }
  catch (err) {
    logger.error(err);
  } finally {
    await alwaysExecuteThisFunction();
  }
}
```

#### convert callback to promise

1. node 环境可以快速转换

``` js
const fs = require('fs')
const util = require('util')

const readFilePromise = util.promisify(fs.readFile)
```

2. 非node环境

```js
const growTreesPromise = (...args) => {
  return new Promise((resolve, reject) => {
    growTrees(...args, (error, location, size) => {
      if (err) return reject(err)
      // resolve 不支持多参数 
      // Using an array object
      resolve([location, size])

      // Using an object
      resolve({location, size})
    })
  })
}
```

### async / await 实现异步循环

``` js
asyncFunctions.reduce(async (result, current) => {

  const res = await current() 

  // res => result

  return result

}, result)
```

---

待整理

- <https://github.com/goldbergyoni/nodebestpractices/blob/master/README.chinese.md>
- [JavaScript 编程技巧](https://dev.to/hellomeghna/tips-to-write-better-conditionals-in-javascript-2189)