---
title: Full Stack Apps on AWS
---

## Cloud Base

Tightly Coupled

Tightly Coupled systems are **quick to stand-up**, but may result in higher **Technical Debt**

Loosely Coupled

Loosely coupled systems require **more time upfront** but are generally easier to improve upon.

Technical Debt

The cost (in time and resources) of additional code rework caused by choosing an easy solution now instead of using a better approach that would take longer to implement.

现在选择一个简单的解决方案而不是使用一个需要更长时间才能实现的更好的方法所导致的额外代码返工的成本(在时间和资源上)。

它本质上是一个抽象的测量, 用来衡量未来我们会遇到多少问题.


URL

- protocol: e.g. https:// http:// file:// ftp:// etc.
  - SSL(Secure Socket Layer)
  - TLS(Transport Layer security)
- domain: This basically tell the system where we want to route traffic to.
  - subdomain
  - domain
- path: the server exactly which resource we are trying to get
- port: what network port to route the traffic through such as `80`, `8080`, `5432`
- file extension: what type of file e.g. `.html` `.php` 
- query parameters: which are variables they can pass along with html or fragment


NoSQL: 
- Simple Key:Value Stores
- is easily scaled OUT
- is great if you are designing as you go

SQL(Structured Query Language)
- primary key / foreign key


signed URL 设计模式, 提供客户端直接上传 FileStore 节省服务器资源.
请求服务端获得 URL, 再通过 URL 进行读写

### Storing Data in the Cloud

#### Provisioning a Cloud Database

每个SQL框架都有自己的方言


### User Authentication and Security

> Authentication = Who Is Asking(认证), Authorization = Can They Ask(授权)

```
Authentication
|
Authorization
```

What is the Current Gold Standard (or best method) of storing passwords
- As salted, hashed strings using bcrypt


```ts
import * as bcrypt from 'bcrypt'
const plainTextPassword = 'SirCatFace'


// register or change password
const saltRounds = 10

// 2 ^ 10
const salt = await bcrypt.genSalt(saltRounds)
const hash = await bcrypt.hash(plainTextPassword, salt)

// login
const compare = await bcrypt.compare(plainTextPassword, hash)

```

<https://jwt.io>

``` ts
import * as jwt from 'jsonwebtoken'

const token = jwt.sign(user, config.jwt.secret)
```

#### Examples of Good Security Policies

- [NPM 国家预防控制中心](https://www.npmjs.com/policies/security)
- [Nylas 女名女子名](https://www.nylas.com/security/)
- [AWS 自动气象站](https://aws.amazon.com/security/)


``` ts
import { spawn } from 'child_process'

const pythonProcess = spawn('python3', ['src/image_filter.py'])

if (pythonProcess !== undefined) {
  pythonProcess.stdout.on('data', data => {
    
  })
}
```