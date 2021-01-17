# Insomnia 网络请求测试工具

2018-05-02

测试协议的时候一般会有两个比较麻烦的地方。一是多个协议使用同一个变量，二是协议之间总有关联性（b 需要 a 返回的结果作为参数）。这篇文章会结合 Insomnia 这款精巧的桌面应用来解决这两个问题。

<!-- more -->

![](https://upload-images.jianshu.io/upload_images/711226-8accc3b3455e3a90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



[官网](https://insomnia.rest/)
[github](https://github.com/getinsomnia/insomnia)

## 应用使用结构

```
/Insomnia
|- workspace.1/              ---------------------+----------+
|    |- folder.1-1/          -------+             |          |
|    |    |- request.1-1-1          |             |          |
|    |    |- request.1-1-2          | folder env  |          |
|    |    |- request.1-1-3          |             |          |          
|    |    |...               -------+             |          |
|    |                                            | sub env  | basic env
|    |- folder.1-2/          -------+             |          |  
|    |    |- request.1-2-1          | folder env  |          |
|    |    |...               -------+             |          |
|    |- request.1.1                               |          |
|    |- request.1.2                               |          |
|    |...                    ---------------------+----------+
|
|- workspace.2/
|    |-folder.2-1/
|    |    |- request.2-1-1
|    |...
|- workspace3/
|    |...
|...
```

## 工作区



点击下拉菜单新建/切换 workspace
![](https://upload-images.jianshu.io/upload_images/711226-534358f7474e81a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

点击`+` 在**当前工作区**新建请求或文件夹
![](https://upload-images.jianshu.io/upload_images/711226-e079f5ffd47e5a38.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 环境变量

### 创建变量
每个工作区（workspace）有自己的环境变量 (Base Environment, 快捷键 `command + e`)，可供此工作区下的所有请求使用

![](https://upload-images.jianshu.io/upload_images/711226-1e785e4a79cad38f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Sub Environment 可以用来存储不同环境下的同名变量。然后可以点击主界面下拉框切换变量环境

**Note:** 如果新建的子环境变量是 private，那这个环境变量不会出现在导出文件中

![image.png](https://upload-images.jianshu.io/upload_images/711226-5a4dc529850d525d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

也可以为文件夹创建环境变量，可供文件夹内的请求使用

![](https://upload-images.jianshu.io/upload_images/711226-30eef6946e4ad5c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 变量的优先级

> Folder Environment > Sub Environment > Base Environment


### 使用变量

在任意输入框处输入变量名，都可得到变量提示

![](https://upload-images.jianshu.io/upload_images/711226-1a3fbcfb3b8462b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](https://upload-images.jianshu.io/upload_images/711226-9ba610969eb99846.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

变量可以嵌套声明

![此处 username 字段使用的是 Base Env 中 username 变量](https://upload-images.jianshu.io/upload_images/711226-a2b99e128bb61c27.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 模板标记 Tamplate Tags

### 例子

缓存请求数据是比较实际的需求。

1. 比如第一个协议需要用户登录获得 uid，第二个协议用 uid 请求该用户的收藏列表。
2. 或者获得书籍列表后，根据某一个书籍 id 获取详细信息

我们用第二个例子简单使用一下模板标记功能(为了简单此处没使用变量)



1. 我们新建 `Book` 目录，创建 `GetList` 请求，具体设置如下图，点击 `Send`，右侧有数据返回则进行下一步

**Note:** 使用了[豆瓣API](https://developers.douban.com/wiki/?title=api_v2) `https://api.douban.com/v2/book/search`

![](https://upload-images.jianshu.io/upload_images/711226-6f6ee89ea091adea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![](https://upload-images.jianshu.io/upload_images/711226-e59916e18392c354.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


2. 新建 `GetDetail` 请求, 基本配置如下

![](https://upload-images.jianshu.io/upload_images/711226-0f38ff2c5a0c0241.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

根据豆瓣API的要求我们要在链接后面添加书籍ID, 输入 res 在提示框中选择 `Response -> Body Attribute`

![](https://upload-images.jianshu.io/upload_images/711226-0a7f627aa61698b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

双击出现的红色 Tag 标签，按照下图配置，设置好后点击 `Done`

![](https://upload-images.jianshu.io/upload_images/711226-77fd51303a8668d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 回到主界面点击 `Send` 即可

### 其他

- 根据服务端返回的数据不同，可以配置不同的格式(如xml, string)，需要大家自己探索。
- 变量声明处（Base Env.etc.）也可以使用模板标记




## 偏好设置

`command + ,` 可以打开偏好设置。设置主题，字号，以及代理


end


还是比较简单实用的工具。还支持 GraphQL。 官方文档有更多的介绍，中文资料较少。有问题也可以去项目的 issues 里去看看 ：）


















