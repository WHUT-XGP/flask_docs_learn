from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 定义一个常规路由 http://127.0.0.1:5000/hello
@app.route('/hello')
def index():
    return 'here is hello'


# 定义动态路由：
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is %s' % username


# 可以使用int: string:等方式指定属性，不符合则返回404
# 转化器类型有string(默认) int(正整数) float(正实数) path(类似string 但是可以包含/) uuid(接受uuid字符串)?
@app.route('/postId/<int:id>')
def show_post_id(id):
    return 'postId is %s' % (id + 1)


# path演示
@app.route('/post/<path:path>')
def show_path(path):
    return 'the path is %s' % path


# 唯一的URL / 重定向行为  http://127.0.0.1:5000/count/ （自动补全/) 思考对比：文件夹和文件
@app.route('/count/')
def show_count():
    return 'the / count'


from flask import render_template

# @app.route('/render')
# def render_html():
#     return render_template('hello.html')


from flask import request


# 以表单的形式拿到数据：
@app.route('/postdata', methods=['GET', 'POST'])
def form_data():
    flag = True
    if request.form['username'] == '123':
        print('username yes')
        flag = False
    if request.form['password'] == 'xxx':
        print('password yes')
        flag = False
    if flag:
        return 404
    else:
        return 'ok'


# 可以用参数request.args.get('param name')的形式拿到params的数据：
@app.route('/login', methods=['GET', 'POST'])
def params_show():
    s = ''
    username = request.args.get('username')
    s = s + username
    password = request.args.get('password')
    s = s + password
    return s


if __name__ == '__main__':
    # url_for('/static', filename='style.css')
    app.run()
