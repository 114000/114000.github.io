---
title: 'Hooks API'
date: 2020-01-01
categories:
- [文档, Coloration]
---

a library of React Hook Utils

- 项目地址Github: <https://github.com/coloration/hooks>

- 下面是文档

<!-- more -->

<div style="display: flex;">
<img src="https://img.shields.io/npm/v/@coloration/hooks.svg" alt="version">
<img src="https://img.shields.io/npm/l/@coloration/hooks.svg" alt="lic">
<img src="https://img.shields.io/npm/dm/@coloration/hooks.svg" alt="Download">
</div>

## Start Up

### Install

``` bash
$ npm i @coloration/hooks -S
```

## API

### HookStore[class]


简易的状态管理 Hooks. 没有设计 Action 层. 如果有需要可以使用 `useStore` 进行下一层封装, 或者继承 ReactStore 进行拓展, 实例内部只是缓存了 `store<T>`, `listeners`, `mapCache`. 

不像之后的 hooks 具有唯一性, hookStore 以类的方式实现, 以增加了复用性.

``` ts
interface ISomeContainerStore {
  isLogin: boolean
  userInfo: IUserInfo
}

const { useStore } = new ReactStore<ISomeContainerStore>({ isLogin: false }, true)
// or
const { useStore } = UseStoreFactory.create<ISomeContainerStore>({ isLogin: false }, true)


interface IContainerMapStore {
  loginStatus: boolean
  user: IUserInfo
}

Container = () => {
  /**
   * if you need a reactive value, must spec a map function, useStore will 
   * decide trigger or not with returned value of the map function every time.
   */
  const { store, updateStore } = useStore<IContainerMapStore>(
    (s) => ({ loginStatus: s.isLogin, user: s.userInfo })
  )

  // reactive value
  store.loginStatus
  store.user

  // else you don't need reactive values, only update them.
  const { updateStore } = useStore()

  updateStore({ isLogin: true })
}
```

### useI18n 


``` tsx

const i18nLocale = {
  [I18nLanguages.ZH_CH]: { '$你好': '你好' },
  [I18nLanguages.EN_US]: { '$你好': 'hello' },
}

function Demo () {
  const [globalLocale] = useI18nLocale()
  return <div>{ globalLocale['$你好'] }</div>
}

function Demo2 () {
  const [locale] = useI18Locale({
    [I18nLanguages.ZH_CH]: { '$你好': '您好' },
    [I18nLanguages.EN_US]: { '$你好': 'hola' },
  })
  return <div>{ globalLocale['$你好'] }</div>
}

function Demo3 () {
  const { lang, setlang } = useLang()
  return (
    <Fragment>
      <Button onClick={() => setLang(I18nLanguages.ZH_CH)}>中文</Button>
      <Button onClick={() => setLang(I18nLanguages.EN_US)}>English</Button>
    </Fragment>
  )
}

<I18nProvider locales={props.i18nLocale}>
  <Demo />
  <Demo2 />
</I18nProvider>
```


### useLocalStorage 

``` js
const [localStorageA, setLocalStorageA] = useLocalStorage('A', { a: 1 }, true)
// localStorage.getItem('A') => '[object Object]'

const [localStorageB, setLocalStorageB] = useLocalStorage('B', { b: 1 })
// localStorage.getItem('B') => '{"b": 1}'
```


### useLocationQuery 

``` js
// http://api.io?a=1&b=2&c=3

const [query, setQuery] = useLocationQuery()

query.a // 1
query.b // 2
query.c // 3

setQuery({ a: 1, b: 2, c: 4 })
setQuery({ c: 4 }, true/* partial */)

// http://api.io?a=1&b=2&c=4

```

### useCookie

```js
// developing
```

### useWindowEvent

``` js
// developing 
useWindowEvent('resize', () => {
  // ...
}, [])
```