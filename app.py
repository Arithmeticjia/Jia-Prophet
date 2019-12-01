from flask import Flask, render_template, session, redirect, url_for,flash
from flask_restful import Api,Resource
import config
from forms import LoginForm
from flask import jsonify,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import pandas as pd
from flask_cors import *
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time
from flask_sqlalchemy import SQLAlchemy
from exts import db
from models import Article,ArticleView,User,UserView
from flask_login import login_user,logout_user,login_required,LoginManager,current_user

import pymysql

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
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
admin.add_view(UserView(User, db.session))


# db.drop_all()     # 删除表
# db.create_all()   # 建表

login_manager=LoginManager()
login_manager.session_protection='strong'   # 认证加密程度
login_manager.login_view='login'            # 处理登录的视图函数
login_manager.login_message='请登录'         # 登陆提示信息
login_manager.init_app(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/')
# @login_required
def index():
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


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


@app.route('/api/bloglist',methods=["GET","POST"])
# @login_required
def bloglist():
    articles = Article.query.all()
    model_to_dict(articles)     # list
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


# @app.route("/login", methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         username = request.form.get('username')
#         password = request.form.get('password')
#         # 数据库校验，用户密码是否正确
#         if username == 'admin' and password == 'admin':
#             session['user_id'] = 1
#             session['user_name'] = username
#             return redirect((url_for('index')))
#         else:
#             error = 'Invalid username/password'
#             return render_template('login.html', error=error)

@login_manager.user_loader
def load_user(user_id):
    print(user_id)  # 登录成功的时候会自动获取主键id
    return User.query.filter_by(id=user_id).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # 实例化form对象
    if request.method == "POST" and form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(name=username, password=password).first()
        if user:
            # 将用户信息注册到flask-login中
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('index'))
        else:
            flash("用户名或密码错误")
    return render_template('login.html', form=form)


@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@api.resource('/API/V1/blog')
class BlogApi(Resource):
    def __init__(self):
        super().__init__()
        self.result = {
            'method':'',
            'vaesion': 'v1',
            'data':'',
        }

    # 定义返回的数据
    def create_data(self, blog):
        result_data = {
            'id': blog.id,
            'title': blog.title,
            'content':blog.content,
        }
        return result_data

    def get(self):
        data = request.args
        id = data.get('id')
        result_data = {}
        if id:
            leave = Article.query.get(int(id))
            if leave is not None:
                result_data = self.create_data(leave)
        else:
            blogs = Article.query.all()
            result_data = []
            for leave in blogs:
                one = self.create_data(leave)
                result_data.append(one)
        self.result['method'] = 'get'
        self.result['data'] = result_data
        return jsonify(self.result)


if __name__ == '__main__':
    app.run(debug=True)
