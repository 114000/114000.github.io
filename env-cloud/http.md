---
title: HTTP
date: 2018-01-01
---

### HTTP methods

- GET: 从服务器获取资源 
  - `flowers` return a list of all flowers
  - `flowers/:id` return a specific car
  - status: `200` `404`
- POST: 向服务器提交资源 
  - `flowers` post a new flower
  - status: `201`
- PUT: 类似POST但用来替换资源
- DELETE - 从服务器上删除资源
  - `flowers/:id` delete a specific flower
  - status: `204`
- HEAD: 类似GET 但是只返回头部不返回内容
- OPTIONS: 获取资源的option一般用来嗅探服务器是否有该接口
- PATCH: 修改某个资源
  - `flowers/:id` update a specific flower
- TRACE: 执行消息回环

### RESTfull Best Pracitices

- Only use nouns and no verbs. They should be plural and consistent
- APIs should be versioned: `{{host}}/api/v0/cars/5`
- Lists shoud be paginated to limit the amount of data sent: `{{host}}/api/v0/cars/?offset=40&limit=10`
- All responses should attempt to use status codes
- All responses should include data format i.e. application/json
-  Error playloads should include

### Designing an API

- REST
  - Highly Popular
  - Easy to migrate endpoints
  - Easy to implement on modern platforms
  - Great for consumable APIs
- GraphQL
  - Super trendy
  - Great for complex relationships
  - Great for flexible data with thing like units
  - Super fun tooling


### Response HTTP Status

``` ts
export enum HttpStatus {
  continue = 100,
  switchingProtocols = 101,
  processing = 102,
  ok = 200,
  created = 201,
  accepted = 202,
  nonauthoritativeInformation = 203,
  noContent = 204,
  resetContent = 205,
  partialContent = 206,
  ambiguous = 300,
  movedPermanently = 301,
  found = 302,
  seeOther = 303,
  notModified = 304,
  temporaryRedirect = 307,
  permanentRedirect = 308,
  badRequest = 400,
  unauthorized = 401,
  paymentRequired = 402,
  forbidden = 403,
  notFound = 404,
  methodNotAllowed = 405,
  notAcceptable = 406,
  proxyAuthenticationRequired = 407,
  requestTimeout = 408,
  conflict = 409,
  gone = 410,
  lengthRequired = 411,
  preconditionFailed = 412,
  payloadTooLarge = 413,
  uriTooLong = 414,
  unsupportedMediaType = 415,
  requestedRangeNotSatisfiable = 416,
  expectationFailed = 417,
  iAmATeapot = 418,
  unprocessableEntity = 422,
  tooManyRequests = 429,
  internalServerError = 500,
  notImplemented = 501,
  badGateway = 502,
  serviceUnavailable = 503,
  gatewayTimeout = 504,
  httpVersionNotSupported = 505
}
```

### HTTP Public API

