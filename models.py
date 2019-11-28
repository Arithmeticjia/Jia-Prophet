from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from exts import db
from flask_login import UserMixin,AnonymousUserMixin
from datetime import datetime


class Article(db.Model):
    # 定义表名
    __tablename__ = 'article'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


''' flask-login user类必须实现以下:
        is_authenticated 是否属性
        is_active 是否激活属性
        is_anonymous 是否匿名属性
        get_id() 方法, 可以继承UserMixin,提供了默认实现
'''


class User(db.Model, UserMixin):
    __tablename__ = 'user'  # 表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
    write_time = db.Column(db.DateTime, default=datetime.now())
    # toString方法

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id


class ArticleView(ModelView):
    can_create = True   # 可以创建数据  False
    can_delete = True   # 可以删除数据  False
    can_edit = True     # 可以编辑数据  False


class UserView(ModelView):
    can_create = True   # 可以创建数据  False
    can_delete = True   # 可以删除数据  False
    can_edit = True     # 可以编辑数据  False
