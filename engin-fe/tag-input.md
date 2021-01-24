---
title: tag input - HTMLInputElement 
date: '2019-12-22'
---

|属性名|可使用的type|详情|只针对JS|
|:---|---:|:---|:---|
|`defaultValue<string>`|--|初始值,不会因为 `value` 的变化而变化||
|`selectionStart<number>`|`text`,`password`<br>`tel`,`url`,`week`<br>`search`,`month`|选中范围的起始位置|✅|
|`selectionEnd<number>`|`text`,`password`<br>`tel`,`url`,`week`<br>`search`,`month`|选中范围的结束位置|✅|
|`selectionDirection`|`text`,`password`<br>`tel`,`url`,`week`<br>`search`,`month`|选中方向 `forward`, `backward`, `none`|✅|
|`check<boolean>`|`checkbox`,`radio`|--||
|`defaultChecked<boolean>`|`checkbox`,`radio`|初始值,不会因为 `checked` 变化而变化|✅|
|`indeterminate<boolean=false>`|`checkbox`,`radio`| - `checkbox` 设置 `indeterminate = true` 后选框显示会变为横线, 点击选框后会 `indeterminate` 变为 `false` `checked` 变为相反的值. NOTE: JS设置check无法影响显示,`click()`可以.<br> - `radio` 不会有显示影响|✅|


*lib*:
  - [MDN HTMLInputElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
  - [input 元素的三个属性](https://dev.to/stefanjudis/three-input-element-properties-that-i-discovered-while-reading-mdn-30fg)
