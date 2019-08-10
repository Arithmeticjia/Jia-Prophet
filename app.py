from flask import Flask
from flask import jsonify,request
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:980612ssj@%@101.132.70.184:3306/JiaBlog"
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    # 定义表名
    __tablename__ = 'article'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


# db.drop_all()     # 删除表
# db.create_all()   # 建表


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict',methods=["GET", "POST"])
def predict():
    data = {"success": False}

    params = request.json
    if (params == None):
        params = request.args

    # 若发现参数，则返回预测值
    if (params != None):
        x = pd.DataFrame.from_dict(params, orient='index').transpose()

    return jsonify(data)


@app.route('/detail',methods=["GET","POST"])
def detail():
    articles = Article.query.all()
    print(articles)
    model_to_dict(articles)
    return jsonify(model_to_dict(articles))


def model_to_dict(result):
    from collections import Iterable
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')


if __name__ == '__main__':
    app.run()
