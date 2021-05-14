---
title: 树莓派
---

## Note:

安装谷歌拼音输入法

- `sudo apt-get install fcitx fcitx-googlepinyin`

连接中文路由需要使用 add_network

``` bash
$ sudo wpa_cli
> add_network
1 # id
> set_network 1 

```

## boot



### 1. MacOS 烧录

1.1 查看磁盘路径 `diskutil list` 记录路径 e.g. `/dev/disk2`
1.2 取消tf卡挂载 `diskutil unmountDisk <sd_path>` 
1.3 烧录镜像 `sudo dd if=<img_path> of=<sd_path> bs=1m;sync` [dd 命令](https://www.runoob.com/linux/linux-comm-dd.html)
1.4 退出tf `$ diskutil eject <sd_path>`

### 2. 烧录树莓派系统

#### 2.1 烧录系统

- 下载镜像: <https://www.raspberrypi.org/software/>
- 格式化sd卡: 磁盘工具 or SD Card Formatter

#### 2.2 自动连接wifi

有系统界面的不能用这个方法

第一次启动前在根目录创建 `wpa_supplicant.conf` 文件.

```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
        ssid="第一个WIFI名称，优先级1"
        psk="WIFI密码"
        key_mgmt=WPA-PSK
        priority=1
}
network={
        ssid="第二个WIFI名称，无密码，优先级2"
        key_mgmt=NONE
        priority=2
}


network={
  # 中文的wifi名
	ssid=e79b9be59889e7a791e68a80
	psk="88888888"
	key_mgmt=WPA-PSK
}

```

#### 2.2 开启远程 ssh 功能

有系统界面的不能用这个方法

第一次启动前在根目录创建 `ssh` 空文件.

#### 2.3 flow

- 进入系统设置: `$ sudo raspi-config`
- 重启: `$ sudo reboot`
- 安装: `$ sudo apt install ffmpeg`
- 卸载: 
  - `$ sudo apt remove python`
  - `$ sudo apt autoremove`
- 软链接:
  - `$ sudo ln -s /usr/bin/python3 /usr/bin/python`
- 网络:
  - 查看可用wifi `$ sudo iwlist wlan0 scan | grep SSID`
  - 查看wifi 信道(系统地区影响信道): `$sudo iwlast wlan0 freq`

### 3. 烧录 ubuntu 系统

#### 3.1 烧录系统

- 安装 xz 命令 

``` bash
$ xz -d xxx.img.xz
$ sudo dd if=/Users/apple/Downloads/ubuntu-20.04.2-preinstalled-server-arm64+raspi.img of=/dev/disk3 bs=4m;sync
```



#### 3.2 链接wifi

修改sd卡根目录的 network-config 

### 4. 注意 

- WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!: 更换系统后要删除 `~/.ssh/known_hosts` 对应行


### 其他

#### 安装 docker 

```
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```


### 树莓派 

- [树莓派 GPIO 介绍](https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html)
- [树莓派搭建空气质量监视器](https://www.balena.io/blog/build-an-environment-and-air-quality-monitor-with-raspberry-pi/)
- [树莓派的问题](https://ownyourbits.com/2019/02/02/whats-wrong-with-the-raspberry-pi/)
- [树莓派的项目](https://hackaday.io/projects?tag=raspberry%20pi)
- [如何使用树莓派架设各种网络服务](https://www.techcoil.com/blog/how-i-use-my-raspberry-pis-to-help-me-work-on-with-my-side-projects/)
- [pi-hole 一个基于树莓派的家用 DNS 服务器，自带屏蔽广告功能。](https://github.com/pi-hole/pi-hole)
- [我如何搭建家庭机房](https://blog.networkprofile.org/6-year-homelab-history-in-pictures/)
- [self-driving-toy-car - 一个开源的自动驾驶玩具车，在小车上面绑了一个树莓派和摄像头。](https://github.com/experiencor/self-driving-toy-car)
- [树莓派的局限 - 作者从硬件角度谈了树莓派三代的一些问题，以及由此导致的不合适使用的场景](https://ownyourbits.com/2019/02/02/whats-wrong-with-the-raspberry-pi/)
- [Pi-hole 拦截广告 - 它是树莓派上的 DNS 服务器](https://www.troyhunt.com/mmm-pi-hole/)
- [开源火星车 - 树莓派作为车载控制中心，使用安卓手机或 xbox 手柄遥控](https://github.com/nasa-jpl/open-source-rover)
- [树莓派如何搭建 NAS - 想要搭建家用储存系统的朋友](https://opensource.com/article/18/7/network-attached-storage-Raspberry-Pi)
- [使用树莓派自制热像仪](https://medium.com/sausheong/build-a-thermal-camera-with-raspberry-pi-and-go-8f70451ad6a0)
- [图灵派（Turing Pi）](https://turingpi.com/)
- [一个语音工具的集成软件，文档教你如何在树莓派上使用 Node.js，搭建自己的语音助手，可以识别语音，也可以将文本转为语音。](https://github.com/webfansplz/volute)
- [使用 Raspberry Pi 学习操作系统开发 - 这是一个免费英文教程，教大家怎么用树莓派，一步步开发一个简单的操作系统内核，每一步都有实例代码。](https://s-matyukevich.github.io/raspberry-pi-os/)

## PLC

- [Snap7 西门子S7系列PLC的通信库 简介](https://blog.csdn.net/lcb411/article/details/101147181)