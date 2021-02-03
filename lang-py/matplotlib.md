
### 基础绘制

``` py
im = array(PIL.Image.open('path'))

# 绘制图像
imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x,y)         # 默认为蓝色实线
plot(x,y,'r*')    # 红色星状标记
plot(x,y,'go-')   # 带有圆圈标记的绿线
plot(x,y,'ks:')   # 带有正方形标记的黑色点线

# 'b' 蓝色
# 'g' 绿色
# 'r' 红色
# 'c' 青色
# 'm' 品红
# 'y' 黄色
# 'k' 黑色
# 'w' 白色
# ----
# '-' 实线
# '--' 虚线
# ':' 点线
# '.' 点
# 'o' 圆圈
# 's' 正方形
# '*' 星形
# '+' 加号
# 'x' 叉号
# 绘制线
plot(x[:2], y[:2])

# 标题
title('title string')

# 新建图像
figure()


# 置灰 不显示颜色信息
gray()

# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')

# 二值化
hist(im.flatten(), 128)


show()
```

## 交互

``` py
im = array(Image.open('path'))
imshow(im)
print('Please click 3 points')
x = ginput(3)
print 'you clicked:', x
show()
```