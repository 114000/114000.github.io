

## applications

- image and voice recognition
- spam detection
- fraud detection
- stock market
- teaching a computer how to play chess
- self-driving cars


## conception 

Teaching computers to learn to perform tasks from past experiences(data).


## 机器学习中的基本算法

## decision tree 决策树

博弈论

用阈值进行分割

选出特征值的权重




**熵 entropy**

粒子移动的自由程度，
集合越稳固越具有同类性熵越低，
可知性可预测性越高熵越低



m个红球 n个蓝球

Entropy = - m/(m+n) * log2(m/(m+n)) - n/(m+n)log2(n/(m+n))

取log2，源自信息论

**信息增益**

Information Gain 
  = Change in Entropy
  = parentEntropy - (child1Entropy + child2Entropy) / 2


决策树的选择必须使得信息增益最大化

eg: 推荐应用

|Gender|Occupation|App|
|:---:|:---:|:---:|
|F|Study|Pokemon Go|
|F|Work|WhatsApp|
|M|Work|Snapchat|
|F|Work|WhatsApp|
|M|Study|Pokemon Go|
|M|Stydy|Pokemon Go|

Entropy = -3/6 * log2(3/6) - 2/6 * log2(2/6) - 1/6 * log2(1/6) = 1.46

1. 如果按性别分 

|F|M|
|:---:|:---:|
|Pokemon Go|Snapchat|
|WhatsApp|Pokemon Go|
|WhatsApp|Pokemon Go|

两边的熵均为 Entropy = -2/3 * log2(2/3) - 1/3 * log2(1/3) = 0.92

则信息增益为

1.46 -（0.92 + 0.92）/ 2 = 0.54

2. 如果按职业分

|Work|Study|
|:---:|:---:|
|Snapchat|Pokemon Go|
|WhatsApp|Pokemon Go|
|WhatsApp|Pokemon Go|

两边的商 0.92, 0

则信息增益为

1.46 - (0.92 + 0) / 2 = 1

所以选择按职业分

当特征值很多的时候，决策树经常会过拟合。为了解决这个问题要使用**随机森林（Random Forests）**，
过程如下，随机选取几个特征列来构建决策树，然后随机选取其他几列再次构建，多次随机选择。
然后我们使用得到的这些决策树，当有新数据时我们让所有决策树进行预测，并选取结果中显示最多的值
作为真正的结果

增加树的数量使得每棵决策树学习训练数据的某个部分，从而减少数据过拟合的可能性。

！！有比随机更好的方式选取列，在集成方法中介绍


决策树的超参

最大深度 max_depth: 最多可以有 2^deptch 片叶子
叶子最小样本数 min_samples_leaf: 整数为数量，小数位百分比
分裂最小样本数 min_samples_split: 整数为数量，小数位百分比
最大特征数 max_features: 




## Navie Bayes Algorithm 朴素贝叶斯算法

eg: 检测邮件

结合各种特征来猜测新邮件是否为垃圾邮件

Bayes Theorem


条件概率公式 formula of conditional probability

P(A|B)P(B) = P(B|A)P(A)


先验概率 prior: 先于实验的概率，它是根据以往经验确定的一种“主观概率”，通常是已知的，例如商品的合格率，以往战绩的胜负率
后验概率 posterior

将我们知道的，转变为我们推测的

已知 P(A) P(R|A)
推测 P(A|R)

P(A|R) = P(A)P(R|A) / ( P(A)P(R|A) + P(B)P(R|B) + P(C)P(R|C) + ...)

上边等式的右侧实际上是一个归一化的操作，即P(A)P(R|A) 分母之和的比例
A, B, C ... 互不相容


朴素：假设事件（特征）独立 
P(B1 & B2) = P(B1)P(B2)

P(A|B)P(B) = P(B|A)P(A) # 条件概率公式
P(A|B) 相关于 P(B|A)P(A)
       相关于 P(B1|A)P(B2|A)P(A)


朴素贝叶斯原理

假设：有大量单词作为特征以鉴别垃圾邮件（easy, money, cheap）
P(spam|'easy', 'money', ..., 'cheap')

1. 颠倒条件求出结果（简化的条件概率公式）
P('easy', 'money', ... , 'cheap'| spam)P(spam)

2. 做出朴素假设，将其拆分为多个简单银子的积，并根据数据得出这个式子的值
P('easy'|spam)P('money'|spam)P('cheap'|spam)P(spam)

3. 对非垃圾邮件也执行此操作
P('easy'|ham)P('money'|ham)P('cheap'|ham)P(ham)

4. 对2,3式子得到的值进行归一化



## gradient descent 梯度下降法

循环找出幅度下降距离最大的方向

