**Microservice architectural style** is an approach to developing a single application as a **suite of small services**, each **running in its own process** and **communicating with lightweight mechanisms**, often an HTTP resource API. These services are **built around business capabilities** and **independently deployable** by fully automated deployment machinery. There is a **bare minimum of centralized management** of these services, which may be written in **different programming languages** and use **different data storage technologies**.

微服务体系结构风格是一种将单个应用程序开发成一套小型服务的方法，每个应用程序都在自己的进程中运行，并与轻量级机制(通常是 HTTP 资源 API)通信。 这些服务是围绕业务能力构建的，可以通过完全自动化的部署机制独立部署。 这些服务只有最低限度的集中管理，可以用不同的编程语言编写，并使用不同的数据存储技术。

### Benefits of Microservices

Independent scaling
Independent releases and deployments
Independent development
Decentralized governance

### Operational Concerns

Service replication  服务复制
Service registration and discovery 服务注册和发现
Service monitoring and logging 服务监视和日志记录
Resiliency 复原力
DevOps

### When to Use Microservices

Two-pizza team / Cross functional 双比萨团队 / 跨职能
Applications with high scalability needs 具有高可扩展性需求的应用程序
Projects with high release velocity 具有高释放速度的项目

<https://blog.christianposta.com/microservices/the-real-success-story-of-microservices-architectures/>


## Independent Development

### Normal Microservice frame

```
user -> frontend[Ionic] -> Proxy[X Proxy] |-> User[Node] -> Database[PostgreSQL]
                                          |-> Feed[Node] ->        ^        -> Filestore[S3] 
```

- Shared Data Microservice Pattern(共享数据微服务模式): 

```
                             |-> Service C -|
                             |              |
Load Balancer -> Service A <-|              |- DB
                    |        |              |
                    DB       |-> Service B -|
```



- Proxy Pattern(代理模式): 

```
                             |-> Service C - DB
                             |              
Load Balancer ->  <Proxy>  <-|-> Service A - DB
                             |             
                             |-> Service B - DB
```

- Aggregator Microservice Pattern(聚合器微服务模式): 

```
                                       |-> Service A1 - DB
                |->  <Aggregator A>  <-|
                |                      |-> Service A2 - DB
Load Balancer <-|
                |                      |-> Service B2 - DB
                |->  <Aggregator B>  <-|
                                       |-> Service B1 - DB
```

- Chained Microservice Pattern(链式微服务模式): 

```
Load Balancer -> Service A <-> Service B <-> Service C
                    |             |             |
                    DB            DB            DB
```

- Branch Microservice Design Pattern(分支微服务设计模式):

``` 
                             |-> Service C 
                             |      |
                             |      DB
Load Balancer -> Service A <-|
                    |        |
                    DB       |-> Service B
                                    |
                                    DB
```

- Asynchronous Messaging Microservice Pattern(异步消息微服务模式):

```
                                                        |-> Service C 
                                                        |      |
                                                        |      DB
Load Balancer -> Service A <-> Service B  <-> <Queue> <-|
                    |             |                     |
                    DB            DB                    |-> Service D
                                                              |
                                                              DB
```

## Container

- intro
  * Building a image
  * Running the container 
  * Debugging a container
  * Image registry
  * Docker compose


### Docker 

Docker is a tool that helps to create "images". An "image" (or Docker image) is a portable package that contains the application and its dependencies. An "image" can be used to instantiate multiple "containers"


```
                ImageA                                        ImageB
     |------------|------------|                    |------------|------------|
     |            |            |                    |            |            |
ContainerA1  ContainerA2  ContainerA3  ......  ContainerN1  ContainerN2  ContainerN3
     |            |            |                    |            |            |
     |------------|------------|---------|----------|------------|------------|
                                         |
     |------------------------------------------------------------------------|
     |                Shared Application Binaries and Libaries                |
     |------------------------------------------------------------------------|
                                         |
     |------------------------------------------------------------------------|
     |                    Kernel of host Operating System                     |
     |------------------------------------------------------------------------|
                                         |
     |------------------------------------------------------------------------|
     |                          Compute Infrastructure                        |
     |------------------------------------------------------------------------|
```

