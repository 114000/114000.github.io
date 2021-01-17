---
title: Antd(React) tips
---

### Antd Table 白色空隙

1. fixed 的设置宽度，其他的固定项目不设置宽度 
2. x轴设置成一个够用的值

``` jsx

<Table scroll={{ x: 2000 }}>
```


### Antd Form 自定义表单空间报错 

``` jsx
const ChildComponent = (props, ref) =>{
  return <input 
    value={props.value}
    onChange={e => props.onChange(e.target.value)}
  />
}

const Child = forwardRef(ChildComponent)

const Parent = props => {
  

  return <Form.Item>
    {props.form.getFieldDecprator('name', {})(
      <Child />
    )}
  </Form.Item>
}


```