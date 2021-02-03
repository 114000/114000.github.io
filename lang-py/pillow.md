
### 打开图片

``` py
from PIL import Image

img = Image.open('path')
```

### 保存图片

``` py
img.save('path.[jpg|png]')
```

### 转换灰度图片

``` py
img.convert('L')
```

### 改变图片尺寸(缩略图)

``` py
img.thumbnail((128, 128))
out = img.resize((128, 128))
```

### 旋转

``` py
out = img.rotate(45)
```

### 裁切图片

``` py
img.crop((100, 100, 400, 400))
```

### 灰度变换

``` py
from PIL import Image
from numpy import *

im = array(Image.open('empire.jpg').convert('L'))

im2 = 255 - im # 对图像进行反相处理

im3 = (100.0/255) * im + 100 # 将图像像素值变换到100...200 区间

im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像

## 查看最大最小值
```

### Numpy

``` py
pil_im = Image.fromarray(im)
pil_im = Image.fromarray(uint8(im))
```

### 直方图均衡化

``` py
def histeq(im,nbr_bins=256):
  """ 对一幅灰度图像进行直方图均衡化"""

  # 计算图像的直方图
  imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
  cdf = imhist.cumsum() # 累积分布函数
  cdf = 255 * cdf / cdf[-1] # 归一化

  # 使用累积分布函数的线性插值，计算新的像素值
  im2 = interp(im.flatten(),bins[:-1],cdf)

  return im2.reshape(im.shape), cdf
```

### 图像平均

``` py
def compute_average(imlist):
  """ 计算图像列表的平均图像"""

  # 打开第一幅图像，将其存储在浮点型数组中
  averageim = array(Image.open(imlist[0]), 'f')

  for imname in imlist[1:]:
    try:
      averageim += array(Image.open(imname))
    except:
      print imname + '...skipped'
  averageim /= len(imlist)

  # 返回uint8 类型的平均图像
  return array(averageim, 'uint8')
```


### 主成分分析

``` py

from PIL import Image
from numpy import *

def pca(X):
  """ 主成分分析：
    输入：矩阵X ，其中该矩阵中存储训练数据，每一行为一条训练数据
    返回：投影矩阵（按照维度的重要性排序）、方差和均值"""

  # 获取维数
  num_data,dim = X.shape

  # 数据中心化
  mean_X = X.mean(axis=0)
  X = X - mean_X

if dim>num_data:
  # PCA- 使用紧致技巧
  M = dot(X,X.T) # 协方差矩阵
  e,EV = linalg.eigh(M) # 特征值和特征向量
  tmp = dot(X.T,EV).T # 这就是紧致技巧
  V = tmp[::-1] # 由于最后的特征向量是我们所需要的，所以需要将其逆转
  S = sqrt(e)[::-1] # 由于特征值是按照递增顺序排列的，所以需要将其逆转
  for i in range(V.shape[1]):
    V[:,i] /= S
else:
  # PCA- 使用SVD 方法
  U,S,V = linalg.svd(X)
  V = V[:num_data] # 仅仅返回前nun_data 维的数据才合理

# 返回投影矩阵、方差和均值
return V,S,mean_X
```


### 高斯模糊 

``` py
from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
```