#### Benefit of Containers

- Docker 映像使开发人员在不同的硬件和平台上创建、部署和运行应用程序变得更加容易，更加快捷。 目前，Docker 已经成为 ci / cd 流水线中不可缺少的工具
- Containers share a single kernel and share application libraries. 容器共享一个内核并共享应用程序库
- Containers cause a lower system overhead as compared to Virtual Machines. 与虚拟机相比，容器会导致较低的系统开销
- Containers are platform independent
- Containers are easy to manage as compared to Virtual Machines (VMs)


#### Building your first image

1. Dockerfile 

Docker can build images automatically by reading the instructions from a **Dockerfile**.
A **Dockerfile** is a text document that contains all the commands a user could call 
on the command line to assemble an image. Using docker build, users can create 
an automated build that executes serveral command-line instructions in succession.

`Dockerfile` example:

``` bash
# Dockerfile - a file without any extension.
#~ The 'FROM' instruction initializes a new build stage and sets the Base Image
#~ for subsequent instructions. As such, a valid Dockerfile must start with a 'FROM'
#~ instruction. The image can be any valid image - it is especially easy to start 
#~ by pulling an image from the Public Repositories.
FROM node:12

### Create app directory
#~ The 'WORKDIR' instruction sets the working directory for any 'RUN', 'CMD', 
#~ 'ENTRYPOINT', 'CPOY' and 'ADD' instructions that follow it in the Dockerfile.
#~ If the 'WORKDIR' doesn't exist, it will be created even if it's not used in
#~ any subsequennt 
WORKDIR /usr/src/app


### Install app dependencies
### A wildcard is used to ensure both package.json AND package-lock.json are copied
### where available(npm@5+)
#~ The 'COPY' instruction copies new files or directories from <src> and adds them
#~ to the filesystem of the container at the path <dest>
COPY package*.json ./
#~ The 'RUN' instruction will execute any commands in a new layer on top of the current 
#~ image and commit the results. The resulting committed image will be used for the 
#~ next step in the Dockerfile.
#~ Layering 'RUN' instructions and generating commits conforms to the core concepts
#~ of Docker where commits are cheap and containers can be created from any point
#~ in image's history, much like source control.
RUN npm ci

### Bundle app source
COPY . .
#~ The 'EXPOSE' instruction informs Docker that the container listends on the specified
#~ network ports at runtime. You can specify whether the port listens on TCP or UDP
#~ and the default is TCP if the protocol is not specified.
#~ The 'EXPORT' instruction does not actually publish the port It functions as a
#~ type of documentation between the person who builds the image and the person 
#~ who runs the container, about which ports are intended to be published.
EXPOSE 8080
#~ There can only be one 'CMD' instruction in a Dockerfile. If you list more than
#~ one 'CMD' then only the last 'CMD' will take effect.
#~ The main purpose of a 'CMD' is to provide defaults for an executing container.
#~ These defaults can include an executable, or they can omit the executable, in
#~ which case you must specify an 'ENTRYPOINT' instruction as well.
CMD ["npm", "run", "prod"]
```

``` bash
# build image with Dockerfile in '.' directory
$ docker build -t <your_dockerhub_username_lowercase>/<image-name> .
```

