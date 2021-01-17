---
title: git 常用工作流
date: 2018-06-26
tag:
- git
---



## 创建git项目
``` bash
$ git init --bare test.git
$ chown -R git:git test.git
```

## 配置钩子

``` bash
$ cd test.git/hooks
hooks$ touch post-receive
hooks$ chown git:git post-receive
hooks$ chmod 755 post-receive
hooks$ vi post-receive
```

编辑 post-receive

脚本[参考](https://blog.csdn.net/u010837612/article/details/70825225?utm_source=itdadao&utm_medium=referral)，还可以使用推送方式

``` bash
#!/bin/sh
DEPLOY_PATH=/your/project/path/

# 这条命令很重要
unset  GIT_DIR 
cd $DEPLOY_PATH
git reset --hard
git pull
chown www:www -R $DEPLOY_PATH 
```

ps: git 需要有 www 目录写的权限

``` bash
# 将 git 添加到 www 用户组
$ usermod -a -G www git 

# 给用户组赋予写的权限
$ chmod 774 www  
```

或者直接在 `/etc/sudoers` 文件中添加 git sudo 权限, 然后改用 `sudo` 执行 `chown` 命令

``` diff
admin ALL=(ALL)  NOPASSWD:ALL
+ git ALL=(ALL) NOPASSWD:ALL
```

``` bash
#!/bin/sh
# ...
sudo chown www:www -R $DEPLOY_PATH 
```


### git 第一次连接远程仓库 

``` bash
# git remote add origin <server>
$ git remote add origin git@xx.xxx.xx.xx:~/xxx.git
```

### 清楚文件夹冗余文件 

``` bash
$ git clean -df
```


## git resource

- [提交信息的规范 - 代码仓库的提交信息应该怎么写，这份规范标准可以参考](https://www.conventionalcommits.org/zh-cn/v1.0.0-beta.4/)