- [tushare 这是国内目前最大且唯一的*免费、开源的财经数据接口包。*在这里你可以找到股票、基金、期货、数字货币等行情数据，公司财务、基金等基本面数据，还有一些行业数据。](https://tushare.pro/document/1?doc_id=130)
- [marvel](https://developer.marvel.com/)
- [HTTP Cat](https://http.cat/)
- [public-apis 这个仓库收集免费的 API，已经有100多个了](https://github.com/toddmotto/public-apis)
- [全球假日 API](https://www.calendarindex.com/)
- [bing 壁纸接口](https://github.com/xCss/bing)
- [jsonstore.io - 通过 HTTP Header 读写 JSON 数据的免费 datastore。](https://github.com/bluzi/jsonstore)
- [chinese-xinhua - 新华字典数据库和 API，收录 14032 条歇后语，16142 个汉字，264434 个词语，31648 个成语。](https://github.com/pwxcoo/chinese-xinhua)
- [Pi API](https://pi.delivery/#apipi_get)
- [Last-Statement-of-Death-Row 美国得州的政府网站，有该州死刑犯的遗言数据库](https://github.com/wansho/Last-Statement-of-Death-Row)
- [开源语音数据库项目 Mozilla 基金会为了开发语音识别技术， 做了一个开源语音数据库项目，邀请全世界用户为这个数据库朗读句子，或者听他人的录音，判断朗读是否准确。](https://voice.mozilla.org/zh-CN/speak)
- [chinese-xinhua - 新华字典数据库和 API，收录 14032 条歇后语，16142 个汉字，264434 个词语，31648 个成语。](https://github.com/pwxcoo/chinese-xinhua)
- [Python 爬虫保存美国农业部网站的水果数据库 - 美国农业部为全世界已知水果制作了 7500 幅水彩证件照，并提供高清下载。作者讲述自己如何编写 Python 爬虫，抓取这些图](https://github.com/jwenjian/ghiblog/issues/114)
- [dead.io 一个显示你是否还活着的 API，做法是它每隔一段时间向你发一封邮件，如果你连续多次没有回复，它就认为你已经死了。你可以通过这个 API，设置一些死了以后需要触发的动作。](https://dead.io/)
- [akshare - 一个基于 Python 的开源金融数据接口库，目的是实现股票、期货等金融产品从数据采集、数据清洗到数据下载的工具，满足金融数据科学家、数据科学爱好者在数据获取方面的需求。](https://github.com/jindaxiang/akshare)
- [货币汇率 API - 该网站提供免费货币汇率的 JSON API。](https://currencyscoop.com/)
- [几何艺术占位符图像 - 该网站提供占位符图像（Placeholder），图像内容是算法生成的几何图形。](https://generative-placeholders.glitch.me/)
- [Branca - 一种安全令牌的数据格式，比 JWT 更安全](https://branca.io/) 同类项目还有 [Paseto](https://paseto.io/)
- [Base API - 这家云服务公司提供基本的 Web API，包括身份验证、电子邮件发送、文件和图像存储。用法简单，容易上手，作为概念产品很不错。](https://www.base-api)
- [Lorem Picsum - 只要在我们的 URL 后面添加你想要的图像大小(宽度和高度) ，你就会得到一个随机的图像。](https://picsum.photos/)


### CDN

- [前端公共库CDN加速](http://www.cdnjs.net/)前端cdn
- [bootCDN](http://www.bootcdn.cn/)前端cdn
- [为什么静态资源应该使用 CDN？](https://forestry.io/blog/for-static-sites-theres-no-excuse-not-to-use-a-cdn/)
- [CDN 提供商2019介绍 该文介绍了全球25家 CDN 服务提供商，并提供简单的测评。](https://haydenjames.io/best-cdn-providers/)
- [CDNPerf 这个网站通过请求速度，比较各大 CDN 的性能表现](https://www.cdnperf.com/)

### HTTP resources

- [QUIC 协议的注意事项 本文介绍了 QUIC 协议的一些优点。作者提出，QUIC 与其称为 HTTP/3，不如称为 TCP/2。](https://blog.erratasec.com/2018/11/some-notes-about-http3.html)
- [http3-explained curl 作者写的小册子，介绍 HTTP/3 协议。此前，他也写了介绍 HTTP/2 的小册子。](https://github.com/bagder/http3-explained)
- [不必要的 HTTP 头信息](https://www.fastly.com/blog/headers-we-dont-want)
- [HAProxy 的防 DDOS 机制 - HAProxy 是一个负载均衡服务器，自带过滤 HTTP 请求的功能，可以防止应用层的 DDOS 攻击，这方面比 nginx 更强大。](https://www.haproxy.com/blog/application-layer-ddos-attack-protection-with-haproxy/)
- [图解 DNS over HTTPS](https://hacks.mozilla.org/2018/05/a-cartoon-intro-to-dns-over-https/)
- [HTTP Toolkit - 这个工具可以拦截和查看 HTTP/HTTPS 请求，并且可以 mock 服务器的回应。](https://httptoolkit.tech/mock)
- [安全相关的 HTTP 头信息介绍](https://nullsweep.com/http-security-headers-a-complete-guide/)
- [HTTP 头信息的安全设置 - ](https://int64software.com/blog/2018/11/05/hardening-website-security-part-1-http-security-headers/)
- [不必要的 HTTP 头信息 - 本文统计了30个最常见的 HTTP 头信息，逐个讨论哪些是必要的，哪些是没必要的。](https://www.fastly.com/blog/headers-we-dont-want)
- [浏览器的 gRPC 协议支持](https://grpc.io/blog/state-of-grpc-web)
- [gRPC-Web - gRPC-Web 是一个JavaScript客户端库，使 Web 应用程序能够直接与后端gRPC服务通信，不需要 HTTP 服务器充当中介。这意味着可以构建真正的端到端 gRPC 应用程序体系结构。](https://www.cncf.io/blog/2018/10/24/grpc-web-is-going-ga/)
- [HTTP 协议简史](https://hpbn.co/brief-history-of-http/)
- [新的 HTTP 头字段 Feature-Policy](https://scotthelme.co.uk/a-new-security-header-feature-policy/) 
- [TLS 1.3 介绍 - HTTPS 协议的最新版本 TLS 1.3，最近成为了国际标准 RFC 8446。本文详细介绍这个新协议，包括 TLS 1.2 的缺陷，以及 TLS 1.3 如何解决它。](http://blog.cloudflare.com/rfc-8446-aka-tls-1-3/) 
- [mkcert - 生成本地 HTTPS 加密证书的工具，一个命令就可以生成证书，不需要任何配置。图片是就是它默认为 localhost 生成的加密证书。](https://github.com/FiloSottile/mkcert) 
- [HTTPS 协议图解](https://tls.ulfheim.net/)
- [DNS over TLS 的 Node 客户端 - 为了提高安全性，防止监听，DNS 查询已经可以在 HTTPS 协议上完成。这篇文章教你怎么写一个 Node 客户端，获取 DNS 信息。](https://sagi.io/2018/09/dns-over-tls---thoughts-and-implementation/)
- [实用的 RESTful API 最佳实践 - 本文介绍了20多个 RESTful API 的最佳实践。](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
- [静态网站为什么需要 HTTPS- 本文总结了对 HTTP 网页进行攻击的方法。](https://www.troyhunt.com/heres-why-your-static-website-needs-https/)

- [GitHub 的官方 RSS Feed](https://www.ronaldsvilcins.com/2020/03/26/rss-feeds-for-your-github-releases-tags-and-activity/)

- [中文谣言数据 2018.12.24](https://github.com/thunlp/Chinese_Rumor_Dataset)