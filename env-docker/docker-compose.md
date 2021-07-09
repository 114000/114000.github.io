# docker-compose 

Compose 是用于定义和运行多容器 Docker 应用程序的工具

## Install

``` bash
# 查看最新版本
$ curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d'


# 下载https://github.com/docker/compose/tags
$ curl -L https://github.com/docker/compose/releases/download/x.xx.x/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

# 太慢 host 换成get.daocloud.io
$ curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

# 执行权限
$ chmod +x /usr/local/bin/docker-compose
```

## Uninstall

```
$ sudo rm rf /usr/local/bin/docker-compose
```

#### docker-compose 常用命令

``` bash
# 构建镜像  
# production.yml 中的 services 名称 [IMAME_NAME]
# 修改端口也要重新构建镜像
$ docker-compose -f production.yml build [IMAME_NAME]

# 启动服务
$ docker-compose -f production.yml up -d

# 重新构建并启动服务
$ docker-compose up -d --build

# 查看状态
$ docker-compose ps

# 查看日志
$ docker-compose -f production.yml logs [IMAME_NAME]
```