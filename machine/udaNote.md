---
title: '课程笔记'
date: 2018-11-14
tag:
- machine

writing: true
---

## tool 

- Anaconda 
  一个包含数据科学常用包的 Python 发行版本。它基于 conda ——一个包和环境管理器——衍生而来。你将使用 conda 创建环境，以便分隔使用不同 Python 版本和不同程序包的项目。你还将使用它在环境中安装、卸载和更新包。通过使用 Anaconda，处理数据的过程将更加愉快。

- Jupyter notebook 
  是一种 Web 文档，能让你将文本、图像和代码全部组合到一个文档中。它事实上已经成为数据分析的标准环境。Jupyter notebook 源自 2011 年的 IPython 项目，之后迅速流行起来。在本课程的第二节课中，你将使用 Jupyter notebook 进行分析工作。




统计学知识

- 居中趋势测量
  * 均值
  * 中值
  * 众数

- 数据的离散性
  * 四分位距法
  * 异常值
  * 标准偏差
  * 贝塞尔修正


## Python Lib

### Pandas

``` py
import pandas as pd

data = pd.read_csv('2_class_data.csv') # 读取数据
```


### Numpy

``` py
import numpy as np

```

### sklearn

``` py
# 逻辑回归
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

# 神经网络
# MLP: Multilayer Perceptron 
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier()

# 决策树
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()

# 支持向量机
# SVM: Support Vector Machine
# SVC: Classifier
from sklearn.svm import SVC
classifier = SVC()

# 参数
# kernel: 核
# - 'linear', 
# - 'poly', 多项式 polynomial 
# - 'rbf', 高斯(径向基函数)核 Raial basis function
# degree: 多项式核次数
# gamma: rbf 锐化程度？
# C:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
```


## 分类算法

- 逻辑回归
- 神经网络
- 决策树
- 支持向量机

回归返回的是值，分类返回的是状态

fit 拟合 - Overfitting 过拟合
generalize 泛化

Golden 测试数据不能用于训练 thou shalt nerver use your testing data for training



## 判断模型好坏

### 混淆矩阵 Confusion Matrix



|          | Guessed Positive | Guessed Negative |
|----------|------------------|------------------|
| Postive  | True Positives   | False Negatives  |
| Negative | False Positives  | True Negatives   |


医疗模型中，假阴性比假阳性更值得注意 - 需要高召回率模型 High Recall
垃圾邮件中，假阳性比假阴性更值得注意 - 需要高精度模型 High Precision


### 准确率 Accuracy

Accuracy 
  = Correctly classified points / All points
  = (True Postives + True Negatives) / Total

Note: 仅通过准确率来评估模型比较棘手，因为对于偏斜较大的数据集，可能会完全忽略较小可能性的情况，例如信用卡欺诈行为(99.83%)

### 精度（查准率） Precision

Percision = Ture Positives / (True Positives + False Positives)

假阳性(误将祖母的邮件标记为垃圾邮件)越小越好

### 召回率（查全率） Recall

Recall = True Positives / (True Positives + False Negatives)


### 算数平均数 Arithmetic Mean

  (x + y) / 2

### 调和平均数 Harmonic Mean

  2xy / (x + y)

调和平均数始终小于算数平均数，它更接近评分较低的那个数


### F1得分

F1得分是精度和召回率的调和平均数


### Fβ得分

Fβ = (1 + β ^ 2) * x * y / (β^2 * x + y)

β小于1则越靠近精度，β大于1则越靠近召回率


### 受试者工作特性曲线 ROC: Receiver Operating Characteristic


Prefect Split ROC: 1

x x x x x x x | o o o o o o o

Good Split ROC: 0.8

x x x x o x | o x o x o o o o

Random(Bad) Split: ROC: 0.5

x o o x x o x | o x o x o o x

统计一条数据上所有拆分点的, 然后在笛卡尔坐标系中划出分布，围出的分布即是 ROC


