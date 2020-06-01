from flask import Flask, url_for, escape

app = Flask(__name__)


@app.route('/')
def index_d():
    hello_world = 'helloWorld'
    return hello_world


@app.route('/index')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/username/<username>')
def show_profile(username):
    return 'It\'s {0}\'s profile'.format(escape(username))


# 使用methods数组来指定请求的方式，同时需要从flask里引入request
from flask import request


@app.route('/test', methods=['GET', 'POST'])
def show_request_method():
    # 可以通过request.method 拿到请求的方式
    if request.method == 'POST':
        return 'this is a POST method'
    if request.method == 'GET':
        return 'this is a GET method'


if __name__ == '__main__':
    # app.run()
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('profile', username='AX'))
