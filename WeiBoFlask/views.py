from flask import Blueprint

# 创建蓝图,分别对应用户操作和博客操作
blog_bp = Blueprint('blog', __name__)
user_bp = Blueprint('user', __name__)