找到负梯度来降低 Error Function

下降的方法针对权重的倒数或误差梯度函数

梯度指出了函数增加至最大时的方向

![](./i/gradientDescent.png)


使用梯度下降法的原因是：解n元一次方程组需要大量计算，当n逐渐增大时，需要转置的矩阵也就增大这样会耗费大量的计算能力，但如果矩阵的大部分条目是零，就会有一些算法能很快计算出结果

误差函数 error function

1. mean absolute error 平均绝对误差

2. squared error 均方误差


## linear regression 线性回归

线性回归会根据训练数据生成直线模型。如果训练数据包含非线性关系，
你需要选择：调整数据（进行数据转换）、增加特征数量（参考下节内容）或改用其他模型。

异常值会对线性回归的预测产生较大偏差，需要特别小心

eg: 预测房价

draw the best fitting line through data

best: 各点距离和最小，即使用gradient descent 最小化误差

调整直线的方式：

1. 绝对值技巧 absolute trick

y = (w1 + p * alpha) * x + (w2 + alpha)

alpha: Learning Rate 学习率，学习率很小防止直线过度位移
p: 点的横坐标，在斜率中代入 p 的原因
  1. 当点在其他象限时，使直线能以正确的方向旋转
  2. 当横坐标距离y周很大时，我们可以是直线旋转的幅度更大

2. 平方技巧 square trick

y = (w1 + p * (q - y) * alpha) * x + (w2 + (q - y) * alpha)

q - y: y轴方向上点到直线的距离
q: 点的纵坐标，代入q保证，点与直线的上下关系不同时 仍能向正确方向移动



3. 平均绝对值误差 mean absolute error

Error = (|y1 - y1-hat| + |y2 - y2-hat| + ... + |ym - ym-hat|) / m

y-hat: 点到预测直线在y轴方向上的映射

4. 均方误差 Mean Squareed Error

Error = ((y1 - y1-hat) ^ 2 + (y2 - y2-hat) ^ 2 + ... + (ym - ym-hat) ^ 2) / 2m

这里多除以2为了之后用，（会求这个误差函数的导数，）
另外此误差函数乘以任何常数都不会改变收敛过程，所以乘 1/2 也没有影响


平均绝对值误差与均方误差的区别

平均绝对值误差在一定范围（拟合区？）上下移动不会改变误差值，
而均方误差作为二次函数（抛物线）它存在最小值（所有值越接近方差越小），所以它在该区域移动时值是会改变的
 


但是，梯度下降步骤包括减去误差的梯度乘以学习速率 \alpha α。因此，选择均方误差还是总平方误差只是选择不同的学习速率。

在现实中，我们可以借助算法判断什么样的学习速率比较合适。因此，如果我们使用均方误差或总平方误差，算法将只是选择不同的学习速率。


批量梯度下降法

**同时**在每个数据点应用平方（或绝对）误差，使用这些值的和更新权重，并重复这一流程很多次。

随机梯度下降法

**逐个地**在每个数据点应用平方（或绝对）误差，获得可以与模型权重相加的值， 加上这个值更新权重，然后在下一个数据点重复。

小批次梯度下降法

以上两种方法在数据量大的时候计算缓慢，线性回归的**最佳方式**是将数据拆分成很多小批次。每个批次都大概具有相同数量的数据点。然后使用每个批次更新权重。


``` py
import pandas as pd
from sklearn.linear_model import LinearRegression

bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

laos_life_exp = bmi_life_model.predict(21.07931)
```

高维度

y-hat = w1x1 + w2x2 + ... + wn-1xn-1 + wn

w1,wn: 该特征的权重

在n个维度，我们设想有n-1个特征，即在n维空间绘制超平面（n-1）来拟合数据点。

与上面一样为求得权重（w1, wn）我们可以使用绝对值技巧和平方技巧，或者计算平均绝对值和平方
误差并利用梯度下降法进行最小化


多元线性回归

``` py
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Load the data from the boston house-prices dataset 
boston_data = load_boston()
x = boston_data['data']
y = boston_data['target']

# Make and fit the linear regression model
# TODO: Fit the model and assign it to the model variable
model = LinearRegression()
model.fit(x, y)

# Make a prediction using the model
sample_house = [[
  2.29690000e-01, 
  0.00000000e+00, 
  1.05900000e+01, 
  0.00000000e+00, 
  4.89000000e-01,
  6.32600000e+00,
  5.25000000e+01, 
  4.35490000e+00, 
  4.00000000e+00, 
  2.77000000e+02,
  1.86000000e+01, 
  3.94870000e+02, 
  1.09700000e+01]]
# TODO: Predict housing price for the sample_house
prediction = model.predict(sample_house)
```


