# 本文件 使用manage对flask实例进行管理

# 注意修改两处位置
# 第一处 __init__.py
# from flask_script._compat import text_type  # zyb修改 由于版本问题,需要修改
# from flask._compat import text_type  # 未修改前
# 第二处 Edit Configurations 配置程序运行方式 Paramaters : runserver
from app import app
from flask_script import Manager

manage = Manager(app)
if __name__ == '__main__':
    manage.run()
