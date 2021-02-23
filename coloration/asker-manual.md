---
title: 'Asker Manual'
date: 2020-01-01
categories:
- [文档, Coloration]
---

@coloration/asker manual

- Github: <https://github.com/coloration/asker>
- document above:

<!-- more -->

<div style="display: flex;">
  <img src="https://img.shields.io/npm/v/@coloration/asker.svg" alt="version">
  <img src="https://img.shields.io/npm/l/@coloration/asker.svg" alt="lic">
  <img src="https://img.shields.io/npm/dm/@coloration/asker.svg" alt="Download">
  <img src="https://img.shields.io/bundlephobia/min/@coloration/asker@0.9.0" alt="min">
  <img src="https://img.shields.io/bundlephobia/minzip/@coloration/asker@0.9.0" alt="minzip">
</div>


## Startup

### Install

``` html
<script src="https://raw.githubusercontent.com/coloration/asker/master/dist/index.js"></script>
<script>
var Asker = asker.Asker
Asker.get('http://api.io`')
</script>
```

or


```bash
$ yarn add @coloration/asker -S
# or
$ npm i @coloration/asker -S
```

### Use

> JavaScript

``` js
import { Asker } from '@coloration/asker'


Asker.get('http://api.io/list', { page: 1, size: 20 })
```

> TypeScript

```ts
import { Asker } from '@coloration/asker'

type FooDto {
  page: number, limit?: number, offset?: number
}

Asker.get<FooDto>('http://api.io/list' { page: 1 })
```

## Instance

You can initialize to cache some configure

``` js
import { Asker } from '@coloration/asker'

const api = new Asker({
  baseUrl: 'http://api.io'
})

api.get('/list', { page: 1, size: 20 })
api.post('/article', { title: 'a article', content: 'write ...' })
```

This is a detail configure for Asker, there are some example for configure after this:

``` ts
export interface AskerConf {
  /** a sub url, it will be added after `baseUrl` at last */
  url?: string,
  
  /** the url first part */
  baseUrl?: string,
  
  /** the string result */
  query?: string,
  
  /** the transferred object for post  */
  body?: any,
  
  /** if you need to set the query string when you call the post like methods, 
   * you could set this  */
  params?: { [key: string]: any },
  
  /** request method, will be override when you invoke instance[method] */
  method?: 'get' | 'option' | 'head' | 'post' | 'put' | 'patch' | 'delete',
  
  /** request headers */
  headers?: { [key: string]: any }

  /** will cache response after first (getLike) request, 
   * second will return the cache */
  getCache?: boolean

  /** asker will change the data type auto by this */
  postType?: 'json' | 'form-data' | 'text' | 'form-urlencoded',
  
  /** default 'object' will call 'JSON.parse()', other return string */
  responseType?: 'object' | 'text',
  
  /** waiting over timeout(MS), asker will call the 'onTimeout' or 'reject' */
  timeout?: number,

  /** set `XMLHTTPRequest` withCredentials */
  withCredentials?: true,

  /** custom validator, default is `status >= 200 && status < 300` */
  validator?: (status: number) => boolean,

  /** custom adapter: you can replace default xhr adapter, `Asker.jsonp` is 
   * implemented by this way。 it also can be used in mock, you can pass a 
   * data (except `undefined`), it will return a response wrapped by 
   * `AskerResponse` object. Or you pass a function return a custom data
  */
  adapter?: string | number | boolean | { [key: string]: any } | any[] |
    ((response: any, defaultResponse: AskerResponse) => Promise) | 
    ((response: T, defaultResponse: AskerResponse) => Promise)
  ,
  
  /** hook chain change the `AskerConf` before the request  */
  before?: (conf: AskerConf) => AskerConf | ((conf: AskerConf) => AskerConf)[],
  
  /** hook chain change your resopnse after the request */
  after?: (response: any) => any

  /** called when xhr trigger `error` event */
  onError?: (errType: string, xhr: XMLHttpRequest, conf: AskerConf) => any,

  /** called when xhr trigger `abort` event */
  onAbort?: (errType: string, xhr: XMLHttpRequest, conf: AskerConf) => any,

  /** called when xhr trigger `timeout` event */
  onTimeout?: (errType: string, xhr: XMLHttpRequest, conf: AskerConf) => any,

  /** called when xhr trigger `upload.progress` event */
  onUploadProgress?: (e: ProgressEvent, xhr: XMLHttpRequest, conf: AskerConf) => any,
  
  /** called when xhr trigger `progress` event */
  onDownloadProgress?: (e: ProgressEvent, xhr: XMLHttpRequest, conf: AskerConf) => any

  /** cancellion */
  canceler?: Canceler

  /** other custom props */
  [key: string]: any
}
```

## Methods

### Normal

``` js
import { Asker } from '@coloration/asker'

