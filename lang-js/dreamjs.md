---
title: 使用 Dreamjs 生成 JSON 数据
date: 2018-07-10
tag:
- jslib

---

[[toc]]

## 基本使用

github: <https://github.com/adleroliveira/dreamjs>

``` bash
$ yarn add dreamjs -D

# or 

$ npm i dreamjs -D
```

``` js
import dream from 'dreamjs'

dream.schema({name: 'name'}).generateRnd().output()
// { name: 'Sam Nichols' }

dream.schema({name: 'name'}).generateRnd(2).output()
// [ { id: 'Maria Porter' }, { id: 'Evan Santiago' } ]
```

## 类型

### 基础的类型

``` js
dream.schema('String', { result: String })
dream.schema('Number', { result: Number })
dream.schema('Boolean', { result: Boolean })
dream.schema('Array', { result: Array })
dream.schema('Object', { result: Object })
dream.schema('Function', { result: Function })
dream.schema('Date', { result: Date })
```

### 自定义类型

有两种可以自定义类型的方式

1. 直接写正则表达式

dreamjs 依赖 [randexp](https://github.com/fent/randexp.js) 实现正则表达式的转换

``` js
dream.schema('order', {
  orderId: /[A-Z]{3}[0-9]{4,10}/,
  state: /(1|2)/,
  image: /http:\/\/www\.\w{6}\.(com|cn|cc)\/\w{4,10}\.(png|jpg|gif)/
})
.generateRnd()
.output()

/*
{ 
  orderId: 'YCX85258',
  state: '1',
  image: 'http://www.0unc5Z.cn/9HQTx.gif' 
}
*/
```

2. 使用 dream.customType 方法

``` js
// 自增id
// 需要注意的是`自增id`依赖上一个项目的 id 字段，也就是说 key 必须为 id 才能使用 'plusId' 这个类型
dream.customType('plusId', helper => {
  return helper.previousItem ? helper.previousItem.id + 1 : 1
})

// 工作日
// oneOf 是helper 的内置函数，内部使用 lodash 中的 sample 函数来随机获取集合中的一个元素
// _.sample <https://www.lodashjs.com/docs/4.17.5.html#sample>
dream.customType('businessDays', helper => {
  return helper.oneOf(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
})

dream.schema({
  id: 'plusId',
  day: 'businessDays'
})
.generateRnd(3)
.output()

/*
[ { id: 1, day: 'Wednesday' },
  { id: 2, day: 'Tuesday' },
  { id: 3, day: 'Tuesday' } ]
*/
```

helper 中另一个内置属性是 helper.chance 它是 chance 库的实例，使用方法在下方预定义类型中有介绍

### 预定义的类型

有很多比较常用的模板比如城市（city），年龄（age）这些东西，dreamjs 在内部引用了 [`chance`](http://chancejs.com/index.html) 库来实现。比如

``` js
const personSchema = dream.schema('person', {
  name: 'name',
  city: 'city',
  age: 'age'
  // ...
})
```

但需要注意的是，dreamjs 默认只能使用 `chance` 库原型链方法的无参形式

``` js
temporaryValue = (typeof (chance[propertyType]) === 'function') ? 
                 chance[propertyType]() : 
                 '[Unknown Custom Type]';
```

如果要使用 `chance` 高级功能，可以在customType 中的 helper 中访问到 `chance`

``` js
dream.customType('childrenAge', helper => helper.chance.age({ type: 'child' }))
```

`chance` 的官方网站: <http://chancejs.com/>

### 类型的组合使用

``` js

dream.schema('orderList', {
  id: String,
  subOrder: [Number, Number, Number],
  data: {
    owner: 'name',
    city: ['country', 'city'],
    address: 'address'
  }
})
.generateRnd(2)
.output()


/*
[
  {
    "id":"LTMWymda7ct8)V(Y&",
    "subOrder":[995639840210944,1561101036683264,3440815498067968],
    "data":{
      "owner":"Isaiah Holt",
      "city":["KR","Zabawi"],
      "address":"1444 Pavam Park"
    }
  },{
    "id":"pPNalegUq)Q(GgrmV@V7",
    "subOrder":[5977717554020352,511086627389440,2681794893709312],
    "data":{
      "owner":"Edgar Thornton",
      "city":["SR","Lelavur"],
      "address":"1933 Fiwer Heights"
    }
  }
]
*/
```


## 常用方法


### schema([String:name]?, [Object:opt])
### useSchema([String:name])

``` js

dream.schema('User', {
  name: String,
  age: Number
})

dream.schema('Location', {
  address: String,
  postcode: Number
})

const data = dream
.useSchema('Location')
.generateRnd()
.output()
```

### customType([String:name], [Function:handler])

[自定义类型](#自定义类型)


### output(), output([Function:callback])

``` js
const data = dream.output()
dream.output((err, result) => {
  if (err) {
    // ...
  }
  else {
    // ...
  }
})
```

### input(Object:PassedData)

通过 input 可以实现自定义数据流，可以再 CustomType 回调中的 helper 使用它

``` js
// 官方例子
dream.customType('customTypeWithInput', function (helper) {
  return helper.input.value;
});

dream.input({value: 'Provided by an input'})
.schema({
  result: 'customTypeWithInput'
})
.generateRnd()
.output(function (err, result) {
  console.log(result);
});

// { result: 'Provided by an input' }
```

### generate([Number:count])
### generateRnd([Number:count])

这两个函数都会生成`给定模式`的`给定数量`的实例，generateRnd 会用随机数据填充，generate 只返回空的模式

### cleanse()

清除输出和选中的 schema

```js
// source
self.cleanse = function() {
  self._output = null;
  self._selectedSchema = null;
};
```


## 注意事项

1. 每次生成数据时要调用 generateRnd 方法填充数据，默认不填充
