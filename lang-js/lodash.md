---
title: lodash
date: 2018-08-03
tag:
- javascript
- functional

# writing: true
---

[[toc]]



## 转换

``` js

_.countBy 
  _.countBy([6, 4, 6] /*, v2k => v2k*/) // => {"6": 2,"4": 1 }

_.groupBy
  _.groupBy([6, 4, 6] /*, v2k => v2k*/) // => { '4': [4], '6': [6, 6] }

_.keyBy
  _.groupBy([6, 4, 6] /*, v2k => v2k*/) // => { '4': 4, '6': 6 }

_.fromPairs 
  _.fromPairs([['fred', 30], ['barney', 40]]) // => { 'fred': 30, 'barney': 40 }

// 转置
_.zip
  _.zip(['fred', 'barney'], [30, 40], [true, false]) // => [['fred', 30, true], ['barney', 40, false]]

_.unzip
_.unzip([['fred', 30, true], ['barney', 40, false]])
// => [['fred', 'barney'], [30, 40], [true, false]]

```

## 降维

``` js
_.flatten
_.flattenDeep
_.flattenDepth
_.intersection([2, 1], [4, 2], [1, 2]); 交集 // => [2]
_.xor([2, 1], [2, 3]) // => [1, 3]
_.union
```

## 升维
``` js
_.chunk
```

## 过滤 

``` js
_.uniq       _.uniq([2, 1, 2])               [2, 1]       // 去重 
_.sortedUniq([1, 1, 2]);


_.compact    _.compact([0, 1, false, 2, '', 3])           // 去除假值 false, null, 0, "", undefined, 和 NaN                       
_.without    _.without([2, 1, 2, 3], 1, 2)   [3]          // 排除 
_.pull       _.without([2, 1, 2, 3], 1, 2)   [3]          // 排除(改变原数组)

_.difference _.difference([3, 2, 1], [4, 2]) [3, 1]       // 排除
_.pullAll    _.pullAll([3, 2, 1], [4, 2])    [3, 1]       // 排除(改变原数组)

_.pullAt // 根据索引删除元素 改变数组

_.remove // 改变数组
_.filter

_.pick       _.pick({ 'a': 1, 'b': '2', 'c': 3 }, ['a', 'c'])
_.omit       _.omit({ 'a': 1, 'b': '2', 'c': 3 }, ['a', 'c'])
```

## format 

```js
_.fill
_.map
_.reverse
```



## 类型转换

```
_.toArray                 
  Array DomCollection Uint8Array String Buffer Object[...value]
  其他返回 [] Number Null etc.
```

## 检索

``` js
_.find
_.findLast
_.max
_.head[_.first]
_.last
_.nth(array, 1)
_.indexOf(array, value, [fromIndex=0])
_.lastIndexOf([1, 2, 1, 2], 2, 2)

```

## 切片

``` js
_.tail(array)          _.slice(array, 1)
_.drop(array, n)       _.slice(array, n)
_.dropRight(array, n)  _.slice(array, 0, -n)

_.initial(array)       _.slice(array, 0, -1)
_.take(array, n)       _.slice(array, 0, n)
_.takeRight(array, n)  _.slice(array, -n)


_.slice(array, [start=0], [end=array.length])
```

## 判定

```js
// 数组相关
_.isArray(Array.isArray)  判定 Array 
_.isArrayLike             判定 Array DomCollection Buffer Uint8Array String 
_.isArrayLikeObject       判定 Array DomCollection Buffer Uint8Array
_.isArrayBuffer           判定 ArrayBuffer
_.isBuffer //false??

```

## 随机

``` js

_.shuffle    _.shuffle([1, 2, 3, 4])     乱序
_.sample     _.sample([1, 2, 3, 4])      随机抽取一个
_.sampleSize _.sampleSize([1, 2, 3], n)  随机抽取n个 n 默认为1
_.ramdom     _.random([lower=0], [upper=1], [floating])
```


## 比较

```
_.eq:  相等，值比较
_.gt:  大于
_.gte: 大于等于
_.lt:  小于
_.lte: 小于等于

均返回布尔值，而且只有两个参数
```


## un

_.join
_.sortedIndex





