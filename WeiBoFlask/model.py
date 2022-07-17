# 本文件 用于存放项目中的模型
# python 提供了pymongo对MongoDB进行操作,但是如果直接在代码中对数据库进行各种操作,不仅增加了代码的耦合性,也降低了代码的安全性
# 因此,选择使用mongoengine这种文档映射器(类似于ORM)操作数据库
# 特别注意:电脑需要安装MongoDB数据库, 并在 计算机管理-服务和应用程序-服务-MongoDB Server 进行启用
from mongoengine import *
from flask_login import UserMixin

# connect('dbname',ip='ip',port='port')
connect('dbname')


# 连接数据库,如果mongodb搭建在本机,并且使用默认端口27017,可以忽略ip和端口,只传入数据库名
# 数据库连接成功之后，就可以开始创建所需要的数据模型，为了使数据类和数据表能够进行关联，需要继承mongoenging的Document类。
# 在声明属性时候，根据需要将属性定义为不同的 field 类型，从而实现类属性和表列的绑定。
# 常用的field 包含StringField、IntField、FloatField、DictField、ListField 等，用于表示字符串、整数、浮点数、字典和列表类型，
# 除此之外，还包含数十种其他类型，读者可以访问http://docs.mongoengine.org进行参考。

# 用户模型
class User(Document, UserMixin):
    username = StringField(required=True)  # 用户名,require表示必填
    password = StringField(required=True)  # 密码
    nickname = StringField()  # 昵称


# 博客模型
class Blog(Document):
    time = IntField(required=True)  # 发布时间
    msg = StringField(required=True)  # 内容

    def get_json(self):
        return {
            'time': self.time,
            'msg': self.msg
        }


# 尝试向数据库中添加一条数据
# user = User()
# user.username = 'username'
# user.password = 'password'
# user.save()

# 查看是否保存成功
