---
title: 使用 fontmin 压缩字体(简单前端项目)
date: 2018-09-16
tag:
- node
---

### 依赖 nodejs

### 初始化项目

``` bash
$ mkdir zipfont
$ cd zipfont
```

1.初始化 node 项目，会在目录生成 package.json 文件, 参数 `-y` 选项都选默认值

``` bash
zipfont$ npm init -y  
```

2.安装项目依赖
- `--save` or `-S` 保存到 `package.json` 的 `dependencies` 字段中
- `--save-dev` or `-D` 保存到 `package.json` 的 `devDependencies` 字段中

``` bash
zipfont$ npm i fontmin --save
```

3.创建入口文件, 

``` bash
zipfont$ touch zip.js
```

找一个可以使用的字体放在目录下面


### 目录结构

``` 
/
|- node_modules/ # 项目依赖模块
|   |- ...
|
|- [字体文件].ttf
|- package.json  # 保存项目信息
|- zip.js        # 程序入口文件
```


### zip.js

4.编写代码

``` js
var Fontmin = require('fontmin')

var fontmin = new Fontmin()
  // 字体文件路径
  .src('*.ttf')
  // 中间件
  .use(Fontmin.glyph({
    text: '百家姓赵钱孙李周吴郑王'
  }))
  // 输出
  .dest('build/')

fontmin.run(function (err, files) {
  if (err) throw err
})

```

5.运行

``` bash
zipfont$ node zip.js
```

### 测试

6.新建 /index.html, 在浏览器中打开

``` html
<!DOCTYPE html>
<html lang="en">
<head>
<style>
@font-face {
  font-family: "zipfont";
  src: url("./build/站酷文艺体.ttf") format("truetype");
}

p, h1 {
  font-family: "zipfont", "萍方", "微软雅黑";
  text-align: center;
  font-size: 40px;
}

h1 {
  font-size: 60px;
}
</style>
</head>
<body>
<h1>百家姓</h1>
<p>赵钱孙李，周吴郑王。</p>
<p>冯陈褚卫，蒋沈韩杨。</p>
<p>朱秦尤许，何吕施张。</p>
<p>孔曹严华，金魏陶姜。</p>
</body>
</html>
```

### 最后

目录结构

``` 
/
|- node_modules/   # 项目依赖模（自动生成）
|   |- ...
|
|- [font].ttf      # 字体源文件
|- package.json    # 保存项目信息 （npm init -y）
|- zip.js          # 程序入口文件
|
|- build/          # 压缩完的字体文件目录（自动生成）
|   |- [font].ttf 
|   |- ...
|- index.html      # 测试用静态网页
```

以上mini版前端项目的构建过程，下面实际的项目构建过程（两者是类似的）

```
src         --  webpack/glup/grunt(解释器，编译器)        --  dist
.vue .jsx   --  vue-loader, babel                        --  html, js(polyfill)
.scss .less --  sass-loader, less-loader postcss-loader  --  css(polyfill)
.png        --  url-loader, img-loader                   --  .png(zipped), base64 in html
```

最后前端代码将会全部编译成成静态，方便服务器部署。


## Tips

- libs
  - node 8.x LTS: <https://nodejs.org/en/> 
  - fontmin <https://github.com/ecomfe/fontmin>
   
- 使用字体请注意版权 
  - [站酷免费字体](http://www.zcool.com.cn/special/zcoolfonts/)

- shell
  - [Mac: fish shell 点击下载](https://github.com/fish-shell/fish-shell/releases/download/2.7.1/fish-2.7.1.app.zip) 
  - [Windows: ](http://cmder.net/)

- 



