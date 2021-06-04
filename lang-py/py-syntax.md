# Python syntax

## 导入

``` py
import numpy as np
import os
from os import path
```

## 逻辑



### 与, 或, 非

``` py
not 0 and 1 or 4 # => 1
```

### 操作符

``` py
1 > 2              # False
1 < 2 > 3          # 1 < 2 and 2 > 3 False
3 > 1 < 2          # 3 > 1 and 1 < 2 True
42 != '42'         # True
'N' == 'n'         # False
'J' in 'Joe'       # True

a = b = (1, 2, 3) 
c = (1, 2, 3)

a[0] is c[0]       # True
a is b             # True
a is c             # False
a == c             # True
(5 + 7) is 12      # Error

## !!! 
True > False       # True
True == 1          # True
'1' != 1           # True 

bool([])           # False
[] != False        # True
```


### 条件

``` py
if a: 
  bar()
elif: b: 
  foo()
else:
  baz()
```

### 三目

```python

a if condition else b

# 注意 and or 的区别
(condition and [a] or [b])[0]

# 保证 a 为真的情况下可以直接使用
condition and 1 or 0
```

### 推导式

### 循环

``` py
for f in files:
  pass

for i, item in enumerate(listLike):
  pass

for n in range(2, 7):
  pass # 2, 3, 4, 5, 6


while True:
  if cv2.waitKey(0): break
```

## 函数

### 函数体

``` py
''' normal '''
def add (a, b):
  return a + b

add(5, 7) # => 12


''' optional '''
def addUser (name, ip = None, address = ''):
  return {
    'name': name, 
    'ip': ip,
    'address': address
  }


''' 不定参 注意参数结构 '''
# 更多详见拆包部分

from functools import reduce

def add_ (*args):
  return reduce(lambda a, b: a + b, args)
  # return sum(args)

add_(1, 2, 3) # => 6 args: (1, 2, 3)


def addUser_ (**kwargs):
  return kwargs

addUser_(name = 'Joe', address = '') # => { 'name': 'Joe', 'address': '' }

def addUser__ (name, **kwargs):
  kwargs['name'] = name
  return addUser_(**kwargs)

addUser_('Joe', address = '') # => { 'name': 'Joe', 'address': '' }
```

### lambda 

``` python
lambda param1, param2, [..params]: returnStatement

eg

lambda x1, x2: x1 + x2

(lambda x1, x2: x1 + x2)(1, 2) # 3
```

## 标量

### 数字

#### 表示法

``` py
a = 5.0
b = 7
```

#### 操作

``` py
a + b       # 12.0
a ** 2      # 25.0
b % 3       # 1
b // 2      # 3
b / 2       # 3.5

abs(-10)    # 10
round(2 ** 0.5, 3) # 1.414
```

### 布尔

#### 表示法

``` py
True, False
```

### None

#### 操作

``` py
bool('a') # => True
bool([])  # => False
```

## 内置对象

### 字符串 

#### 表示法

``` py
# 单行
a = 'a looooong string'
b = "anthor string"
``` 

#### 操作

``` py
# repeat 
'words' * 3 # => 'wordswordswords'

# leng
len('words') # => 5

# combine

str(2) + '1' # => 21
2 + int('1') # => 3
2 + float('3') # => 5.0
2 + '1' # Error

# split & index
name = 'My Name is Joe'
name[0]       # 'M'
name[-5]      # => 's'
name[-3:]     # => 'Joe' 
name[-3:0]    # => '' 
name[11:14]   # => 'Joe' 
name[5:]      # => 'me is Joe' 
name[:7]      # => 'My name'
name[-100:20] # => 'My Name is Joe'

name.split() 
name.split(' ')  # => ['My', 'Name', 'is', 'Joe']

# replace
name.replace(n[-3:], '*' * 3) # 'My name is ***'

# find
name.find('Joe') # => 11

# format 
'My name is {}'.format(784533) # 'My name is 784533'

# count
name.count(' ') # 3
```

### list

#### 表示法

``` py
weekend = ['Sat', 'Sun']
```

#### 操作

