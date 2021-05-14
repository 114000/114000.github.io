# Flask - Python 服务端框架

2020-11-01

- [pip](lang-py/pip.md)

## Install


- 新建目录 `$ mkdir <project>`
- 创建虚拟环境 `<p>$ python -m venv <venvName>`
- 激活虚拟环境
  * linux `<p>$ source <venvName>/bin/activate`
  * windows `<p>$ <venvName>\Scripts\activate`
- 安装 flask `<venvName>$ pip install Flask`


## Startup

> /app.py

```python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello</h1>'

@app.route('/user/<name>')
def user(name):
  return '<h1>Hello, {}!<h1>'.format(name)
```

1. 

- 设置App 入口文件 
  - linux `<venvName>export FLASK_APP=app.py`
  - windows: `<venvName>set FLASK_APP=app.py`
- Simple Server `<venvName>$ flask run --reload --debugger`
- 访问 `localhost:5000`

2.

- `<venvName>$ python main.py`

``` py
from app import app

if __name__ == "__main__":
  app.run(debug = True)
```



## 格式化请求参数

### GET & Query String

``` py
from flask import request, jsonify
from app import app

@app.route('/test/query', methods=['GET'])
def test_query ():
  # Query String: ?grade=2&class=6
  try:
    # default None
    grade_num = request.args.get('grade', None)
    # Error 
    class_num = request.args['class']

    return 'Class: {} Grade: {}'.format(class_num, grade_num)
  except:
    return jsonify({ 'message': '参数错误' }), 400

```

### POST & JSON

``` py
import json
from app import app

@app.route('/test/json', methods=['POST'])
def test_json ():
  # str => dict
  # 数组第一项的url
  url = json.loads(request.data)[0]['url']

  return url
```

### POST & Form Data

``` py
from flask import request, jsonify
from app import app

@app.route('/test/form-data', methods=['POST'])
def test_form_data ():
  # FormData 从 request.form 中获取

  return jsonify(request.form)
```


## 上下文

``` py
from flask import request

@app.route('/')
  user_agent = request.headers.get('User-Agent')
  return '<p>{}<p>'.format(user_agent)
```

|变量名|上下文类型|说明|
|:---|:---|:---|
|`current_app`|应用上下文|当前应用的应用实例|
|`g`|应用上下文|处理请求时用作临时存储的对象，每次请求都会重设这个变量|
|`request`|请求上下文|请求对象，封装了客户端发出的 HTTP 请求中的内容|
|`session`|请求上下文|用户会话，值为一个字典，存储请求之间需要“记住”的值|




## 钩子

- `before_request`: 注册一个函数，在每次请求之前运行
- `before_first_request`: 注册一个函数，只在处理第一个请求之前运行。可以通过这个钩子添加服务器初始化任务
- `after_request`: 注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
- `teardown_request`: 注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行

钩子间共享应用上下文 `g`

e.g. 待补充

## 响应


e.g. 

简单

``` py
@app.route('/')
def index():
  return '<h1>Bad Request</h1>', 400
```

复杂

``` py
from flask import make_response

@app.route('/')
def index():
  response = make_response('<h1>This document carries a cookie!</h1>')
  response.set_cookie('answer', '42')
  return response
```


### 重定向

```py
from flask import redirect

@app.route('/')
def index():
  return redirect('http://abc.com')

```

### 中断

``` py
from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
```


## 附录

### Request 

