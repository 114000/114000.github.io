---
title: 感知机 perceptron
date: 2018-08-18
tag:
- machine
---

感知机理论上保留着能够解决复杂函数的可能性（多层感知机）,
但是权重需要人工设定

## 人工神经元,朴素感知机

感知机接收多个信号(x1, x2)，(到达阈值θ)输出一个信号

```
     |- 0 (w1x1 + w2x2 <= θ)
y = -| 
     |- 1 (w1x1 + w2x2 > θ)
```
w1, w2 是权重(weight): 调节输入信号的重要性
b(偏置bias uniy, -θ): 调整神经元被激活的难易度

AND gate(&&)

```
w1 = 0.3, w2 = 0.4, θ = 0.5
θ > 0
w1 < θ
w2 < θ
w1 + w2 > θ
```
NAND gate(!&&)

```
w1 = -0.3, w2 = -0.4, θ=-0.5
θ < 0
w1 > θ
w2 > θ
w1 + w2 < θ
```

OR gate(||)

```
θ > 0
w1 > θ
w2 > θ
```

``` python
def AND (x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  return w1 * x1 + w2 * x2 > theta and 1 or 0


def generateGate(w1, w2, b):
  w = np.array([w1, w2])
  return lambda x1, x2: np.sum(w*np.array([x1, x2])) + b > 0 and 1 or 0

AND = generateGate(0.5, 0.5, 0.7)
OR = generateGate(0.5, 0.5, -0.2)
NAND = generateGate(-0.5, -0.5, 0.7)
```

XOR 无法用线性函数表示

## 多层感知机(multi-layered perceptron)

通过叠加层（加深层），感知机能进行更加灵活的表示.

``` python
XOR = lambda x1, x2: AND(OR(x1, x2), NAND(x1, x2))
```

```
第0层        第1层         第2层
x1     s1 = OR(x1, x2)    
                           AND(s1, s2)
x2     s2 = NAND(x1, x2)
```

理论上2层感知机就能构建计算机，但一般比较自然的做法是，
`与门，或门` - `半加器，全加器` - `算数逻辑单元ALU` - `CPU`


调整曲线方式


line: 3x1 + 4x2 - 10 = 0
point: (1, 1) bias = 1
learning rate: 0.1

3        4        -10
1 * 0.1  1 * 0.1  1 * 0.1   +(如果点在指向上方则为 - )
——————————————————————————————
3.1      4.1      -9.9

new line: 3.1x1 + 4.1x2 - 9.9 = 0