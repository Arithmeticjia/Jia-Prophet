from flask import Flask
from flask import jsonify,request
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time

app = Flask(__name__)


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