``` py
# C
list(('Sat', 'Sun')) # => ['Sat', 'Sun']

# R 同字符串

# U
weekend.insert(0, 'Fri') # => None | weekend => ['Fri', 'Sat', 'Sun']
weekend.append('Mon')  # => None | weekend => ['Sat', 'Sun', 'Mon']
weekend.extend('Mon', 'Fri') # Error: takes exactly one argument
weekend.extend(['Mon', 'Fri']) # => None | weekend => ['Sat', 'Sun', 'Mon', 'Fri']
weekend + ['Fri'] # ['Sat', 'Sun', 'Fri'] | ['Sat', 'Sun']
# D
weekend.remove('sat') # Error
weekend.remove('Sat') # None | weekend => ['Sun']

# count
weekend.count('Sat') # 1


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

#### 列表推到 list comprehension

``` py
symbols = '$¢£¥€¤'

#

codes = []
for s in symbols:
  if s > 127:
    codes.append(ord(s))

# 
codes = list(filter(lambda c: c > 127, map(ord, symbols)))

# 
codes = [ord(s) for s in symbols if ord(s) > 127]
```


### dict

#### 表示法

``` py
d = { 'immutableKey': ['hi', 'Joe'] }
```

#### 操作

``` py
# C
dict(name = 'Joe', age = 3) # => { 'name': 'Joe', 'age': 3 }
dict([('name', 'Joe'), ('age', 3)]) # => { 'name': 'Joe', 'age': 3 }

# R
user['name'] # 'Joe'

# U
user['age'] = 5 # None | user => { 'name': 'Joe', 'age': 5 }
user.update({ 'age': 5, ip: '0' }) # None | user => { 'name': 'Joe', 'age': 5, ip: '0' }

# D
del user['age'] # None | user => { 'name': 'Joe' }
del user['ip']  # Error
```

### Tuple

#### 表示法

``` py
letters = ('a', 'b', 'c')
```

#### 操作

``` py
# C
a = (1, 2, 3)
b = tuple(a)
c = tuple([1, 2, 3])

a == b # True
a is b # True 元组特点
a == c # True
a is c # False

# R
a[2] # => 3

# count
a.count(3) # 1
```

### collections.namedtuple 具名元组

```py
# define
City = namedtuple('City', 'name country populartion coordinates')
City = namedtuple('City', ['name', 'country', 'populartion', 'coordinates'])

# C
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
139.691667))

# R
tokyo.country # => 'JP'

# class property
City._fields # 
# class method
City._make(iterable) # City(*tokyoData)
# instance method
tokyo.asdict()


```


### Set

#### 表示法

``` py
a = { 1, 2, 3, 4 }
```

#### 操作

``` py
# C
a = set((1, 2, 3, 4))
set('Joe') # => {'o', 'e', 'J'}
# U
a.add(5) # None | a => { 1, 2, 3, 4, 5 }

# R

# D
a.discard(4) # None | a => { 1, 2, 3 }
a.discard(10) # None | a => { 1, 2, 3, 4 }

x, y = set('Joe'), set('Jake')
x & y # {'e', 'J'}
x | y # {'k', 'a', 'o', 'e', 'J'}
x ^ y # {'o', 'k', 'a'}

x - y # {'o'}
y - x # {'k', 'a'}
```


## 内置序列

#### 按存储类型分类

- 容器序列(存引用, 任意类型): `list`, `tuple`, `collection.deque` 

- 扁平序列(存值, 单一类型): `str`, `bytes`, `bytearray`, `memoryview`, `array.array`

#### 按可变性分类

- 可变序列: `list`, `bytearray`, `array.array`, `collection.deque`, `memoryview`

- 不可变序列: `tuple`, `str`, `bytes`



### 生成器表达式 

``` py
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
  print(tshirt)
```

### 拆包 

``` py
a, b = b, a
lat, lng = (33.9425, -119.4080)
_, filename = os.path.split('/home/user/.ssh/id-rsa.pub')
a, b, *rest = range(5) # (0, 1, [2, 3, 4])
*head, b, c = range(5)
a, *body, c = range(5)

for name, cc, pop, (latitude, longitude) in metro_areas:
  pass

```

### 切片

`[start:stop:step]` => `seq.__getitem__(slice(start, stop, step))`

``` py
s = 'bicycle'
s[::3]  # 'bye'
s[::-1] # 'elcycib'
s[::-2] # 'eccb'

l = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]   # [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]          # [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]  # [0, 1, 20, 11, 5, 22, 9]
l[2:5] = 100        # Error 
l[2:5] = [100]      # [0, 1, 100, 22, 9]
```