# -*- coding:utf-8 -*-
# @Time : 2020/6/1 21:59
# @Author : AX
# @File : cookie_set.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


from flask import request, make_response, jsonify

# cookie set
import json


@app.route('/pos')
def pose():
    dis = dict()
    dis['cookies'] = 'dddd'
    dis['username'] = 'AX'
    return dis


if __name__ == '__main__':
    app.run()
