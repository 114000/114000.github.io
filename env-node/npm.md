# node包管理(npm/package/yarn)

<!-- more -->

## npm 命令

### 安装包 install | i | add


|cmd|description|demo|
|:---|:---|:---|
|`npm i` |初始化项目|- `git clone <project> & cd $_` <br /> - `npm i` |
|`npm i [<@scope>/]<pkg>` |安装最新版本npm包|- `npm i react -S` <br /> - `npm i @vue/cli -g`|
|`npm i [<@scope>/]<pkg>@tag`||`npm i vue-demi@lastest` |
|`npm i [<@scope>/]<pkg>@<version>`|指定版本|`$ npm i jquery@3.5.1`|
|`npm i [<@scope>/]<pkg>@<version range>`|指定版本范围|`$ npm i jquery@">=1.11.0 <2.0.0"`|

**args**

`[--save-prod|--save-dev|--save-optional] [--save-exact] [--no-save]`

|arg|alias|position|desc|
|:---|:---|:---|:---|
|`--global`|`-g`|1|忽略项目全局安装|
|`--save-prod`(默认)|`--save`, `-S`|1|保存到 `package.json/dependencies`|
|`--save-dev`|`-D`|1|保存到 `package.json/devDependencies`|
|`--save-optional`|`-O`|1|保存到`package.json/optionalDependencies`|
|`--save-exact`|`-E`|2|安装精确版本|
|`--no-save`||2|不会记录到 `package.json`, 也无法用 `npm ls` 查出来，但是可以被`npm uninstall`卸载|

!> 一个包只能安装在 `dependencies`, `devDependencies`, `optionalDependencies`, `peerDependencies` 其中一个位置上


### 卸载包 uninstall | un | unlink | remove | rm | r


**args** 

`npm uninstall [<@scope>/]<pkg>[@<version>]...`

`[--save-prod|--save-dev|--save-optional] [--no-save]`


!> `--no-save` 只会删除包，不会修改 package.json

!> 其他参数都无效，无论依赖添加在哪里都会从 package.json 删除


### 更新包 update | up | upgrade


`npm update [-g] [<pkg>...]`

> 根据**版本号约束规则**进行更新 


### 发布包 publish


1. 切换 npm官方源(或者自己的源) `$ npm config set registry http://registry.npmjs.org/`
2. 登录并输入信息:  `$ npm login`
3. 发布: `$ npm publish --access public`

## 版本号

### 版本号表示

- `0.0.1-alpha.1`
- `0.0.1-beta.1`
- `0.0.1-rc.1`
- `0.0.1`

### 版本号约束

> `major`.`minor`.`patch` 主版本号·次版本号·修补版本号

|类型|含义|例子|
|:---|:---|:---|
|`major.minor.patch`|固定版本 `-E`|`1.12.5`|
|`^major.minor.patch`|锁定左侧第一个非零版本(默认)|- `^1.12.5`: `<2.0.0` <br /> - `^0.2.0`: `<0.3.0` <br /> - `^0.0.17`: `0.0.17`|
|`~major.minor.patch`|只允许更新patch版本|- `~1.12.5`: `<1.13.0`|

**举例**

``` js
{
  "dist-tags": { "latest": "1.2.2" },
  "versions": [
    "1.2.2", "1.2.1", "1.2.0",
    "1.1.2", "1.1.1",
    "1.0.0",
    "0.4.1", "0.4.0",
    "0.2.0"
  ]
}

// package: ^1.1.1 => 1.2.2
// package: ~1.1.1 => 1.1.2
// package:  1.1.1 => 1.1.1
// package: ^0.2.0 => 0.2.0
// package: ^0.4.0 => 0.4.1
```


### npm 切换源

**npm**

- 淘宝源: `$ npm config set registry https://registry.npm.taobao.org`
- 官方源: `$ npm config set registry http://www.npmjs.org`

**npm with nrm**

1. 安装nrm `$ npm i nrm -g`
2. 查看可使用的源 `$ nrm ls`
3. 切换源 `$ nrm use taobao`
4. 添加源 `$ nrm add <name> <protocol://address>`
5. 删除源 `$ nrm delete <name>`
6. 源测速 `$ nrm test`

---


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

## yarn 命令

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
