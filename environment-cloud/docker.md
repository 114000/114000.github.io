---
title: Docker
---

### Docker Startup

#### Linux 安装 docker

``` bash
$ yum install yum-utils device-mapper-persistent-data lvm2 -y

## 国内源 https://mydream.ink/utils/container/docker-ce.repo
$ yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

$ yum install docker-ce docker-ce-cli containerd.io -y

$ systemctl start docker

# 开机启动
$ systemctl enable docker
```

#### 卸载 docker

``` bash
# 卸载
$ yum remove docker-ce
# 删除数据
$ sudo rm -rf /var/lib/docker
```

#### 修改 docker 镜像

``` bash
$ vi /etc/docker/daemon.json

{
  "registry-mirrors": [
    "https://dockerhub.azk8s.cn",
    "https://reg-mirror.qiniu.com"
  ]
}

$ systemctl daemon-reload
$ systemctl reload docker
```

### Docker 常用命令

``` bash
$ docker ps -a # 查看容器
$ docker stop [CONTAINER IDs]
$ docker rm [CONTAINER IDs] # 删除容器
$ docker images 查看镜像
$ docker image ls
$ docker rmi [IMAGE ID] # 删除镜像
```

### docker-compose 

#### 安装 docker-compose

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

### Docker 部署前端项目



- [docker-slim - 一个 Docker 镜像文件的瘦身工具，据称最好情况下，可以让镜像文件体积缩小为原来的30分之一。](https://github.com/docker-slim/docker-slim)
- [如何将 Web 应用做成 Docker？](https://itnext.io/dockerizing-modern-web-apps-cd9667eebf44)
- [一篇简短扼要的教程，如何使用 Docker Compose 很方便地安装 PostgreSQL。](https://www.brock.sh/docker-compose-postgresql/)
- [如何在主机和 Docker 容器之间复制文件 - 软件以 Docker 容器发布的情况越来越多，docker cp命令可以在容器内外复制文件。](https://linuxhandbook.com/docker-cp-example/)
- [云原生技术公开课 - 本课程由阿里云和CNCF联合开发，课程全程免费且无需注册，主要介绍容器和 kubernetes。](https://edu.aliyun.com/roadmap/cloudnative?from=timeline)
- [Kubernetes 中文指南 - 本书是第一本系统整理的开源中文版 Kubernetes 参考资料，记录了本人从零开始学习和使用 Kubernetes 的历程，着重于总结和资料分享，同时也会有相关的概念解析](https://jimmysong.io/kubernetes-handbook/)
- [Docker 镜像构建教程：减小镜像体积](https://fuckcloudnative.io/posts/docker-images-part1-reducing-image-size/)
- [k8s YAML 生成器](https://k8syaml.com/)