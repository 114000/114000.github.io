---
title: Python matplotlib
date: 2018-08-15
tag:
- python

---

[[toc]]

matplotlib 是 Python 主要的科学绘图库，其功能为生成可发布的可视化内容，如折线图、直方图、散点图等。将数据及各种分析可视化，可以让你产生深刻的理解，而我们将用 matplotlib 完成所有的可视化内容。

## 安装与引用

``` bash
$ pip install matplotlib
```

## 绘制正弦函数

- [numpy](./python-numpy.md)

``` python
import numpy as np
import matplotlib.pyplot as plt

## 生成坐标点
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel('x')           # x轴的单位
plt.ylabel('y')           # y轴的单位
plt.title('sin & cos')    # 图标标题
plt.legend()              # 绘制图例 sin - cos --
plt.show()
```

## 绘制阶跃函数 

``` python
import numpy as np
import matplotlib.pylab as plt

step_function = lambda x: np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
```

## 绘制图片


``` python
import matplotlib as plt
from matplotlib.image import imread

# 只能绘制 png
img = imread('your/path/pic.png')

plt.imshow(img)
plt.show()
```