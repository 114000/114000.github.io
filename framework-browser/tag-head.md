---
title: tag head
---

### 最小化推荐

下面是任何web文档(网站,webapp)必须要有的元素

``` html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--
  以上两个 meta 标签必须放到 <head> 的最前面, 这样可以确保文档
  能正确的渲染. 任何其他头部元素必须放在这些标签后面
 -->
<title>Page Title</title>
```

- **meta charset**: 定义网站编码, `utf-8`是标准编码方式
- **meta name=”viewport”**: 关于移动端响应式的视口设置
- **width=device-width**: 视口使用设备的物理宽度(而不缩小页面),可以使移动端的页面更为友好
- **initial-scale=1** 初始拉伸比例, `1`代表不拉伸

#### 头部可包含的标签

合法的 `<head>` 标签包括 `meta`, `link`, `title`, `style`, `script`, `noscript`, and `base`.

这些标签告诉web技术(e.g. 浏览器,搜索引擎,机器人等)文档应该被怎样检测和渲染.

```html
<!--
  Set the character encoding for this document, so that
  all characters within the UTF-8 space (such as emoji)
  are rendered correctly.
-->
<meta charset="utf-8">

<!-- Set the document's title -->
<title>Page Title</title>

<!-- Set the base URL for all relative URLs within the document -->
<base href="https://example.com/page.html">

<!-- 链接一个外部的css文件 -->
<link rel="stylesheet" href="styles.css">

<!-- Used for adding in-document CSS -->
<style>
  /* ... */
</style>

<!-- JavaScript & No-JavaScript 变迁 -->
<script src="script.js"></script>
<script>
  // function(s) go here
</script>
<noscript>
  <!-- 禁用 script 时显示此标签内容 -->
</noscript>
```

#### Meta 标签

``` html
<!--
  下面两个 meta 标签必须放到 <head> 的最前面, 这样可以确保文档
  能正确的渲染. 任何其他头部元素必须放在这些标签后面
-->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!--
  Allows control over where resources are loaded from.
  Place as early in the <head> as possible, as the tag  
  only applies to resources that are declared after it.
-->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">

<!-- web 应用的名称 (尽量只在网站是web应用的情况下使用) -->
<meta name="application-name" content="Application Name">

<!-- Chrome, Firefox OS and Opera 的主题颜色 -->
<meta name="theme-color" content="#4285f4">

<!-- 文档的简介 (150字符长度限制) -->
<!-- 这部分内容 *也许* 会成为搜索引擎结果中的一部分 -->
<meta name="description" content="A description of the page">

<!-- 控制搜索引擎爬网和建立索引的行为 -->
<meta name="robots" content="index,follow"><!-- 所有搜索引擎 -->
<meta name="googlebot" content="index,follow"><!-- 只针对 Google  -->

<!-- Tells Google not to show the sitelinks search box -->
<meta name="google" content="nositelinkssearchbox">

<!-- 告诉 Google 不需要为此文档提供翻译 -->
<meta name="google" content="notranslate">

<!-- 验证网站所有权 Verify website ownership -->
<meta name="google-site-verification" content="verification_token"><!-- Google Search Console -->
<meta name="yandex-verification" content="verification_token"><!-- Yandex Webmasters -->
<meta name="msvalidate.01" content="verification_token"><!-- Bing Webmaster Center -->
<meta name="alexaVerifyID" content="verification_token"><!-- Alexa Console -->
<meta name="p:domain_verify" content="code_from_pinterest"><!-- Pinterest Console-->
<meta name="norton-safeweb-site-verification" content="norton_code"><!-- Norton Safe Web -->

<!-- 识别用于构建文档的软件 (i.e. - WordPress, Dreamweaver) -->
<meta name="generator" content="program">

<!-- 文档主题的简介 -->
<meta name="subject" content="your document's subject">

<!-- 根据文件内容给出一般年龄等级 -->
<meta name="rating" content="General">

<!-- Allows control over how referrer information is passed -->
<meta name="referrer" content="no-referrer">

<!-- Disable automatic detection and formatting of possible phone numbers -->
<meta name="format-detection" content="telephone=no">

<!-- Completely opt out of DNS prefetching by setting to "off" -->
<meta http-equiv="x-dns-prefetch-control" content="off">

<!-- Specifies the document to appear in a specific frame -->
<meta http-equiv="Window-Target" content="_value">

<!-- Geo tags -->
<meta name="ICBM" content="latitude, longitude">
<meta name="geo.position" content="latitude;longitude">
<meta name="geo.region" content="country[-state]"><!-- Country code (ISO 3166-1): mandatory, state code (ISO 3166-2): optional; eg. content="US" / content="US-NY" -->
<meta name="geo.placename" content="city/town"><!-- eg. content="New York City" -->
```

*lib*
- [HTML 网页的 head 元素 指南](https://htmlhead.dev/)