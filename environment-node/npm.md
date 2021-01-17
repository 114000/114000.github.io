---
title: package.json & npm & yarn

---

[[toc]]

### 通过版本号安装包

- 指定版本: `$ npm i your-package@1.12.5`
- 指定范围: `$ npm i your-package@">=1.12.5 <1.13.0"`


## npm flow

### npm 发布包

1. 切换 npm官方源(或者自己的源) `$ npm config set registry http://registry.npmjs.org/`
2. 登录并输入信息:  `$ npm login`
3. 发布: `$ npm publish --access public`

### npm 切换源

- 淘宝源: `$ npm config set registry https://registry.npm.taobao.org`
- 官方源: `$ npm config set registry http://www.npmjs.org`

### npm(nrm) 切换源

1. 安装nrm `$ npm i nrm -g`
2. 查看可使用的源 `$ nrm ls`
3. 切换源 `$ nrm use taobao`

---

## package.json 版本号约束

- `1.12.5`: `1.12.5`
- `^1.12.5`: <2.0.0
- `~1.12.5`: <1.13.0

## package.json 为命令添加软连接

``` json
// package.json
{
  // ...
  "scripts": {
    "build": "./node_modules/.bin/webpack"
  }
}
```

运行

```bash
$ npm run build
$ yarn build
```


---

## yarn startup

### yarn 安装

- linux (CentOS)
1. 下载 `$ wget https://github.com/yarnpkg/yarn/releases/download/v1.7.0/yarn-v1.7.0.tar.gz`
2. 解压 `$ tar -zxvf yarn-v1.7.0.tar.gz -C /usr/local/src`
3. 添加软连接 `$ ln -s /usr/local/src/yarn-v1.7.0/bin/yarn /usr/bin/yarn`

### yarn 升级

- MacOS: `$ brew update yarn`



## yarn flow


### yarn 切换源

- 淘宝源: `$ yarn config set registry https://registry.npm.taobao.org`
- 官方源: `$ yarn config set registry https://registry.yarnpkg.com`

### yarn 清除缓存

``` bash
$ yarn cache clean
```


- [package.json 大数据分析](https://medium.com/warsawjs/state-of-package-json-dependencies-de99828b6c3f)
- [如何通过 npm 窃取信用卡密码？](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5) 
