# docker-compose 

Compose 是用于定义和运行多容器 Docker 应用程序的工具

## 安装 docker-compose

``` bash
# 下载https://github.com/docker/compose/tags
# 太慢 host 换成get.daocloud.io
$ curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
```

#### docker-compose 常用命令

``` bash
# 构建镜像  
# production.yml 中的 services 名称 [IMAME_NAME]
# 修改端口也要重新构建镜像
$ docker-compose -f production.yml build [IMAME_NAME]

# 启动服务
$ docker-compose -f production.yml up -d
# 查看状态
$ docker-compose ps

# 查看日志
$ docker-compose -f production.yml logs [IMAME_NAME]
```