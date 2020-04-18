from flask import render_template, Flask

from c5_database import User
app = Flask(__name__)


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('c6_404.html'), 404  # 返回模板和状态码

#
# # 后面我们创建的任意一个模板，都可以在模板中直接使用
# @app.context_processor
# def inject_user():  # 函数名可以随意修改
#     user = User.query.first()
#     return dict(user=user)  # 需要返回字典，等同于return {'user': user}
#
#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
#
# @app.route('/')
# def index():
#     movies = Movie.query.all()
#     return render_template('index.html', movies=movies)
#
#
