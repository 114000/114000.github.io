---
title: node 笔记
date: 2018-06-26
tag:
- node
---

常用 npm

- [request](https://github.com/request/request)
- [nodemon]() 
- [express]()
- [morgan]() 记录访问日志
- [ejs]() 视图引擎
- [body-parser] 把表单中提交的内容放到body 对象中

node API

EventEmitter

``` js
const EventEmitter = require('event')
const emitter = new EventEmitter()

emitter.on([eventName],  [callback])
emitter.once([eventName],  [callback])

emitter.emit([eventName], callbackArguments)
```

Fs

``` javascript
const fs = require('fs')

// 目录/文件信息
fs.stat([dir], [callback<error, stats>])
  stats.isFile<bool>()
  stats.isDirectory<bool>()

// 创建目录
fs.mkdir([dirName], [callback<error>])
fs.mkdirSync([dirName])

// 写入文件(创建或覆盖)
fs.writeFile([dirName], [fileContent], [callback<error>])
// 写入文件(创建或追加)
fs.appendFile([dirName], [appendContent], [callback<error>])

// 读取文件 
fs.readFile([dirName], [callback<error, bufferData>])  //可用 toString 方法转化 bufferData
fs.readFile([dirName], [type], [callback<error. typeData>]) // type: 'utf8'

// 读取目录信息
fs.readdir([dir], [callback<error, files>]) //files: [ 'hello.log', 'subLogs' ]

// 修改目录/文件名
fs.rename([oldDir], [newDir], [callback<error>])

// 删除空目录
fs.rmdir([dir], [callback<error>])

// 删除文件
fs.unlink([dirName], [callback<error>])

// eg: 递归删除
function forceRemove (dir) {
  const sub = fs.readdirSync(dir)
  .map(d => dir + '/' + d)
  .map(dname => fs.statSync(dname).isDirectory() ? 
    forceRemove(dname) : fs.unlinkSync(dname)
  )
  .filter(res => res !== undefined)

  return sub.length === 0 ? fs.rmdirSync(dir) : new Error('删除失败')
}

// 读取流 分次读入减少内存占用，防止崩溃
fs.createReadStream([fileName]) => readStream
readStream.on('data', [callback<dataChunk>])
readStream.on('end', [callback])
readStream.on('error', [callback<error>])
readStream.pipe(writeStream)

// 写入流
fs.createWriteStream([fileName]) => writeStream
writeStream.on('pipe', [callback<source>])
writeStream.write([dataChunk])
```


Zlib

```js
const zlib = require('zlib')

zlib.createGzip() => ???  可传入pipe
```

http

```js
const http = require('http')

// 网络请求
const options = {
  protocol: 'http:',
  hostname: 'api.douban.com',
  port: '80',
  method: 'GET',
  path: '/v2/movie/top250'
}

http.request(options, [callback<responseStream>]) => request 
request.on('error', [callback<error>])
request.end()

responseStream.setEncoding([typeString]) // typeString: 'utf8'
responseStream.on('data', [callback<dataChunk>])

// 服务器
http.createServer() => server
server.on('request', [callback<request, response>])
server.listen([port])

```


path

```js
const path = require('path')

path.resolve([startPath], [aimPath])
```

使用项目内依赖的命令工具


```js
package.json

{
  // ...
  "scripts": {
     "start": "./node_modules/.bin/nodemon index.js"
  }
}
```

### Node 运行 es6

1. 安装需要的 package

  ```bash
  $ yarn add @babel/cli @babel/core @babel/node @babel/preset-env nodemon -D
  ```

2. 配置 `.babelrc`

  ```json
  { "presets": ["@babel/preset-env"] }
  ```

3. 配置package.json

  ``` json
  {
    //...
    "scripts": {
      "start": "nodemon lib/index.js --exec babel-node",
      "build": "babel lib -d dist",
      "serve": "node dist/index.js"
    }
    //...
  }
  ```

- Resources
  - [example node server](https://github.com/babel/example-node-server)


### node tips 

[node 捕获全局异常](https://www.jianshu.com/p/c88a71997ff7)
``` js
process.on('uncaughtException', function(err){
    console.error(err);
});
```