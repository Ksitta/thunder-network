# Thunder network项目后端
主要依赖 Django 以及 REST framework 框架

需要在内层backend文件夹下编写一个config.txt

格式如下

```
[db]
MYSQL_USER = root
MYSQL_PWD = 123456

[nce] 
NBI_NAME = campusAc01@north.com
NBI_PWD = Zp2T7lMXA@
```

其中[nce]中填写申请到的北向账号及密码，用于与华为NCE接口对接

需要在mysql中建立名为django_db的数据库

在mysql中执行

```
create database django_db
```

