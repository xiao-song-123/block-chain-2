from app.extension import db
from _datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    identify_lable=db.Column(db.String(100),nullable=False)
    telephone=db.Column(db.String(50),nullable=True)
    gender=db.Column(db.String(255),nullable=True)
    address=db.Column(db.String(255),nullable=True)


    def __init__(self, username,password,identify_lable,telephone,gender,address):
        self.username = username
        self.password = password
        self.identify_lable=identify_lable
        self.telephone=telephone
        self.gender=gender
        self.address=address
    def __repr__(self):
        return '<User %r>' % self.username


class Commodity( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 100 ),nullable=False)
    price = db.Column( db.Integer)
    number = db.Column( db.Integer, nullable=False)
    type = db.Column( db.String( 100 ), nullable=True )
    status = db.Column( db.String( 100 ), nullable=False)  #商品状态
    product_id = db.Column( db.String(255), nullable=False) #编号（ 物流：运单号  仓库：仓库编号）
    data_pd = db.Column( db.DateTime,index=True,default=datetime.utcnow )
    weight = db.Column(db.String(255),nullable=True )
    com = db.Column(db.String(50), nullable=False)  #操作的公司名
    time = db.Column(db.TIMESTAMP, nullable=False)  #操作时间，需要获取当前系统时间
    person = db.Column(db.String(20), nullable=False) #操作人
    tel = db.Column(db.String(30), nullable=False)  #操作人联系方式
    # 后面有注释的字段为需要修改的字段，不可为空，大家共同修改

    def __init__(self, name, price, number, type, status, product_id,data_pd,weight,com,time,person,tel):
        self.name = name
        self.price = price
        self.number = number
        self.type = type
        self.status = status
        self.product_id = product_id
        self.data_pd=data_pd
        self.weight=weight
        self.com = com
        self.time = time
        self.person = person
        self.person = tel

    def __repr__(self):
        return '<Commodity %r>' % self.name


