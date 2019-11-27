from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from exts import db
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


class ArticleView(ModelView):
    can_create = True   # 可以创建数据  False
    can_delete = True   # 可以删除数据  False
    can_edit = True     # 可以编辑数据  False