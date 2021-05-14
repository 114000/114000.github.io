# pip

- 查看版本 `pip -V`
- 升级pip `python -m pip install --upgrade pip` 
  * windows 需要管理员权限
- 查看安装的包 `pip list`
- 查看安装包版本号 `pip freeze`
- 生成依赖文件 `pip freeze > requirements.txt`
- 安装包 `pip install`
- 卸载包 `pip uninstall`
- 根据依赖文件安装依赖 `pip install -r requirements.txt`
- 切换源
  * 单切: pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple
  * 全切: pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
  * 可用源
    - https://pypi.tuna.tsinghua.edu.cn/simple
    - https://mirrors.aliyun.com/pypi/simple
    - http://mirrors.cloud.tencent.com/pypi/simple
    - http://pypi.douban.com/simple




### Trouble Shooting 

> pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.