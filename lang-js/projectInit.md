---
title: Webpack 以及前端项目初始化
date: 2018-07-16
tag:
- javascript
---

[[toc]]


``` bash
$ npm i yarn -g
```

## 基本用法

### Getting Started


``` bash
$ mkdir [project-dir]
$ cd [project-dir]
$ yarn init -y
```

``` bash
$ yarn add webpack webpack-cli -D
$ mkdir src dist
$ touch webpack.config.js dist/index.html src/index.js

```

``` js
/* /webpack.config.js */
const path = require('path')

module.exports = {
  entry: './src/index.js', // 源代码入口
  output: {
    filename: 'main.js', // index.html 要引入的文件
    path: path.resolve(__dirname, 'dist')
  }
}
```

```html
<!-- /dist/index.html -->
...
<script src="main.js"></script>
...
```

``` diff
/package.json
  {
    "name": "project-name",
    "version": "1.0.0",
+   "private": true
-   "main": "index.js",
+   "script": {
+     "build": "webpack --mode=production" 
#     -- 指定 mode, 防止 warning 提示
+   } 
    "license": "MIT",
    "devDependencies": {
      "webpack": "^4.16.1",
      "webpack-cli": "^3.0.8"
    }
  }
```

``` bash
$ yarn build
```




### (HMR) Hot Module Replacement

基于 Getting Started 的代码

- 参考：<https://webpack.js.org/guides/development/#using-webpack-dev-server>

``` bash
$ yarn add webpack-dev-server -D
```

```diff
/webpack.config.js
  const path = require('path')

  module.exports = {
    entry: './src/index.js', // 源代码入口
    output: {
      filename: 'main.js', // index.html 要引入的文件
      path: path.resolve(__dirname, 'dist')
    },
+   devServer: {
+     contentBase: './dist'  
+   }
  }
```

``` diff
/package.json
  "scripts": {
    "build": "webpack --mode=production",
+   "start": "webpack-dev-server --open --mode=development --port=23333"
#   --mode=development 指定 mode 使HMR运行变快，
#   默认为 production 每次修改文件都会重新编译
  },
```

``` bash
$ yarn start
```
### Babel


### Postcss


## 进阶