Asker.get('http://api.io', { page: 1, size: 20 })
Asker.post(
  'http:/api.io/article', 
  { content: 'write ...'},
  { 
    query: 'title=article' 
    // or
    params: { title: 'article' }
  }
)
```

all methods:

post like: `post` `patch` `put`

get like: `get` `delete` `options` `head`


### JSONP

the `jsonp` field get from backend developer or document of the origin server. JSONP is a outdate way to handle the across origin.

``` js
Asker.jsonp(
  'http://api.io/jsonp', { page: 1, size: 20 }, { jsonp: 'jsoncallback' }
)

// or change callback name in 2rd parameter 
Asker.jsonp(
  'http://api.io/jsop?page=1&size=20', 'jsoncallback'
)
```

### Batch Requests

```js
Asker.batch(
  'http://api.io/upload', 
  // an array or a normal param
  [{ file: file1 }, { file: file2 }], 
  { 
    method: 'post',
    // max number of batchs in same tile, default is the array length
    slice: 3,
    // retry times of a batch when request failure, default is 0 times
    retry: 2
  }
)
// apply the Promise.all for these requests
.then(allResponses => {})
```

### Custom Adapter & Mock

The `jsonp` and `batch` methods are implemented by `adpater`. You also could implement some other methods. Other platforms, for example, miniprogram, the enviorment support JavaScript, but not support `XMLHTTPRequest`.

``` js
export function get (url, params, conf) {
  return Asker.get(url, params, Object.assign(conf, {
    adapter (conf) {
      // ...
      return wx.http(/* ... */)
    }
  }))
}
```

#### Uniapp Request Example 

``` js
import { Asker } from '@coloration/asker'

function uniappRequestAdapter (conf, defRes) {
  return new Promise((resolve, reject) => {
    uni.request({
      url: conf.uri,
      method: String(conf.method).toUpperCase(),
      data: conf.body,
      success (response) {
        defRes.statusCode = response.statusCode
        defRes.data = response.data

        response.statusCode === 200 ? resolve(defRes) : reject(defRes)
      },
      fail: reject
    })
  })
}

// demo 1
const api = new Asker({ 
  adapter: uniappRequestAdapter
})

// demo 2: WARN!: global override
Asker.adapter = uniappRequestAdapter
const api = new Asker()
```

You are mocking when you return a data in the `adapter` function instead of the promise. You could also pass a normal data to `adapter`.

```js
Asker.get('whatever string', whateverParam, {
  adapter: [1, 2, 3]
})
.then(response => {}) // [1, 2, 3]
}
```

## Features

> some differences from other request tool

### Cache responses for Getlike methods

When we spec `getCache : true` in configure，Asker hold the response in `Asker.cache` object with the url and query until you reload the browser.

When we send requests with the same url, params and getCache configure field, Asker will find from the `Asker.cache` firstly. Inexsitly, will request.

Note: the response will be save after `after` pipe. so you don't need format it every time.

``` js
// request
Asker.get('http://api.io/config', { type: 1 }, { getCache: true })
.then( => {
  // find response from cache
  return Asker.get('http://api.io/config', { type: 1 }, { getCache: true }) 
})

// request
Asker.get('http://api.io/config', { type: 2 }, { getCache: true }) 


```

from `0.9.0` you could spec `getCache` with a number. the respose will be hold number seconds.

``` js
function cacheFetch () {
  return Asker.get('http://api.io/config', { type: 1 }, { 
    getCache: 3, adapter: Math.random() 
  }) 
}

cacheFetch().then(num => { /* 0.540440389323092  */})

setTimeout(() => {
  cacheFetch().then(num => { /* 0.540440389323092  */})
}, 3000)

setTimeout(() => {
  cacheFetch().then(num => { /* 0.8885207860889037  */})
}, 3001)
```

### Post Type

Asker will transform the body type when you set the postType field. Default is `json`

```js
Asker.post(
  'http://api.io/upload', 
  { file: file, name: 'photoname' },
  { postType: 'form-data' }
)
.then(res => {})
```

### Cancel Request

after called the cancel methods, we will receive an error in promise.catch or conf.onAbort method.

```js
import { Asker, Canceler } from '@coloration/asker'

const canceler = new Canceler()

Asker.get('http://api.io/eg1', null, { canceler })
Asker.get('http://api.io/eg2', null, { canceler })

canceler.cancel()
```

### Timeout

if response timeout, we will receive an error in `promise.catch` or `conf.onTimeout` method.

```js
Asker.get('http://api.io/test-timeout', null, { 
  timeout: 3000,
  onTimeout: (error, xhr, conf) => {}
})

Asker.get('http://api.io/test-timeout2', null, { timeout: 3000 })
.catch(error => {
  const { status, message } = error

  status === 0
  message === Asker.errorType.TIMEOUT
})
```
