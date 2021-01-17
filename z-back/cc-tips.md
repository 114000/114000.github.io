---
title: 【归档】Cocos2D Creator
date: 2017-11-30
tag: Outdated
---


::: danger
2019-12-16: 留档
:::

---

### Cocos2D Creator 导入 Spine 特效文件

1. 生成的文件拖入项目中

```
fileName.altas // 图集的坐标文件
fileName.json  // 动画数据
fileName.png   // 图片
```

2. 层级管理器中创建空节点，添加再点击 `添加组件` - `添加渲染组件` - `Spine Skeleton`

3. 将导入的JSON 文件拖到组件的  Skeleton Data 属性上，再选择 Animation 中的需要的动画

---

### Cocos2D Creator 打包图集 Texture Packer

1. **保留图集元素的透明区域**: Layout/Trim mode => `None`
2. **图集中的元素允许旋转**: Layout/Algorithm => `MaxRects`

---


### Cocos2D Creator 加载图集中的 SpriteFrame 

<http://docs.cocos.com/creator/manual/zh/scripting/load-assets.html#动态加载-asset>

``` javascript
cc.loader.loadRes("test assets/sheep", cc.SpriteAtlas, function (err, atlas) {
    var frame = atlas.getSpriteFrame('sheep_down_0');
    sprite.spriteFrame = frame;
});
```

---

- [web端横屏改为逆时针旋转90度](http://forum.cocos.com/t/web-90/50145)

---
- 文字左对齐：锚点x设置为0

- 代码控制 cc.widget 

```javascript
this.widget.isAlignLeft = info.left
this.widget.isAlignRight = !info.left
this.widget.isAlignTop = info.top
this.widget.isAlignBottom = !info.top

this.widget[info.left ? 'left' : 'right'] = info.hor
this.widget[info.top ? 'top' : 'bottom'] = info.ver
    
// 设置完 widget 需要手动更新否则不会生效
this.widget.updateAlignment()
```

- 不能创建同名 js文件，路径不用也不行，内部好像是用文件名的hash做的模块索引

- on 添加的事件可以用 off 解绑，once 添加的不能用off解绑