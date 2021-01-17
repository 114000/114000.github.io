---
title: Lerna
date: 2020-11-21
tags:
- JavaScript
- Tool
--- 

> A tool for managing JavaScript projects with multiple packages.
> -- 用于管理具有多个程序包的JavaScript项目的工具。

### example

**React**

```
github/react -> |- npm/react`
                |- npm/react-dom
                |- npm
                |- npm
```

### lerna startup

- install
  1. `$ yarn global add lerna`
  2. `$ lerna init` 
  3. `$ lerna add [package1] --scope=[package2]`


## Flow

## Create Project

- create package

`lerna create [package name]`


### lerna sources

- [lerna 入门教程 - 对于大型项目，多个模块放在一个代码仓库里面会比较方便。lerna 是管理这种多模块复合仓库的流行工具，本文介绍 lerna 的最简单用法。](https://blog.npmjs.org/post/186494959890/monorepos-and-npm)