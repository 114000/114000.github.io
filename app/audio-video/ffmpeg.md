## startup

``` bash
# macOS
$ brew install ffmpeg
```


## Commend 

``` bash
$ ffmpeg \
[全局参数] \
[输入文件参数] \
-i [输入文件] \
[输出文件参数] \
[输出文件]
```

``` bash
$ ffmpeg \
-y \ # 全局参数
-c:a libfdk_aac -c:v libx264 \ # 输入文件参数
-i input.mp4 \ # 输入文件
-c:v libvpx-vp9 -c:a libvorbis \ # 输出文件参数
output.webm # 输出文件
```

## Parameters

- c：指定编码器
- c copy：直接复制，不经过重新编码（这样比较快）
- c:v：指定视频编码器
- c:a：指定音频编码器
- i：指定输入文件
- an：去除音频流
- vn： 去除视频流
- preset：指定输出的视频质量，会影响文件的生成速度，有以下几个可用的值 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。
- y：不经过确认，输出时直接覆盖同名文件。


## flow

### 查看视频信息

``` bash
$ ffmpeg -i <input_file>

## demo

$ ffmpeg -i input.mp4
```

### 修改文件格式

容器转换,不修改编码格式

``` bash 
$ ffmpeg -i <input_file> -c copy <output_file>

## demo

$ ffmpeg -i input.mp4 -c copy output.avi
```

### 转换编码格式

- encoder:
  * video
    - libx264：最流行的开源 H.264 编码器
    - NVENC：基于 NVIDIA GPU 的 H.264 编码器
    - libx265：开源的 HEVC 编码器
    - libvpx：谷歌的 VP8 和 VP9 编码器
    - libaom：AV1 编码器
  * audio
    - libfdk-aac
    - aac

``` bash
$ ffmpeg -i <input_file> -c:v <encoder> <output_file>

## demo

$ ffmpeg -i input.mp4 -c:v libx264 output.mp4
```

### 调整码率

调整码率（transrating）指的是，改变编码的比特率, 一般用来将视频文件的体积变小. 下面的例子指定码率最小为964K，最大为3856K，缓冲区大小为 2000K。


``` bash
 
## demo

$ ffmpeg \
-i input.mp4 \
-minrate 964K -maxrate 3856K -bufsize 2000K \
output.mp4
```

### 调整分辨率

下面是改变视频分辨率（transsizing）的例子，转为 480p 。

``` bash
## demo

$ ffmpeg \
-i input.mp4 \
-vf scale=480:-1 \
output.mp4
```

### 提取音频

从视频里面提取音频（demuxing）

``` bash
## demo

$ ffmpeg \
-i input.mp4 \
-vn -c:a copy \
output.aac

## -vn表示去掉视频，-c:a copy表示不改变音频编码，直接拷贝。
```

### 添加音轨

添加音轨（muxing）指的是，将外部音频加入视频，比如添加背景音乐或旁白。

``` bash
## demo

$ ffmpeg \
-i input.aac -i input.mp4 \
output.mp4
```

### 截图


下面的例子是从指定时间开始，连续对1秒钟的视频进行截图。

``` bash
## demo

$ ffmpeg \
-y \
-i input.mp4 \
-ss 00:01:24 -t 00:00:01 \
output_%3d.jpg
```

如果只需要截一张图，可以指定只截取一帧

``` bash
$ ffpeg \
-y \
-i input.mp4 \
-ss 00:00:04 \
-vframes 1 -q:v 2 \
output.jpg
```

上面例子中，`-vframes 1`指定只截取一帧，`-q:v 2`表示输出的图片质量，一般是1到5之间（1 为质量最高）。

### 裁剪

裁剪（cutting）指的是，截取原始视频里面的一个片段，输出为一个新视频。可以指定开始时间（start）和持续时间（duration），也可以指定结束时间（end）。

``` bash
$ ffmpeg -ss [start] -i [input] -t [duration] -c copy [output]
$ ffmpeg -ss [start] -i [input] -to [end] -c copy [output]

## demo
$ ffmpeg -ss 00:01:50 -i [input] -t 10.5 -c copy [output]
$ ffmpeg -ss 2.5 -i [input] -to 10 -c copy [output]
```

### 为音频添加封面

``` bash
## demo
$ ffmpeg \
-loop 1 \
-i cover.jpg -i input.mp3 \
-c:v libx264 -c:a aac -b:a 192k -shortest \
output.mp4
```

`-loop 1` 参数表示图片无限循环，`-shortest` 参数表示音频文件结束，输出视频就结束。