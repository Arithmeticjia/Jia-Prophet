from flask import Flask, render_template, session, redirect, url_for
import config
from flask import jsonify,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time
from flask_sqlalchemy import SQLAlchemy
from exts import db
from models import Article,ArticleView
import pymysql

app = Flask(__name__)
admin = Admin(app=app, name='后台管理系统',template_mode='bootstrap3')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:980612ssj@%@101.132.70.184:3306/JiaBlog"
# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['JSON_AS_ASCII'] = False
# app.config['SECRET_KEY'] = '123456'
app.config.from_object("config.DevelopmentConfig")  # 加载配置文件
db.init_app(app)
# admin.add_view(ModelView(Article, db.session))
admin.add_view(ArticleView(Article, db.session))


# db.drop_all()     # 删除表
# db.create_all()   # 建表


@app.route('/')
def index():
    return render_template('index.html')

def testdb():
    post = Article.query.filter(Article.title == "")

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


@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        # 数据库校验，用户密码是否正确
        if username == '妲己' and password == '123123':
            session['user_id'] = 1
            session['user_name'] = username
            return redirect((url_for('index')))
        else:
            return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
