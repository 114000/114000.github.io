## type

自定义 type 显示参考 OOP 魔术方法 `__repr__`

``` py
type(3) # <type 'int'>
```

## File

## random

``` py
import random

random.randrange(3, 6) 
```



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