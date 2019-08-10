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
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:980612ssj@%@101.132.70.184:3306/MyBlog"
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run()
