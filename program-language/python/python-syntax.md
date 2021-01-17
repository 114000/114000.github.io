---
title: Python syntax
date: 2018-08-18
tag:
- python
---


## 一些命令

``` bash
# 更新pip
$ python -m pip install --upgrade pip 

# 安装package
$ pip install numpy
```

## 导入

``` py
import numpy as np
```



## 逻辑


### 三目

```python

(condition and [a] or [b])[0]

保证 a 为真的情况下可以直接使用
condition and 1 or 0
```

## 函数

### lambda 

``` python
lambda param1, param2, [..params]: returnStatement

eg

lambda x1, x2: x1 + x2

(lambda x1, x2: x1 + x2)(1, 2) # 3
```