---
title: Git
date: 2018-01-01
---

## 常用工作流

### 创建裸版本Git仓库

``` bash
$ git init --bare <project_name>.git
$ chown -R git:git <project_name>.git
```