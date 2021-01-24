## Introduction

What is "Serverless"

- A buzzword (not a pattern/technology/architecture) 流行语(不是模式 / 技术 / 架构)
- A spectrum of solutions 一系列解决方案
- servers are managed by someone else 服务器是由别人管理的
- allow to scale up and down easily 可以很容易地上下调整
- pay for what you use (except for storage) 支付你使用的东西(除了储藏室)
- no administration 没有行政部门

Benifits of Serverless

- Low entry barrier 低进入门槛
- Cost efficient 成本效益
- High-availability and scalability 高可用性和可扩展性


What we will cover in this lesson

- What is serverless? 什么是无服务器？
- Function as a Service (FaaS) 函数即服务
- Simple functions and how to connect them to events 简单函数以及如何将它们连接到事件
- How functions are executed 如何执行函数
- Pros and Cons of using FaaS 使用 FaaS 的利弊

What are we going to build?

- Image sharing application 图片共享应用程序
- Images and groups 图片和群组
- A number of features 一些特性
  - REST API
  - React frontend
  - WebSockets 3
  - Authentication 认证
  - Scalable 可升级的
- Mostly serverless components 主要是无服务器组件

### Function as a Service

Serverless 核心组件

- FaaS : Function as a service: write code in individual functions and deploy them to a platform to be executed faas: 作为服务的功能: 在单个函数中编写代码，并将它们部署到一个要执行的平台上
  - AWS Lambda
  - Google Cloud Functions
  - Azure Functions
  - OpenWisk
- Datastores: Storage of data 数据存储: 数据的存储
  - AWS S3
  - AWS DynamoDB 
  - Google Firebase 
- Messaging: Send messages from one application to another 消息传递: 将消息从一个应用程序发送到另一个应用程序
  - AWS SQS
  - AWS Kinesis
  - Google Pub/Sub
- Services: Services that provide functionalities where we don't need to manage servers 服务: 提供我们不需要管理服务器的功能的服务，例如认证、机器学习、视频处理
  - authentication
  - ML
  - video processing
  - Big Data
  - Orchestration


Function as a Service

- Computed in the world of serverless
  - Split application into small functions
- Event driven 
- Pay per invocation
- Rest is handled by a cloud provider
  - Provisioning servers, scaling up and down
  - Reliability, autoscaling
  - Managing servers
  - Installing updates

Use-case for FaaS

- Mobile/web backends
- Real-time streaming
- Files processing

Lambda function vs AWS Lambda

请记住，AWS Lambda 是一个运行代码以响应来自 Amazon Web Services 的事件的计算服务，而 Lambda 函数是一个连接到在 AWS Lambda 运行的事件源的单个函数。


我们可以直接为 AWS Lambda 函数配置Amount of RAM, Function timeout

AWS Lambda limitations
- At most 3GB of memory per execution
- Functions can run no more that 15 minutes
- Can only write files to /tmp folder
- Limited number of concurrent executions
- Event size up to 6 MB

### AWS Lambda

Demo

- "Hello world" example 
- Learn how to deploy a function 
- Get familiar with Lambda service

steps:

- step1: Create function AWS -> Lambda -> Create function -> Author from scratch -> Create
- step2: Edit, Test and Save Function 

AWS took care of 

- Deploying our code 部署我们的代码
- Autoscaling 自动缩放
- Reliability 可靠性

### Events with AWS Lambda

### How FaaS works

### Invocation types

### JavaScript Callbacks

### Platform events

### Additional Parameters

### When to use serverless

***


## REST API

### API Gateway

### Amazon API Gateway

### API Gateway Configuration

### API Gateway Stages

### Implement GET-Groups API

### Web Interface : Introduction

### Using API from a Web Application

### Sending Request

### DynamoDB: Introduction

### DynamoDB: Storing Data

### Connecting API To DynamoDB

### Create Items with DynamoDB

### POST Method

### Routing in React

### Creating Group UI

### Advanced API Gateway

### API Gateway Pricing 

### API Gateway Limits

### Pagination: Exercise Solution




***

## Serverless Framework

### YAML

### Serverless Framework Application

### CloudFormation

### Using Serverless Framework

### Demo: Serverless Template

### Port Get All Groups Demo

### Demo: Group API

### Validate Requests

### Images API

### Queries With Node.js

### Demo: get images

### Indexes in DynamoDB 

### Exercise: Create image record


***

## Event Processing

### Uploading Files

### Cloudformation References

### Demo: presigned URL

### S3 Events

### WebSocket: Introduction

### API Gateway: WebSockets

### Websockets with Serverless Framework

### Full-Text Search

### DynamoDB Stream

### Decouple DynamoDB

### Scaling a Data Stream

### Elasticsearch

### Enable DynamoDB Stream

### Error Handing

### Simple Notification


 
***

## Authentication

### Authentication with API Gateway

### Implementing A Custom Authorizer

### Demo: Mock Authentication 

### Implementing Authentication

### OAuth and OpenID

### Oauth FLow

### Verifying JWT Token 

### Handling Auth0 JWT Token 

### Storing Secrets

### Lambda Middleware

***

## Best Practices

### Ports and Adapeters

### Integration Tests

### Local Execution

### Running Serverless Application Locally

### Canary Deployment

### Lambda Canary Deployments

### Configure Canary Deployment 

### Serverless Observability

### Distributed Tracing 

### Enabling X Ray Tracing 

### Optimize Lambda Function 

### Optimize Lambda Environment

### Demo: Optimize 

### Security

## Serverless Application

