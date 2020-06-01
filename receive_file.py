# -*- coding:utf-8 -*-
# @Time : 2020/6/1 21:48
# @Author : AX
# @File : receive_file.py
# @Software: PyCharm
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user = request.headers.get('User-Agent')
    print(request.headers)
    print(user)
    return 'hello'


@app.route('/receivefile', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save('/static/the_file.txt')


if __name__ == '__main__':
    app.run()
