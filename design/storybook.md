# storybook-v6


## 开始

``` bash
$ vue create storybook-v6
$ cd storybook-v6
$ npx sb init --type vue
$ npm run storybook
```

##  使用  

``` js
import bar from './Bar.vue'

export default {
  title: 'Example/Bar',
  component: bar,
  argTypes: {
    color: { control: 'color' }, // 声明"颜色"prop用拾色器来展示,其他类型查看下方表格
  },
}

const Template = (args, { argTypes }) => ({
  props: Object.keys(argTypes),
  components: { bar },
  template: '<bar v-bind="$props" />', // 可以用模板字符串,也可以用jsx
});

export const Primary = Template.bind({})
Primary.args = { 
  val: [200, 300, 400, 240, 200] // 预设变量
  }

export const Secondary = Template.bind({})

Secondary.args = {
  val: [100, 200] // 预设变量
}


```

### 所有参数类型

<https://storybook.js.org/docs/react/essentials/controls#annotation>

| Data Type | Control Type | Description | Options |
|:---|:---|:---|:---|
|array|array|serialize array into a comma-separated string inside a textbox|separator|
|boolean|boolean|checkbox input|-|
|number|number|a numeric text box input|min, max, step|
|-|range|a range slider input|min, max, step|
|object|object|json editor text input|-|
|enum|radio|radio buttons input|options|
|-|inline-radio|inline radio buttons input|options|
|-|check|multi-select checkbox input|options|
|-|inline-check|multi-select inline checkbox input|options|
|-|select|select dropdown input|options|
|-|multi-select|multi-select dropdown input|options|
|string|text|simple text input|-|
|-|color|color picker input that assumes strings are color values|-|
|-|date|date picker input|-|


## 引用其他storybook 

```diff
// .storybook/main.js

module.exports = {
  "stories": [
    "../src/**/*.stories.mdx",
    "../src/**/*.stories.@(js|jsx|ts|tsx)"
  ],
  "addons": [
    "@storybook/addon-links",
    "@storybook/addon-essentials"
  ],
+ "refs": {
+   "design-system": { 
+     "title": "Design System", 
+     "url": "https://5ccbc373887ca40020446347-yldsqjoxzb.chromatic.com"
+   }
+  }
}
```