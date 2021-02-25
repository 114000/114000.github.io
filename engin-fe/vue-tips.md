### 多插槽

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
<slot :row="item" :index="i">
  <div
    class="cp-sp-table__col"
    :style="styles[j]"
    v-for="(f, j) in fields"
    :key="j">{{ item[f] }}</div>
</slot>
 
 
<!-- parent -->
<Component>
  <div slot-scope="d" :style="{ paddingTop: '0.7rem' }">
    <XXX
      :color="d.item.color"
      :max="state.max"
      :min="0.05"
      :name="d.item.name"
      :value="d.item.value" />
  </div>
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