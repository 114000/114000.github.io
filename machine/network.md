---
title: 神经网络
date: 2018-08-18
tag:
- machine
---


[[toc]]

## 激活函数 activation function

激活函数(h),将输入信号的总和(a)转换为输出信号(y)

``` 
a = w1x2 + w2x2 + b
y = h(a)
```

一般而言，“朴素感知机”是指单层网络，指的是激活函数使用了阶跃函数的模型。“多层感知机”是指神经网络，即使用 sigmoid 函数（后述）等平滑的激活函数的多层网络。




### sigmoid 函数

神经网络常用的一种激活函数

``` python
sigmoid = lambda x: 1 / (1 + np.exp(-x))
```

### ReLU (Rectified Linear Unit) 函数 

``` python
relu = lambda x: np.maximum(0, x)
```

### softmax 函数

``` python
def softmax (a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  
  return exp_a / sum_exp_a

def softmax (a):
  c = np.max(a)
  exp_a = np.exp(a - c) # 溢出对策
  sum_exp_a = np.sum(exp_a)
  
  return exp_a / sum_exp_a
```

指数函数经常会出现特别大的值，由于计算机的精度问题，常常会出现不确定的情况，这里要经常注意

softmax 函数的输出是 0.0 到 1.0 之间的实数。并且，softmax 函数的输出值的总和是 1 `np.sum(y) == 1`。输出总和为 1 是 softmax 函数的一个重要性质。正因为有了这个性质，我们才可以把 softmax 函数的输出解释为“概率”。

exp 是单调递增函数，所以softmax函数不会改变元素间的大小关系，
而且计算机处理指数运算需要一定的计算量，因此实际情况中，softmax 函数一般会被省略


### 恒等 (identity) 函数 

### 线性函数不能作为激活函数

线性函数的问题在于，不管如何加深层数，总是存在与之等效的“无隐藏层的神经网络”.无法发挥多层网络带来的优势

```
h(x) = cx
y(x) = h(h(h(x)))

y(x) = ax
a = c ** 3
```

### 输出层的激活函数 σ sigma

输出层所用的激活函数，要根据求解问题的性质决定。一般地:

- 回归问题可以使用恒等函数 y = x，(体重)
- 二元分类问题可以使用 sigmoid 函数 y = 1 / (1 + e ** -x)，(性别)
- 多元分类问题可以使用 softmax 函数。yk = e ** ak / (e ** a1 + ... e ** an) (yk 第k个神经元输出，n共有n个输出神经元)

## 各层间的信号传递

![](./i/036.png)

```
A(1) = [ a(1)1, a(1)2, a(1)3 ]
X = [x1, x2]
B(1) = [ b(1)1, b(1)2, b(1)3 ]
W(1) = [
  [ w(1)11, w(1)21, w(1)31 ],
  [ w(1)12, w(1)22, w(1)32 ],
]

# w(1)32
# (1) 第1层的权重
# 3 下一层(输出层)的神经元序号 a(1)3
# 2 上一层(输入层)的神经元序号 x2
```

表示为矩阵乘法 

- `A(1) = XW(1) + B(1)`
- `Z(1) = h(A(1))`

``` python
import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1)

print(A1) # [0.3, 0.7, 1.1]
print(Z1) # [0.57444252, 0.66818777, 0.75026011]
```


### 前向处理 forward

输入到输出方向 

### 后向处理 backward

输出到输入方向

神经网络可以用在分类和回归问题上