---
title: nginx
date: 2018-06-28
tag:
- nginx
---

## nginx startup

### nginx install

- CentOS

1. 新建 nginx.repo 文件
``` bash
$ vi /etc/yum.repos.d/nginx.repo
```

``` bash
# nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/centos/7/$basearch/
gpgcheck=0 # 不检查 gpg
enabled=1  # 默认开启
```

2. 安装
``` bash
$ yum install nginx -y
# 浏览器访问IP即可
```

---

## nginx flow


``` bash
# 测试配置
$ nginx -t 

# 启动
$ systemctl start nginx
$ systemctl enable nginx

# 重启
$ systemctrl reload nginx
```

---

## nginx resources

- [Nginx 如何设置 IPv6 网站](https://bubblin.io/blog/ipv6-nginx)
- [nginxconfig.io](https://nginxconfig.io/)

--- 

## nginx tips

### nginx 反向代理(proxy)时传递真实IP

```
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

### nginx 获取、返回IP

```
location /ip {
    default_type text/plain;
    return 200 $remote_addr;
}
```

```
location /json_ip {
    default_type application/json;
    return 200 "{\"ip\":\"$remote_addr\"}";
}
```

### nginx 403 for forbidden

``` bash 
$ getenforce 
# 如果是 Disabled 可能是其他权限引起的，如果不是[eg:Enforincing]就修改这个selinux配置
# chcon -Rt httpd_sys_content_t [访问路径]
```
http://www.ha97.com/4336.html
https://www.barretlee.com/blog/2016/11/19/nginx-configuration-start/


### nginx 配置二级域名

1. 在运营商处未二级域名添加解析(多个二级域名解析到同一个 ip 即可)
2. 在nginx server 模块中添加配置 `server_name  2.yourdomain.top two.youdomain.cc;`


### Resources 

- [如何改进 NGINX 配置文件节省带宽？ - NGINX 官方的博客文章，教大家五个小技巧，通过改进配置来节省带宽、提高性能。](https://www.nginx.com/blog/help-the-world-by-healing-your-nginx-configuration/)
- [NGINX Config](https://www.digitalocean.com/community/tools/nginx)