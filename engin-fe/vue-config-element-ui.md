---
title: Vue-Element
date: 2018-09-02


---

## 在 Vue 项目中配置一个 Element 组件库

### 依赖

- [node](https://nodejs.org/en/)
- [yarn](https://github.com/yarnpkg/yarn) (也可以使用 npm 修改相关命令即可)
- [vue cli](https://github.com/vuejs/vue-cli) 创建的 Vue@2.x 项目
- element-theme: <https://github.com/ElementUI/element-theme>

``` bash
~$ vue create [project] -d
~$ cd project
~/p $ yarn add element-ui -S
~/p $ yarn add element-theme element-theme-chalk -D
```


### 配置样式

在 `/package.json` 的 `script` 添加下面 yarn 命令，方便以后使用

``` js
{
  "script": {
    "theme": "./node_modules/.bin/et",
    "theme-install": "./node_modules/.bin/et -i ./src/component-config/theme-config.scss",
    "theme-build": "./node_modules/.bin/et -c./src/component-config/theme-config.scss -o./src/component-config/theme/",
    "theme-watch": "./node_modules/.bin/et -w -c ./src/component-config/theme-config.scss -o ./src/component-config/theme/"
  }
  // ...
}

```

``` bash
# 在 src 下新建 component-config 目录，并生成一个 scss 的配置文件
# !!!!注意：这个目录名字一定要跟 package.json script 配置的目录一致

$ mkdir component-config 
$ yarn theme-install

```

`.scss` 文件中包含主题颜色，圆角、边框等基础样式以及各个组件的一些样式的配置, 如:

``` scss
$--color-success: #67c23a !default;
$--color-warning: #e6a23c !default;
$--color-danger: #f56c6c !default;
$--color-info: #909399 !default;

$--border-width-base: 1px !default;
$--border-style-base: solid !default;
$--border-color-base: #dcdfe6 !default;

$--select-border-color-hover: $--border-color-hover !default;
$--select-disabled-border: $--disabled-border-base !default;
$--select-font-size: $--font-size-base !default;
$--select-close-hover-color: $--color-text-secondary !default;
```

根据自己项目的需求修改好之后，

``` bash
$ yarn theme-build

## or 你想监听变化进行修改
$ yarn theme-watch
```

### 使用

1. 引用全部组件

新建文件

``` js
// /src/component-config/index.js

import Vue from 'vue'
import Element from 'element-ui'
import './theme/index.css'

Vue.use(Element)
```

```js
// /src/main.js
import './component-config'
```

2. 引用部分组件

``` js
// /src/component-config/index.js

import Vue from 'vue'
import { Button, Select } from 'element-ui'


import './theme/button.css'
import './theme/select.css'

Vue.use(Button)
Vue.use(Select)

```

```js
// /src/main.js
import './component-config'
```


### Element UI resources

- [element-admin](https://github.com/umi-soft/element-admin)








