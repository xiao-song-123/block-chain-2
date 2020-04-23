from werkzeug.security import generate_password_hash, check_password_hash

from ppp.extension import db
from _datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    identify_lable = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password, password)  # 返回布尔值

    def __init__(self, username, password, identify_lable, telephone, gender, address):
        self.username = username
        self.password = password
        self.identify_lable = identify_lable
        self.telephone = telephone
        self.gender = gender
        self.address = address

    def __repr__(self):
        return '<User %r>' % self.username


class Commodity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    number = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(100), nullable=False)  # 商品状态
    product_id = db.Column(db.String(255), nullable=False)  # 编号（ 物流：运单号  仓库：仓库编号）
    data_pd = db.Column(db.DateTime, index=True, default=datetime.day)
    weight = db.Column(db.String(255), nullable=True)
    com = db.Column(db.String(50), nullable=False)  # 操作的公司名
    time = db.Column(db.String(100), nullable=False, )  # 操作时间，需要获取当前系统时间

    ini = db.Column(db.String(255))  # 初始地
    dec = db.Column(db.String(255))  # 目的地
    person = db.Column(db.String(20), nullable=False)  # 操作人
    tel = db.Column(db.String(30), nullable=False)  # 操作人联系方式
    block_info = db.Column(db.Text, nullable=True)  # 二维码信息

    # 后面有注释的字段为需要修改的字段，不可为空，大家共同修改

    def __init__(self, name, price, number, type, status, product_id, data_pd, weight, com, time, ini, dec, person,
                 tel):
        self.name = name
        self.price = price
        self.number = number
        self.type = type
        self.status = status
        self.product_id = product_id
        self.data_pd = data_pd
        self.weight = weight
        self.com = com
        self.time = time
        self.ini = ini
        self.dec = dec
        self.person = person
        self.tel = tel

    def __repr__(self):
        return '<Commodity %r>' % self.name


class Blockchain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(100), nullable=False)  # 索引
    commodity_id = db.Column(db.Integer, nullable=False)
    commodity_name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=True)
    prehash = db.Column(db.String(255), nullable=True)
    curhash = db.Column(db.String(255), nullable=True)
    nonce = db.Column(db.String(255), nullable=True)  # 随机数

    def __init__(self, index, commodity_id, commodity_name, data, prehash, curhash, nonce):
        self.index = index
        self.commodity_id = commodity_id
        self.commodity_name = commodity_name
        self.data = data
        self.prehash = prehash
        self.curhash = curhash
        self.nonce = nonce
