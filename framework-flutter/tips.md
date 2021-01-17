---
title: Flutter Tips
date:  2018-08-12
---


1. 只有容器可以设置填充，边距，边框或背景色(Container)

2. 图片必须在根目录下的 `pubspec.yaml` - `flutter` - `assets` 配置后才能使用

    ``` yaml
    flutter:
      assets:
        - images/pic.jpg
    ```

    ``` dart
    new Image.asset('images/pic.jpg', fit: BoxFit.cover);
    ```

3. 无样式布局初始化

    ``` dart

    void main() {
      runApp(new MyApp());
    }


    class MyApp extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        // 不包一层 MaterialApp 你就等着被坑死吧！
        return new MaterialApp(
          home: yourRootWidgetContainer,
        );
    }
    ```

4. `r` 是刷新可见元素，如果改了一般的类要按 `R`


5. 显示网络图片

```dart
Image.network(imageUrl);
```

6. 小间距可以使用 SizedBox 填充

``` dart
Column(
  children: [
    Image.network(posts[index].imageUrl),
    SizedBox(height: 16.0),
    Text(
      posts[index].title,
      style: Theme.of(context).textTheme.title
    ),
    Text(
      posts[index].author,
      style: Theme.of(context).textTheme.subhead
    ),
    SizedBox(height: 16.0)
  ]
)
```

7. 图片的圆角 

``` dart

Material(
  borderRadius: BorderRadius.circular(12),
  clipBehavior: Clip.hardEdge, // 否则图片不根据圆角变化
  // ...
)

```


#### links:

- [How to build iPhone Calculator using Flutter](https://hackernoon.com/how-to-build-iphone-calculator-using-flutter-fe934ce78d7e)