``` bash
# list all images
$ docker images
# 
$ docker image rm -f <image_name/ID>
# Remove unused or dangling images
$ docker image prune
```

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Dockerizing a Node.js web app](https://nodejs.org/de/docs/guides/nodejs-docker-webapp/)

``` bash
# run container
$ docker run --publish 8080:8080 --name <name> <your_dockerhub_username_lowercase>/<image-name>
```


``` bash
# Use the following commands if you want to remove any running container:
$ docker container ls
$ docker container kill <container_name>
$ docker container prune
```

#### Debug a container

``` bash
# Docker logs 命令向您显示容器的日志
$ docker logs <container_name>
# 可以使用以下命令继续跟踪容器的新输出
$ docker logs <container_name> --follow
# 只查看日志末尾的行
$ docker logs <container_name> --tail 3
```



``` bash
# You can run a command in a running container exec. This command will open a bash terminal inside the container:
$ docker exec -it feed bash
```

- [docker logs](https://docs.docker.com/engine/reference/commandline/logs/)
- [docker exec](https://docs.docker.com/engine/reference/commandline/exec/)


#### Important commands in Docker

- container 
  * `create`: Create a container from an image.
  * `start`: Start an existing container.
  * `run`: Create a new container and start it.
  * `ps`: List running containers.
  * `inspect`: See lots of info about a container.
  * `logs`: Print logs.
  * `stop`: Gracefully stop a running container.
  * `kill`: Stop the main process in a container abruptly.
  * `rm`: Delete a stopped container.
- images
  * `build`: Build an image.
  * `push`: Push an image to a remote registry.
  * `images`: List images.
  * `history`: See intermediate image info.
  * `inspect`: See lots of info about an image, including the layers.
  * `rm`: Delete an image.

- [docker CLI](https://docs.docker.com/engine/reference/commandline/docker/)


#### Docker Compose

Dockercompose 允许我们使用多个容器运行应用程序。 我们将使用一个 YAML 文件来配置我们需要的所有服务，
然后运行一个命令来创建和启动所有服务。

``` bash
# nginx.conf
worker_processes 1;  
events { worker_connections 1024; }
error_log /dev/stdout debug;

http {
  sendfile on;

  upstream user {
    server backend-user:8080;
  }

  upstream feed {
    server backend-feed:8080;
  }

  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Host $server_name;

  server {
    listen 8080;
    location /api/v0/feed {
      proxy_pass http://feed;
    }
    location /api/v0/users {
      proxy_pass http://user;
    }       
  }

}
```

``` yaml
# docker-compose.yaml
version: "3"
services:
 reverseproxy:
   image: your_dockerhub_username_lowercase/reverseproxy
   ports:
     - 8080:8080
   restart: always
   depends_on:
    - backend-user
    - backend-feed   
 backend-user:
  image: your_dockerhub_username_lowercase/udacity-restapi-user
  volumes:
   - $HOME/.aws:/root/.aws
  environment:
   POSTGRESS_USERNAME: $POSTGRESS_USERNAME
   POSTGRESS_PASSWORD: $POSTGRESS_PASSWORD 
   POSTGRESS_DB: $POSTGRESS_DB 
   POSTGRESS_HOST: $POSTGRESS_HOST 
   AWS_REGION: $AWS_REGION 
   AWS_PROFILE: $AWS_PROFILE 
   AWS_BUCKET: $AWS_BUCKET
   JWT_SECRET: $JWT_SECRET
   URL: "http://localhost:8100"
 backend-feed:
  image: your_dockerhub_username_lowercase/udacity-restapi-feed
  volumes:
   - $HOME/.aws:/root/.aws
  environment:
   POSTGRESS_USERNAME: $POSTGRESS_USERNAME
   POSTGRESS_PASSWORD: $POSTGRESS_PASSWORD 
   POSTGRESS_DB: $POSTGRESS_DB 
   POSTGRESS_HOST: $POSTGRESS_HOST 
   AWS_REGION: $AWS_REGION 
   AWS_PROFILE: $AWS_PROFILE 
   AWS_BUCKET: $AWS_BUCKET
   JWT_SECRET: $JWT_SECRET
   URL: "http://localhost:8100"
 frontend:
  image: your_dockerhub_username_lowercase/udacity-frontend
  ports:
   - "8100:80"
```

```yaml
# docker-compose-build.yaml
version: "3"
services:
 reverseproxy:
 build:
 context: .
 image: your_dockerhub_username_lowercase/reverseproxy 
 backend_user:
 build:
 context: ../../udacity-c3-restapi-user
 image: your_dockerhub_username_lowercase/udacity-restapi-user
 backend_feed:
 build:
 context: ../../udacity-c3-restapi-feed 
 image: your_dockerhub_username_lowercase/udacity-restapi-feed
 frontend:
 build:
 context: ../../udacity-c3-frontend 
 image: your_dockerhub_username_lowercase/udacity-frontend:local
```

```bash
# Build the images for each of our defined services, using the command
$ docker-compose -f docker-compose-build.yaml build --parallel
# To start the system, run a container for each of our defined services, in the attached mode:
$ docker-compose up
# Alternatively, you may use detached mode to run containers in the background
$ docker-compose up -d 
# To see the list of running container
$ docker-compose ps
```

### Container Orchestration

- creation of a Kubernetes cluster
- Deployment of an microservice application as a pod
- Converting a pod into a deployment

#### Kubernetes

Kubernetes (K8s)是一个 Apache 2.0许可的开源容器编排工具，用于有效地管理集装箱化应用程序.

> Use the SAME API across bare metal and EVERY cloud provider

- Known as the linux kernel if dustributed systems.
- Abstracts away the underlying hardware of the nodes and provides a uniform interface 
for workloads to be both deployed and consume the shared pool of resources.
- Works as an engine for resolving state by converging actual and the desired 
state of the system.

#### Decouples Infrastructure and Scaling 

- All services within Kubernetes are natively Load Balanced.
- Can scale up and down dynamically 
- Used both to enable self-healing and seamless upgrading or rollback of application

#### What can it REALLY do?

- Autoscale Workloads
- Blue/Green Deployments
- Fire off jobs and scheduled cronjobs
- Manage Stateless and Statefull Applications(e.g. persistent volumes)
- Easily integrate and support 3rd party apps


#### How does Kubernetes work?

- 一个Kubernetes 部署遵循“ Master-Worker”模型。 
  - Node - A physical or virtual machine that runs multiple containers belonging to an application.
  - Cluster - A set of Master and Worker Nodes. When we deploy Kubernetes, we get a cluster, 
  which each cluster has a minimum of one worker node. A **master node** is capable of managing 
  multiple worker nodes.
  - Master Node - A node that decides the pod scheduling, and pod replication. 
  The main components of a master node are - “kube-api-server”, “kube-scheduler”, “kube-controller”.
  - Worker Node - A node on which pods are scheduled and run.
  - Pod - A group of tightly coupled containers with shared storage, network, and a specification for how to run the containers. All the containers in a Pod are co-located and co-scheduled. The worker node(s) hosts the pods


#### The architecture of a Kubenetes cluster

- kubelet - a “node agent” using which the worker node communicates with the master node. The kubelet runs on each Node.
- kube-proxy - a “node agent” using which the worker node communicates with the external world. The kube-proxy also runs on each Node.
- kube-apiserver - the frontend API that exposes the Kubernetes control plane.
- etcd - a key-value store to stores the cluster state
- kube-scheduler - a component that schedules the pods for running on the most suitable Node.
- kube-controller-manager - a component that bundles and runs controller processes. These processes concern the nodes, replication, endpoints, and access management.

- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [Learn Kubernetes Basics, which includes cluster creation, application deployment, scaling up, update and debug the containerized application.](https://kubernetes.io/docs/tutorials/kubernetes-basics/)


#### KubeOne

|Command|	Description|
|:---|:---|
|kubectl|	To display category-wise list all the commands and corresponding description|
|kubectl version|	To display the version of installed Kubernetes client and server |
|kubectl version --client|	To display the version of installed Kubernetes cluster |
|kubectl config current-context|	To display the configuration file name for the current context |
|kubectl get nodes|	To display the list of nodes along with their status, role, age, and version |
|kubectl get pods|	To display the list of containers in current namespace |
|kubectl get pods --all-namespaces|	To display all pods in all namespaces |
|kubectl cluster-info|	To display the cluster state. It returns a URL |

### Kubernetes Pod

- Pod is the smallest unit we can execute in Kubernetes.
- Pod is a group of one or more container which shares the storage.


豆荚内的容器组具有以下基本特征:

- share the same namespace (IP address and ports), storage, and network
- can communicate within the set using `localhost`
- behaves like a single entity.
- will always run on a single host node (co-located) until the service that they run is terminated. Then, it frees up the resources of the node.
- will always be scheduled together to run on a host node as a single entity (co-scheduled). If a container is shut down/added/removed, then the pod has to "restart". Here, the "pod restart" means to restart the environment the containers run in. 
- uses Docker as the container runtime
- run a single instance of the containerized application. Multiple instances of the application (horizontal-scaling) can be created by running multiple pods, one for each application instance.

### Converting a pod into a Deployment

Deployment is:
- create new Pods or ReplicaSets
- delete the existing Deployments, thereby releasing the compute resources occupied by them

``` yaml
# reverseproxy-deployment.yaml

apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  labels:
    service: reverseproxy
    # version: v2 ### for update 'reverseproxy' deployment
  name: reverseproxy
spec:
  replicas: 2
  # pod template
  template: 
    metadata:
      labels:
        service: reverseproxy
        # version: v2 ### for update 'reverseproxy' deployment
    spec:
      containers:
      - image: scheele/reverseproxy
        name: reverseproxy
        imagePullPolicy: Always          
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "1024Mi"
            cpu: "500m"       
        ports:
        - containerPort: 8080
      restartPolicy: Always
```

``` 
Deployment - ReplicaSet - Pod
```

``` bash
$ kubectl apply -f reverseproxy-deployment.yaml
$ kubectl get deployment
$ kubectl get rs
$ kubectl get pod
```

### Deployment of an microservice application as pod

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-example
spec:
  containers:
  - image: <docker>
    name: name
    imagePullPolicy: Always
    resources: 
      requests:
        memory: '64Mi'
        cpu: '250m'
      limits:
        memory: '1024Mi'
        cpu: '500m'
    ports:
    - containerPort: 8080
  restartPolicy: Always
```


## Service Registration, Discovery & Scaling

- Configuration of the application
- Overview about Service registration and discovery
- Creation of Service
- Connection service with a deployment
- Scaling the application

### ConfigMaps & Secrets

Kubernetes有一个从应用或容器解耦配置的集成模式。这个模式利用了两个Kubernetes组件。ConfigMaps和Secrets。

#### ConfigMap

- Externalized data stored within kubernetes. 存储在 kubernetes 中的外部化数据
- Can be referenced through several different means: 可以通过几种不同的方式引用:
  - environment variable 环境变量
  - a command line argument (via env var) 命令行参数(通过 env var)
  - injected as a file into a volume mount 以文件形式注入到卷装载中
- Can be created from a manifest, literals, directories, or files directly.

example:

```yaml
apiVersion: v1
kind: ConfigMap
data:
  AWS_BUCKET: udagram-scheele-dev
  AWS_PROFILE: default
  AWS_REGION: us-east-2
  JWT_SECRET: hello
  POSTGRESS_DB: udagramscheeledev
  POSTGRESS_HOST: udagram-scheele-dev. xaytk2sgtsw.us-east-2.rds.amazonaws.com
  URL: http://localhost:8100  
metadata:
  name: env-config
```

#### Secret

- Functionally identical to a ConfigMap. 与 ConfigMap 在功能上相同
- Stored as base64 encoded content. 存储为 base64编码的内容
- Encrypted at rest within etcd (if configured!). 加密休息在 etcd (如果配置!)
- Ideal for username/passwords, certificates or other sensitive information that should not be stored in a container. 理想的用户名 / 密码、证书或其他敏感信息不应该存储在容器中
- Can be created from a manifest, literals, directories, or from files directly. 可以直接从清单、文本、目录或文件创建

example:

``` yaml
apiVersion: v1
kind: Secret
data:
  AWS_PASSWORD: YyFCXCpkJHpEc2I=
  AWS_USERNAME: dwRhY2l0eQ==
metadata:
  creationTimestamp: '2020-02-14T09:51:05Z'
  name: aws-secret
  namespace: default
  resourceVersion: 42203
  selfLink: /api/v1/namespaces/default/secrets/aws-secret
  uid: 84cb3378-4f0f-11ea-8c82-02500000001
type: Opaque
```



### Configuration of the Application


### Service Types

Services
- Unified method of accessing the exposed workloads of Pods. 访问吊舱外露工作负载的统一方法
- Durable resource (unlike Pods) 持久资源(与豆荚不同)
  - static cluster-unique IP 静态集群唯一 IP
  - static namespaced DNS name 静态名称空间的 DNS 名称
  `<service name>.<namespace>.svc.cluster.local`

- Target Pods using equality based selectors. 使用基于相等的选择器的目标吊舱
- Uses kube-proxy to provide simple load-balancing. 使用 kube-proxy 提供简单的负载平衡
- kube-proxy acts as a daemon that creates local entries in the host’s iptables for every service. Kube-proxy 充当一个守护进程，为每个服务在主机的 iptables 中创建本地条目



Services type: 
- ClusterIP (default) Clusterip (默认值)
- NodePort
- LoadBalancer 负载均衡器
- ExternalName 外部名称

Creation of Service

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    service: backend-feed
  name: backend-feed
spec:
  ports:
  - name: "8080"
    port: 8080
    targetPort: 8080
  selector:
    service: backend-feed
```


Scaling the Application

``` bash
$ kubectl scale deployment/user --replicas=10
```

### Independent releases and deployments

- CI/CD Overview
- Travis as a CI example 
- Connect Github and CI/CD


### CI/CD Overview

- CI/CD: DevOps 模型中遵循的最佳实践之一
- DevOps: 是行业最佳实践和一系列工具的组合
  * Increase the speed of software delivery 提高软件交付的速度
  * Increases the speed of software evolution 提高软件进化的速度
  * Have better reliability of the software 具有较好的软件可靠性
  * Have scalability using automation, 使用自动化具有可扩展性,
  * Improved collaboration among teams. 改善团队之间的协作

在 DevOps 模型中，开发和运营团队合并为一个团队。 这些 DevOps 团队使用一些工具和最佳实践来有效地完成他们的目标。 其中一些最佳做法是:

- Continuous Integration / Continuous Delivery (CI/CD) 持续集成 / 持续交付集成
- Microservices 微服务
- Infrastructure as Code (IaaC) - Configuration Management and Policy as a Code 基础设施作为准则(IaaC)-组态管理和政策作为准则
- Monitoring and Logging 监察及记录
- Communication and Collaboration 沟通与协作


#### What is CI/CD

- Frequent releases
- Automated processes
- Repeatable
- Fast processing

#### What is Continuous Integration (CI)

Continuous Integration is a practie where members of a team integrate their work
frequently. Each integration is verified by an automated build (including tests)
to detect integration errors as quickly as possible.

持续集成是一个团队成员经常集成他们的工作的实践。每个集成都要通过自动构建（包括测试）来验证，以尽快发现集成错误。

typical task:

- Integration
- Testing
- Linting
- Building

#### What is Continuous Delivery (CD)

Continuous Delivery is a software development discipline where you build software
in such a way that the software can be released to production at any time.

持续交付是一门软件开发的学科，在这门学科中，你在构建软件的过程中，可以随时将软件发布到生产中。

typical task:

- Lifecycle Management: how you can deploy and manage the lifecycle of your 
whole development workflow. 如何部署和管理整个开发工作流程的生命周期。
- Pipelines: With pipelines to define at which stage of the development you
deploy your application to specific system. 通过管道来定义你在开发的哪个阶段将你的应用部署到特定的系统中。
- Deployable any time

### CI/CD Key Concepts

- Small, Iterative Changes
- Trunk-based Development or Git Flow
- Fast Building and Testing Phases
- Consistency Throughout the Deployment Pipeline
- Decouple Deployment and Release
