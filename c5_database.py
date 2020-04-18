from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/python_admin'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


# 继承UserMixin类会让 User 类拥有几个用于判断认证状态的属性和方法，
# 其中最常用的是 is_authenticated 属性：如果当前用户已经登录，
# 那么 current_user.is_authenticated 会返回 True，
# 否则返回 False。有了 current_user 变量和这几个验证方法和属性，
# 我们可以很轻松的判断当前用户的认证状态。
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

#
#
# # 创建的数据库文件 data.db
# db.create_all()  # 重新生成表模式，那么需要先使用 db.drop_all()

# 增

# from app import Movie, User  # 导入模型类
# user = User(name='Grey Li')  # 创建一个 User 记录
# m1 = Movie(title='Leon', year='1994')  # 创建一个 Movie 记录
# m2 = Movie(title='Mahjong', year='1996')  # 再创建一个 Movie 记录
# # db.session.add(user)  # 把新创建的记录添加到数据库会话
# db.session.add(m1)
# db.session.add(m2)
#
# db.session.commit()  # 提交数据库会话，只需要在最后调用一次即可
#
# # 读取
# movie = Movie.query.first()  # 获取 Movie 模型的第一个记录（返回模型类实例）
# print(movie.title)  # 对返回的模型类实例调用属性即可获取记录的各字段数据
# print(movie.year)
# print(Movie.query.all())  # 获取 Movie 模型的所有记录，返回包含多个模型类实例的列表
# print(Movie.query.count())  # 获取 Movie 模型所有记录的数量
# print(Movie.query.get(1))  # 获取主键值为 1 的记录
# print(Movie.query.filter_by(title='Mahjong').first())  # 获取 title 字段值为 Mahjong 的记录
# print(Movie.query.filter(Movie.title == 'Mahjong').first())  # 等同于上面的查询，但使用不同的过滤方法

# # 改
# movie = Movie.query.get(2)
# movie.title = 'WALL-E'  # 直接对实例属性赋予新的值即可
# movie.year = '2008'
# db.session.commit()  # 注意仍然需要调用这一行来提交改动
#
# # 删
# movie = Movie.query.get(1)
# db.session.delete(movie)  # 使用 db.session.delete() 方法删除记录，传入模型实例
# db.session.commit()  # 提交改动
