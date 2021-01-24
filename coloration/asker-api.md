---
title: 'Asker API'
date: 2020-01-01
categories:
- [文档, Coloration]
---

自己开发的 web HTTP 请求工具。 

- 项目地址Github: <https://github.com/coloration/asker>

- 下面是文档

<!-- more -->

## Static Methods / Instance Methods

``` js
import { Asker } from '@coloration/asker'

Asker.get()
```

- get: `<T = any>(url: string, params?: any, conf?: AskerConf) => Promise<T>`
- delete: `<T = any>(url: string, params?: any, conf?: AskerConf) => Promise<T>`
- head: `<T = any>(url: string, params?: any, conf?: AskerConf) => Promise<T>`
- option: `<T = any>(url: string, params?: any, conf?: AskerConf) => Promise<T>`

- post: `<T = any>(url: string, body?: any, conf?: AskerConf) => Promise<T>`
- put: `<T = any>(url: string, body?: any, conf?: AskerConf) => Promise<T>`
- patch: `<T = any>(url: string, body?: any, conf?: AskerConf) => Promise<T>`

- jsonp: `AskerJsonpConf` extends `AskerConf`. an addition option is `jsonp`. It's will be specitied with callback function name. like `callName`
  - `<T = any>(url?: string, params?: any, conf?: AskerJsonpConf): Promise<T>`
  - `<T = any>(url?: string, callName?: string, conf?: AskerJsonpConf): Promise<T>`

- batch: `AskerBatchConf` extends `AskerConf`. `slice` option means, how much requests in one batch will be send. `retry` option means, how many times to retry when the request fail.
  - `<T = any>(url?: string, paramsOrbody?: any[], conf?: AskerBatchConf): Promise<T>`




## Helper 

### query2Object

`(obj: { [key: string]: any }, encode = false) => string`

- format plain object to query string witch like `window.location.search`. But it does not have `?` chat.
- `encode`: if spec it `true`, it will transform every `**value**` with `encodeURIComponent`. Default is `false`.


### object2Query

`<T = any> (query: string, raw = false) => T`

- format query string to object. every chat before the first `?` will be discarded. Included the `?`.
- `raw`: if spec it `true`. the `**value**` will be format with `JSON.parse`. string number will be number, string boolean will be boolean, and so on.


### splitBlob

`(fileOrblob: Blob, piece: number): Blob[]`

- split the file or blob with piece. The function will return one Blob Array. Its' length is `Math.ceil(Blob.size / piece)`


### HTTP Status Code

from 0.8.0

> define

```ts
// copy from nestjs
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

> use

``` js
import { HttpStatus } from '@coloration/asker'
```