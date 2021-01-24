``` py
import cv2 as cv


def g_name (suffix):
  return 'img/shimarin{}'.format(suffix)

o = cv.imread(g_name('.jpg'))


### 写字
# cv.putText(img, 'ShimaRin', (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 4)

### 翻转 

# hor = cv.flip(o, 1) # 正数水平
# ver = cv.flip(o, 0) # 0垂直
# hor_ver = cv.flip(o, -1) # 负数水平+垂直

### 写入

# cv.imwrite(g_name('_new.jpg'), hor)
# cv.imwrite(g_name('_new.png'), ver)
# cv.imwrite(g_name('_new.bmp'), hor_ver)

cv.imshow('Output Image', hor)




cv.waitKey(0)

```