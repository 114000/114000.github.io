---
title: Python Numpy
date: 2018-08-15
tag:
- python

---

[[toc]]

NumPy 是 Python 科学计算的基础包之一。它的功能包括多维数组、高级数学函数（比如线性代数运算和傅里叶变换），以及伪随机数生成器。

NumPy 中，主要的处理也都是通过 C 或 C++ 实现的

## 安装与引用

``` bash
$ pip install numpy
```

```python
import numpy as np 
```

## 一维向量运算

``` python
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

# element-wise
x + y     # [3. 6. 9.]
x - y     # [-1. -2. -3.]
x * y     # [2. 8. 18.]
x / y     # [0.5 0.5 0.5]

# broadcast
x / 2     # [0.5 1. 1.5]
```

## 二维矩阵运算

``` python
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])

A.shape # (2, 2) 2 * 2 矩阵
A.dtype # int32

# element-wise
A + B     # [[4, 2], [3, 10]]
A - B     # [[-2, 2], [3, -2]]
A * B     # [[3, 0], [0, 24]]
A / B     # [[0.333, inf], [inf, 0.666667]]

# broadcast
A * 10       # [[10, 20], [30, 40]]
A * [10, 20] # [[10, 40], [30, 80]]

# dot
np.dot(A, B) 
# | 1, 2 |   | 3, 0 |   | 1*3+2*0, 1*0+2*6 |   | 3, 12 |
# | 3, 4 | · | 0, 6 | = | 3*3+4*0, 3*0+4*6 | = | 9, 24 |


```

## 访问元素

```python
X = np.array([[51, 55], [14, 19], [0, 4]])

X.shape      # (3, 2) 3row 2col
X.shape[0]   # 3  3row
X.ndim       # 2 维度
X[1]         # [14, 19]
x[2][1]      # 4  python
X[1, 1]      # 19 numpy
for row in X: print(row) # [51, 55], [14, 19], [0, 4]
X[[1, 2]]    # [[14, 19], [0, 4]] numpy
X[1:3]       # [[14, 19], [0, 4]] python
X[2][X[2]>0] # [4] python,numpy
X[2, X[2]>0] # [4] numpy, numpy
```

## 生成数据函数

``` python
np.arange(0, 6, 0.1) #[0, 0.1, 0.2 .... 5.8, 5.9]
```


## 数学函数 

``` python
from math import pi
np.sin([pi/6, pi/2, pi*5/6]) # [0.5 1. 0.5]
np.cos
```

### 阶跃函数

``` python
step = lambda x: np.array(x > 0, dtype = np.int)

# [-5.0. -4.0, ... 0, ... 4.0, 5.0]
# x > 0 [false, false, ... false ... true, true]
# np.int() [0, 0, ... 0, ... 1, 1]
```

### sigmoid

``` python
sigmoid = lambda x: 1 / (1 + np.exp(-x))
```


### 统计函数

- numpy.amin
- numpy.amax
- numpy.ptp 最大差值
- numpy.percentile(a, q, axis) 统计百分比
- numpy.median(a, axis) 中位数
- numpy.mean 算数平均数
- numpy.average 加权平均数
- numpy.std 标准差
- numpy.var 方差


divide

## 保存文件 

``` py
savetxt('test.txt',x,'%i')

x = loadtxt('test.txt')
``` 