多项式回归 Polynonial Resgression

y-hat = w1x^3 + w2x^2 + w3x^1 + w4

正则化 regularization

防止过度拟合，可以用于回归（regression）和分类 (classification)

在计算误差时，考虑模型的复杂性（例如，多项式系数）

Error = errors + complexityError * lambda

L1 Regularization

complexityError = 多项式系数的绝对值之和

计算效率不高（虽然看起来更简单），尽管不包含平方，不过绝对值很难微分（求导）
只有数据稀疏时，L1计算速度更快

适合稀疏输出

最大的好处在于提供特征选择，可以忽略噪声（什么意思？）

L2 Regularization

complexityError = 多项式系数的平方和

便于计算，平方是不错的导数
适合非稀疏输出


lambda 用于调节复杂度误差对模型的影响度，lambda 小的时候复杂误差对模型的影响会变小


神经网络回归 neural network

非线性数据 - 分线段拟合数据

在删除神经网络最末端的激活函数后，神经网络即可用于回归

## 感知机算法 perceptron


## logistic regression 逻辑回归

线性分类

how do we find this line that best cuts the data

减小错误数 => 对数损失函数（log loss function） => gradient descent 




## SVM support vector machine 支持向量机


如何找到更好的拟合线

最接近线的点距离线的距离总长越长 => 最大最小值 => gradient descent

the word support comes from the fact that the points close to the boundary are 
called the support.

Error = Classification Error + Margin Error

分类错误的点，距离分类线越远惩罚越大,

**分类误差** Classifier Error

我们不以 wx + b = 0(分类线)计算误差，而是以分类区间的两条边做为计算误差的函数，对即使分类正确，
但进入该区域的点也施加惩罚

**边际误差** Margin Error

Margin = 2/|W|
Error = |W|^2

Large Margin <==> Small Error
Small Margin <==> Large Error

**C Parameter**

分类误差的常数

C 变大时，我们聚焦数据的正确分类，分类更加正确，但间隔会变小
C 变小时，我们聚焦合适的间隔，间隔较大，分类误差较多

**Kernel Trick**

我们在数据上增加一些维度，寻找更高维度的表面，投射到平面上形成曲线，以分割数据


**RBF: radial basis functions kernel** 径向基核函数

gamma 越大，曲线越陡峭，截面的圆越小，拟合度越高

gamma = 1 / (2 * sigma ^ 2)

## Meural Network 神经网络

多条（线性/非线性）函数组成的（单层/多层）多节点逻辑门，

面部识别
语音识别
下棋
自动驾驶


## Kernel Trick 核函数

its very well used in supprot vector machines

在二维代表这曲线 在三维代表这分层 z = xy

提升机制


## K-Means Clustering k类均值聚类

确定披萨店的位置 

1. 随机划分区域
2. 计算区域内的点到区域中位置的距离x1，和到其他区域中心位置的距离 xn
3. 如果 xn &lt; x1 将这些点归到 n区
4. 计算区域中心位置
5. 重复 2-5

应用场景 已知聚类数量


## Hierarchical Clustering 分层聚类


1.确定类别之间最小距离 d
2.找到离x点最近的y点，如果他们之间距离小于d，则将他们放到同一组
3.如果y点已被分组，则将x也放入该组
4.重复2-3

不需要知道聚类数量 但是要知道最小距离



数据为什么要分为测试集与训练集 

是的。因为机器学习是基于统计抽样原理，即抽样的数据可以反映真实的数据分布，但是每个抽样数据也都是有偏的；同时足够复杂的机器学习模型有足够的参数完全记住一份有限的数据集的，也会同样记住其中的偏差，因此会不同于真实分布。使用独立的测试集能用来验证模型学到的是全集数据中共性，而非训练数据的特性。


Bias-Variance Tradeo


## 监督学习- 集成方法

we put a bunch of models to form a better model
我们将一堆模型，整合成一个更好的模型

**bagging** : bootstrap aggregating 自动聚集

在局部进行小规模的学习，然后再将这些模型整合

**boosting**

adaBoost 自适应增强算法 比较普遍

先进行机器学习，将结果中分类错误的惩罚增大，让下一个机器学习时注意这些错误，反复这样做很多次，得出弱选择器


weight = ln(accurancy / (1 - accurancy)) = ln(#correct/#incorrect)

算出所有区域的权重叠加然后划分区域


``` py
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
model = AdaBoostClassifier(
  base_estimator = DecisionTreeClassifier(max_depth = 2),
  n_estimators = 4 ## 弱学习器使用的最大数量
)
model.fit(x_train, y_train)
model.predict(x_test)
```
