### 多插槽

[vue3 插槽](https://vue3js.cn/docs/zh/guide/component-slots.html#%E8%A7%A3%E6%9E%84%E6%8F%92%E6%A7%BD-prop)

``` html
<!-- components -->
<div>
  <slot name="slot-one"></slot>
  <hr />
  <slot></slot>
<div>
 
<!-- parent -->
<Component>
  <template v-slot:slot-one>
    one
  </template>


  <!-- 直接写 -->
  default string


  <!-- or -->
  <template v-slot:default>
    default string
  </template>
</Component>
```

### slot 传参

``` html
<!-- components -->
<tr>
  <slot :item="aItem" :index="i">
    <!-- slot default -->
    <td
      class="cp-sp-table__col"
      :style="styles[j]"
      v-for="(f, j) in fields"
      :key="j">{{ item[f] }}</td>
  </slot>
</tr>
 
 
<!-- parent -->
<Component>
  <template v-slot:default="d">
    <td>{{ d.index }}<td>
    <td>{{ d.item[0] }}<td>
  </template>
</Component>
```

### 获取 ref

``` js
<div ref="chart" />
 
 
// option api
mounted () {
  this.$refs.chart
}
 
// composition api
 
 
setup () {
  const chartDom = ref(null)

  mounted(() => {
    // chartDom.value
  })

  return {
    chart: chartDom
  }
}
```

### 传递原生属性/事件

``` html
<!-- v2 -->
<div class="cp-box" v-bind="$attrs" v-on="$listeners">
 
 
<!-- v3: 函数合并到$attrs中 -->
<div class="cp-box" v-bind="$attrs">
 
<Box :style="{ height: '100px' }" @click="handleClick" />
```