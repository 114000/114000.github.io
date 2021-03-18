---
title: centOS 常用软件安装
date: 2018-06-26
tag:
- linux
---

centerOS 7.3
[远程连接到Linux操作系统实例](https://help.aliyun.com/document_detail/59083.html?spm=5176.10173289.0.0.603e2e776v9mgK#%E6%9C%AC%E5%9C%B0%E4%B8%BA%20Linux%20%E6%88%96%E6%94%AF%E6%8C%81%20SSH%20%E5%91%BD%E4%BB%A4%E7%9A%84%E7%8E%AF%E5%A2%83)


## 生成 SSH Key

1. 生成 SSH Key
```
$ ssh-keygen -t rsa -C "your_email@example.com"
```

2. 配置
  - 在 github / gitlab 中配置 `~/.ssh/id_rsa.pub` 中的内容
  - 在**目标服务器**的 `~/.ssh/authorized_keys` 添加 `~/.ssh/id_rsa.pub` 中的内容



### 安装node

**Note:** Nodejs 版本各版本镜像 <https://npm.taobao.org/mirrors/node>

``` bash
#### 切换目录
$ cd /usr/local/src

#### 下载 - 此处下载的是编译好的linux版本的node, 如果下载不带平台后缀的需要自行编译
$ wget https://npm.taobao.org/mirrors/node/v14.16.0/node-v14.16.0-linux-x64.tar.gz

#### 解压 - 解压后可正常使用
$ tar xvf node-v14.16.0-linux-x64.tar.gz

#### 添加到命令行 - 需要root权限 软连接
$ ln -s /usr/local/src/node-v14.16.0-linux-x64/bin/node /usr/bin/node
$ ln -s /usr/local/src/node-v14.16.0-linux-x64/bin/npm /usr/bin/npm
```

### 添加环境变量

``` bash
$ vi ~/.bash_profile

###
export PATH=/usr/local/src/node-v12.14.1-linux-x64/bin/:$PATH
###

$ source ~/.bash_profile
```

### 安装pm2

``` bash
$ npm install pm2 -g
$ ln -s /usr/local/src/node-v12.14.1-linux-x64/bin/pm2 /usr/bin/pm2
```

### 安装 Python3

[参考](https://ehlxr.me/2017/01/07/CentOS-7-%E5%AE%89%E8%A3%85-Python3%E3%80%81pip3/)

``` bash
$ cd /usr/local/src

## 下载
$ wget https://npm.taobao.org/mirrors/python/3.6.5/Python-3.6.5.tgz

## 解压
$ tar -xzvf Python-3.6.5.tgz


## 初始化及其安装路径
$ cd Python-3.6.5
$ ./configure --prefix=/usr/local/src/python3

## 编译
$ make

## 编译安装
$ make install

## 添加到命令行
$ ln -s /usr/local/src/python3/bin/python3 /usr/bin/python3
```

### 安装git 
[报错解决参考](https://blog.csdn.net/woniu211111/article/details/54613956)

``` bash
## 下载解压
$ wget https://github.com/git/git/archive/v2.17.0.tar.gz
$ tar -xzvf v2.17.0.tar.gz
$ cd ./git-2.17.0

## 编译安装 - 此过程出现问题可以参考上面报错解决参考
$ make prefix=/usr/local/src/git all
$ make install prefix=/usr/local/src/git

## 添加到命令行
ln -s /usr/local/src/git/bin/git /usr/bin/git
```

bash: git-upload-pack: command not found
`git clone git@xx.xx.xx.xx:/home/git/test.git --upload-pack "/usr/local/src/git/bin/git-upload-pack"`