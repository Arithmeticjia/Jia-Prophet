from flask_sqlalchemy import SQLAlchemy
from exts import db


class Article(db.Model):
    # 定义表名
    __tablename__ = 'article'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)