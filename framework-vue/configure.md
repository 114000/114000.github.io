---
title: Vue 项目配置
---

### Vue 配置 Tailwindcss & Purgecss

```bash
$ vue create your-project

$ cd your-project

y/$ yarn add tailwindcss purgecss @fullhuman/postcss-purgecss -D

## 生成 tailwind.config.js
y/$ ./node_modules/.bin/tailwind init
```

``` js
// postcss.config.js
const tailwindcss = require("tailwindcss")
const autoprefixer = require("autoprefixer")
const purgecss = require("@fullhuman/postcss-purgecss")

module.exports = {
  plugins: [
    tailwindcss("./tailwind.config.js"),
    autoprefixer({
      add: true,
      grid: true
    }),
    //Only add purgecss in production
    process.env.NODE_ENV === "production" ? purgecss({
      content: [
        "./src/**/*.html",
        "./src/**/*.vue"
      ]
    }) : ""
  ]
}
```