---
title: SQL & CL
date: 2019-01-01

---


## SQLite

### startup

``` bash
$ sqlite3
> .open db.sqlite # 所在目录创建 <db.sqlite> 文件
> .databases      # 查看数据库
> .quit           # 退出命令
```

### 表操作

``` bash
# list
> .tables # .table

# delete
> drop table <tablename>;
```

### 清空表

``` bash
> .open db.sqlite
> delete from <tablename>;
```


### Sql

- [数据库基础](http://webdam.inria.fr/Alice/)
- [SQLite 用作搜索服务](https://24ways.org/2018/fast-autocomplete-search-for-your-website/)
- [LiteCLI 一个 SQLite 数据库的命令行客户端](https://www.pgcli.com/launching-litecli.html)
- [Mixnode - Mixnode 是一个收集了全世界网页的数据库，允许使用类似 SQL 的语法查询网页。](https://www.mixnode.com/blog/posts/turn-the-web-into-a-database-an-alternative-to-web-crawling-scraping)
- [sqlfmt SQL 语句格式化的在线工具。](https://sqlfum.pt/)
- [SQL 开源教程 - 这是一本互动书籍，免费，帮助读者了解如何使用 SQL 对数据集运行查询。](https://selectstarsql.com/)
- [q - 一个对 CSV 文件使用 SQL 数据查询的工具](https://github.com/harelba/q)
- [ByteScout SQL Trainer 一个互动式的在线 SQL 语法教程，针对新手。答对一个问题，才能进入下一个](https://app.bytescout.com/sql-trainer/index.html)
- [dbdiagram.io - 创建数据库的实体-关系图的工具。](https://dbdiagram.io/)
- [Active Record 与 Data Mapper 的差异 - 关系型数据库的操作通常采用 ORM 库，将表格转换成对象。ORM 主要分成两种类型：Active Record 与 Data Mapper。本文讨论这两种模型的差异和适用场景。"](http://www.culttt.com/2014/06/18/whats-difference-active-record-data-mapper/)
- [SQL 谋杀之谜 - 一个英文的 SQL 初级教程，以游戏的方式，让你利用学到的 SQL 概念和命令来找出谋杀凶手](https://mystery.knightlab.com/walkthrough.html)
- [HugeGraph - 百度安全团队研发的一款易用、高效、通用的开源图数据库系统， 具备完善的工具链组件，助力用户轻松构建基于图数据库之上的应用和产品](https://github.com/hugegraph/hugegraph)
- Dgraph
- [RDF 和 SPARQL 初探：以维基数据为例](http://www.ruanyifeng.com/blog/2020/02/sparql.html)