``` py
class Request

form # 一个字典，存储请求提交的所有表单字段
args # 一个字典，存储通过 URL 查询字符串传递的所有参数
values # 一个字典，form 和 args 的合集
cookies # 一个字典，存储请求的所有 cookie
headers # 一个字典，存储请求的所有 HTTP 首部
files # 一个字典，存储请求上传的所有文件
scheme # URL 方案（http 或 https）
host # 请求定义的主机名，如果客户端定义了端口号，还包括端口号
path # URL 的路径部分
query_string # URL 的查询字符串部分，返回原始二进制值
full_path # URL 的路径和查询字符串部分
url # 客户端请求的完整 URL
base_url # 同 url，但没有查询字符串部分
remote_addr # 客户端的 IP 地址
environ # 请求的原始 WSGI 环境字典

def get_data() # 返回请求主体缓冲的数据
def get_json() # 返回一个 Python 字典，包含解析请求主体后得到的 JSON
def blueprint() # 处理请求的 Flask 蓝本的名称；蓝本在第 7 章介绍
def endpoint() # 处理请求的 Flask 端点的名称；Flask 把视图函数的名称用作路由端点的名称
def method() # HTTP 请求方法，例如 GET 或 POST
def is_secure() # 通过安全的连接（HTTPS）发送请求时返回 True

```

#### Response

``` py
class Response

  status_code # HTTP 数字状态码
  headers # 一个类似字典的对象，包含随响应发送的所有首部
  content_length # 响应主体的长度
  content_type # 响应主体的媒体类型

  def set_cookie () # 为响应添加一个 cookie
  def delete_cookie () # 删除一个 cookie
  def set_data () # 使用字符串或字节值设定响应
  def get_data () # 获取响应主体
```


## 扩展


### Flask-SQLAlchemy

``` bash
(venv)$ pip install flask-sqlalchemy
```

```py
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

- MySQL: mysql://username:password@hostname/database
- Postgres: postgresql://username:password@hostname/database
- SQLite（Linux，macOS）: sqlite:////absolute/path/to/database
- SQLite（Windows）: sqlite:///c:/absolute/path/to/database


#### 最常用的SQLAlchemy列类型

- `Integer<int>`: 普通整数，通常是 32 位
- `SmallInteger<int>`: 取值范围小的整数，通常是 16 位
- `BigInteger<int|long>`: 不限制精度的整数
- `Float<float>`: 浮点数
- `Numeric<decimal.Decimal>`: 定点数
- `String<str>`: 变长字符串
- `Text<str>`: 变长字符串，对较长或不限长度的字符串做了优化
- `Unicode<unicode>`: 变长 Unicode 字符串
- `UnicodeText<unicode>`: 变长 Unicode 字符串，对较长或不限长度的字符串做了优化
- `Boolean<boolean>`: 布尔值
- `Date<datetime.date>`: 日期
- `Time<datetime.time>`: 时间
- `DateTime<datetime.datetime>`: 日期和时间
- `Interval<datetime.timedelta>`: 时间间隔
- `Enum<str>`: 一组字符串
- `PickleType<object>`: 任何 Python 对象, 自动使用 Pickle 序列化
- `LargeBinary<str>`: 二进制 blob


#### 最常用的SQLAlchemy列选项

- `primary_key`: 如果设为 True，列为表的主键
- `unique`: 如果设为 True，列不允许出现重复的值
- `index`: 如果设为 True，为列创建索引，提升查询效率
- `nullable`: 如果设为 True，列允许使用空值；如果设为 False，列不允许使用空值
- `default`: 为列定义默认值

### 常用的SQLAlchemy关系选项

- `backref`: 在关系的另一个模型中添加反向引用
- `primaryjoin`: 明确指定两个模型之间使用的联结条件；只在模棱两可的关系中需要指定
- `lazy`: 指定如何加载相关记录，可选值有 select（首次访问时按需加载）、immediate（源对象加载后就加载）、joined（加载记录，但使用联结）、subquery（立即加载，但使用子查询），noload（永不加载）和 dynamic（不加载记录，但提供加载记录的查询）
- `uselist`: 如果设为 False，不使用列表，而使用标量值
- `order_by`: 指定关系中记录的排序方式
- `secondary`: 指定多对多关系中关联表的名称
- `secondaryjoin`: SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件


### Flask-CORS

``` bash
(venv)$ pip install flask_cors
```

``` py
from app import app
from flask_cors import CORS

CORS(
  app,
  supports_credentials=True,
  resources={r'/*': { 'origins': '*' }}
)
```

### swagger-py-codegen

### flask-Restful