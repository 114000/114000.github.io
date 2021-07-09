# Docker

## Startup

### 1. CentOS

#### Install

``` bash
$ curl -fsSL https://get.docker.com/ | sh

$ systemctl start docker

# 开机启动
$ systemctl enable docker
```

#### Uninstall

``` bash
# 列出包含docker字段的软件的信息
$ rpm -qa | grep docker

$ yum remove <list>
# e.g.
$ yum remove docker-ce-cli.x86_64 1:19.03.5-3.el7
```

### Upgrade

1. Uninstall 
2. Install

#### 修改 docker 镜像源

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

## 镜像 Image

### 搜索远程镜像 


- <https://hub.docker.com/>

``` bash
$ docker search <image_name>

```

```
e.g. $ docker search centOS

NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
centos                             The official build of CentOS.                   6503      [OK]
ansible/centos7-ansible            Ansible on Centos7                              133                  [OK]
consol/centos-xfce-vnc             Centos container with "headless" VNC session…   128                  [OK]
jdeathe/centos-ssh                 OpenSSH / Supervisor / EPEL/IUS/SCL Repos - …   117                  [OK]
centos/systemd                     systemd enabled base container.                 97                   [OK]
```

### 查看本地镜像

``` bash
$ docker images
```

### 下载远程镜像到本地

``` bash
$ docker pull <image_name>
```


### 创建镜像 

#### 1. Dockerfile(推荐)

``` bash
$ mkdir <image_dir>
$ cd <image_dir>
<image_dir> $ vi Dockerfile 

### EDIT Dockerfile

$ docker build [--tag <namespace>/<image_repository>:<tag>] <dockerfile_path>
```




#### 2. 手动

``` bash
$ docker commit -m <commit_message> \
                -a <author> <container_name> | <container_id> \
                <namespace>/<image_repository>:<tag>
```

### 删除镜像

``` bash
## 删除所有使用该镜像的容器
$ docker rm <container_id> | <container_name>
$ docker rmi <image_repository> | <image_id>
```

### 推送镜像 

``` bash
$ docker login
$ docker push <namespace>/<image_repository>
```


## 容器 Container

### 启动容器(运行镜像)

``` bash
## first time
$ docker run [--name <container_name>] <image_name> [<cmd>]

## later 
$ docker start <container_name> | <container_id>


## 交互容器
$ docker run --interractive | -i <image_name> <path>


## e.g. 
$ docker run -i centos /bin/bash
[root <container_id>]\# exit
$

## 挂起
$ docker run --detach | -d run centos [<cmd>]

e.g.
$ docker run --name ping_baidu -d centos ping baidu.com
$ docker logs --follow ping_baidu
$ docker stop ping_baidu

```

### 查看容器

``` bash
$ docker ps ## 运行中
$ docker ps --all | -a 
$ docker ps --latest
```

### 查看容器日志

``` bash
$ docker logs <container_name> | <container_id>
```

### 停止容器 

``` bash
$ docker stop <container_name> | <container_id>
```

### 重启容器 

``` bash
$ docker restart <container_name> | <container_id>
```

### 删除容器

``` bash
$ docker rm <container_name> | <container_id>
```

### Docker 部署前端项目

