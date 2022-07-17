# 本文件 用于初始化flask实例
import time
from flask import Flask, request, jsonify
from flask import render_template  # 用于渲染网页
from flask_login import LoginManager, login_user, login_required, logout_user  # 用于权限管理
from flask import Blueprint  # #
from views import blog_bp, user_bp  # #
from model import Blog, User

# 创建flask实例
app = Flask(__name__)
app.debug = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# 在app实例中注册蓝图
app.register_blueprint(blog_bp, url_prefix='/blog')
app.register_blueprint(user_bp, url_prefix='/user')

# 实现登录功能
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied'
login_manager.init_app(app)


@app.route('/login')
def login():
    return 'login page'


@login_manager.user_loader
def load_user(uid):
    user = User.objects(id=uid)  # 查找相关用户
    if len(user) > 0:
        curr_user = user[0]
        curr_user.id = user[0].id
        return curr_user


@user_bp.route('/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.objects(username=username, password=password)
    if len(user) > 0:
        cuur_user = user[0]
        cuur_user.id = user[0].id
        # 通过Flask-Login的login_user方法登录用户
        login_user(cuur_user)
        return jsonify({'mag': 'success'})
    else:
        return jsonify({'msg': 'wrong username or password'})


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'


# 开始实现相应的接口
# 一,发布微博接口
@blog_bp.route('/post', methods=['post'])  # 声明接口,第一个参数是接口地址,第二个参数是调用结构的方法
def post_blog():
    msg = request.form.get('blog', None)  # 获取微博的内容
    blog = Blog()  # 创建blog对象
    blog.msg = msg
    blog.time = int(time.time())
    blog.save()  # 保存到数据库
    return jsonify({'mag': 'success'})  # 返回json格式的对象,表示发布成功


# Postman接口测试工具,以后再学习
# 二,获取微博列表
@blog_bp.route('/list', method=['get'])
@login_required  # 进行权限限制
def blog_list():
    blogs = Blog.objects.order_by('-time').all()  # 按时间实现倒序排序
    result = []
    for item in blogs:
        result.append(item.get_json())
    return jsonify({'list': result})  # 把每个对象转换为json格式加入返回结果列表中


# 对template进行配置
@app.route('/')  # 将路由'/'和index.html模板文件绑定起来
def index():  # put application's code here
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
