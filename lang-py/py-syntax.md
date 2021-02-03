---
title: Python syntax
date: 2018-08-18
tag:
- python
---


## 导入

``` py
import numpy as np
```



## 逻辑

``` py
if a:
  # 
else:
  #
```

## 循环

``` py
for infile in filelist:

```


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


## 数组操作

``` py
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

x[2] # 400

x[:2]
y[:2]

im[i,:] = im[j,:]      # 将第 j 行的数值赋值给第 i 行
im[:,i] = 100          # 将第 i 列的所有数值设为100
im[:100,:50].sum()     # 计算前100 行、前 50 列所有数值的和
im[50:100,50:100]      # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
im[i].mean()           # 第 i 行所有数值的平均值
im[:,-1]               # 最后一列
im[-2,:] (or im[-2])   # 倒数第二行
```

## 模块

### pickle

``` py
# 保存均值和主成分数据
f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()

# 载入均值和主成分数据
f = open('font_pca_modes.pkl', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()

# 打开文件并保存
with open('font_pca_modes.pkl', 'wb') as f:
  pickle.dump(immean,f)
  pickle.dump(V,f)

# 打开文件并载入
with open('font_pca_modes.pkl', 'rb') as f:
  immean = pickle.load(f)
  V = pickle.load(f)
```