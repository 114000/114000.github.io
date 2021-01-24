---
layout: post
title: 新建项目时的基本配置（webpack）
desc:
date: 2016-07-05
categories: 前端
thumbnailImage: https://hd.unsplash.com/photo-1465628976988-fe43bda15798
coverImage: https://hd.unsplash.com/photo-1465628976988-fe43bda15798
tags:
- Javascript
---
使用 webpack 新建前端项目时，不同功能的配置比较繁琐，在此列举一些自己常用到的配置。

<!-- more -->

<!-- toc -->

---

## es6(Babel) 的配置

需要的 npm 包

1. [babel-core](https://github.com/babel/babel-loader)
2. [babel-loader](https://github.com/babel/babel-loader)
3. [babel-preset-es2015](https://www.npmjs.com/package/babel-preset-es2015)
4. [babel-preset-stage-2](https://www.npmjs.com/package/babel-preset-stage-2)

.babelrc

``` javascript
{
  "presets": ["es2015", "stage-2"]
}
```

webpack.config.js

``` javascript
module.exports = {
  // ...
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel', exclude: /node_modules/ }
    ]
  }
}
```

## Eslint 的 standard 配置

需要的 npm 包

1. [eslint](https://github.com/eslint/eslint)
2. [eslint-loader](https://github.com/MoOx/eslint-loader)
3. [eslint-config-standard](https://github.com/feross/eslint-config-standard)
4. [eslint-plugin-standard](https://github.com/feross/eslint-config-standard)
5. [eslint-plugin-promise](https://github.com/feross/eslint-config-standard)


.eslintrc

``` javascript
{
  "extends": "standard"
}

```

webpack.config.js

``` javascript
module.exports = {
  // ...
  module: {
    loaders: [
      { test: /\.js$/, loader: 'eslint', exclude: /node_modules/ }
      // 如果同时使用babel 需要先进行 eslint 检测
      // { test: /\.js$/, loader: 'babel!eslint', exclude: /node_modules/ }
    ]
  }
}
```

## Postcss 补全浏览器前缀的配置

需要的 npm 包

1. [postcss](https://github.com/postcss/postcss)
2. [postcss-loader](https://github.com/postcss/postcss-loader)
3. [autoprefixer](https://github.com/postcss/autoprefixer)
4. [css-loader](https://github.com/webpack/css-loader)
5. [style-loader](https://github.com/webpack/style-loader)

webpack.config.js

``` javascript
module.exports = {
  // ...
  module: {
    loaders: [
      {
        test: /\.css$/,
        loader: 'style!css!postcss'
      },
    ]
  },
  postcss: function () {
    return [
      require('autoprefixer')({ browsers: ['ie > 8', 'iOS >= 7', 'Firefox >= 20'] })
    ]
    // 如果你想要更多的postcss的插件，可以安装对应的包，然后在此数组中返回
    // return [require('autoprefixer'), require('precss')]
  },
}
```

tips: [`autoprefixer` 选择浏览器范围](https://github.com/ai/browserslist)


### 文件监听

轮询判断文件的最后编辑时间是否变化

``` js
module.exports = {
  // 默认 false
  watch: true,
  watchOptions: {
    ignored: /node_modules/, // 默认为空
    aggregateTimeout: 300, // 
    poll: 1000, // 每秒轮询1000次

  }
}
```

### 热更新

webpack-dev-server

``` js
module.exports = {
  mode: 'development'
  devServer: {
    hot: true // 启动 webpack.HotModuleReplacementPlugin
  }
}
```


webpack 构建出来的 bundle.js 本身是不具备热更新的能力的，HotModuleReplacementPlugin 
的作用就是将 HMR runtime 注入到 bundle.js，使得bundle.js可以和HMR server建立 
websocket 的通信连接


### 文件指纹策略

- Hash: 只要项目有修改，整个项目构建的hash 值就会更改
- Chunkhash: 不用的 entry 生成不同的 chunkhash 
- Contenthash: 根据文件内容定义 hash 文件内容不变，则contenthash 不变一般用于css

占位符

- `[ext]`: 资源后缀名
- `[name]`: 文件名称
- `[path]`: 文件的相对路径
- `[folder]`: 文件所在文件夹
- `[contenthash]`: 文件的内容 hash, 默认是md5生成
- `[hash]`: 
- `[emoji]`: 一个随机指代文件内容的 emoji

`[hash:8].[ext]` 取hash前8位， 默认32位

### 代码压缩

- JS 代码压缩 TersorPlugins, 默认也有代码压缩
- CSS 代码压缩 OptimizeCssAssetsWebpackPlugin, cssnano
- HTML 代码压缩 HtmlWebpackPlugin

### 清理构建目录

CleanWebpackPlugin 

### 复制静态文件

CopyWebpackPlugin

### CSS 功能增强

- postcss, 
  - autoprefixer 补齐样式前缀
  - cssnext 使用以后版本的css
- px2rem-loader: `options: { remUnit: 75 /* 一个 rem 对应的像素数 */, remPrecision: 8 /* px 转换为rem 的小数位数 */}`
  - <https://github.com/amfe/lib-flexible> 计算根元素的值

### 静态资源内联

- html: `raw-loader`
- js: `raw-loader`
- css: `style-loader`, `html-inline-css-webpack-plugin`