## 回归指标 


### 平均绝对误差 Mean Absolute Error

数据点到拟合线的距离之和

``` py
from sklearn.metirics import mean_absolute_error
from sklearn.linear_model import LinearRegression

classifier = LinearRegression()
classifier.fit(X, y)

guesses = classifier.predict(X)

error = mean_absolute_error(y, guesses)
```

### 均方误差 Mean Squared Error

绝对值函数无法微分，不利于我们使用诸如梯度下降等方法。所以更常使用均方误差

``` py
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

classifier = LinearRegression()
classifier.fit(X, y)

guesses = classifier.predict(X)

error = mean_squared_error(y, guesses)
```

### R2

非常常见的回归度量

R2 = 1 - 线性回归模型的均方误差/简单模型的均方误差

Bad Model => 0
Good Model => 1

``` py
from sklearn.metrics import r2_score

y_true = [1, 2, 4]       # 真值
y_pred = [1.3, 2.5, 3.7] # 预测值

r2_score(y_true, y_pred)
```


## 错误类型

### Oversimplifying the problem - UnderFitting 欠拟合

- Does not do well in the training set. 训练集的拟合不够好
- Error due to bias. 偏差引起误差


### Overcomplicating the problem - OverFitting 过拟合

- Does well in the training set, but it tends to(趋向) memorize it instead of learning
the characteristic(特点) of it. 
- Error due to variance. 方差引起的误差


## 交差验证 


Model Complexity Graph

x: training data
o: testing data

| o
| x                                                   o
|                          o
|                          x
|                                                     x
----------------------------------------------------------------->
欠拟合underfitting            right            过拟合 overfitting
高偏差误差 high bias error                      高方差误差 high variance error

但上面有个错误，我们不能用测试数据来选择模型，测试数据只能用在最后。此处只是用来表义（分析结果）

为解决这个问题，我们从训练数据中再分离出一个交差验证集(Cross Validation)

训练集(Training Set)将用于训练参数
交差验证集(Cross Validation Set)用于对模型做出决定，（degree）
测试集(Testing Set)用于模型最终测试


### K折交叉验证 K-fold cross validation

将数据集分成 K 份，循环（K次），每次使用不同一份做为测试集，剩下的当做训练集使用，得出的平均结果作为模型

``` py
from sklearn.model_selection import KFold

kf = KFold(12, 3, shuffle = True)

for train_indices, test_indices in kf:
  print train_indices, test_indices
```

### 学习曲线 Learning Curves

![](./i/udanote1.png)

```
error
|
| x
|        x
|                 x
|                 o
|                 
|        o
|                 
| o
---------------------------------- number training points

高偏差（欠拟合）两条曲线相互接近并交于一点

error
|
| x
|                 
|        x
|                 x
|                 o
|        o
|                 
| o
---------------------------------- number training points

较好的模型相互接近并交于一个很低的点


error
|
| x
|                 
|        x
|                 x
|                 
|                 
|                 o
|        o
| o
---------------------------------- number training points
```

高方差（过拟合）训练集保持很低，交差验证集保持很高，无法相交


### 机器学习过程


1. 用训练数据训练一堆模型
2. 然后使用交差验证数据挑选最佳模型
3. 最后用测试数据测试模型是否很好

Hyper-paramters

||Hyper Parameter|paramter|
多项式|多项式次数|系数|
决策树|深度|树叶和节点等的阈值|
|支持向量机|内核(线性，多项式) gamma|


### 网格搜索 Grid Search Cross Validation

制作一个表格，列出所有可能的超参组合，寻找出合适的超参搭配

|gamma \ kernel|Linear|Polynomial|
|0.1|F1 Score = 0.5|F1 Score = 0.2|
|1|F1 Score = 0.8|F1 Score = 0.4|
|10|F1 Score = 0.6|F1 Score = 0.6|


## 线性回归

