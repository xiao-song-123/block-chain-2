from app.extension import db
from _datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True,nullable=False)
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

class Commodity( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 100 ), unique=True, nullable=False )
    price = db.Column( db.Integer, nullable=False )
    number = db.Column( db.Integer, nullable=False )
    type = db.Column( db.String( 100 ), nullable=True )
    status = db.Column( db.String( 100 ), nullable=True )
    product_id = db.Column( db.String( 255 ), nullable=True )
    data_pd = db.Column( db.DateTime,index=True,default=datetime.utcnow )
    weight = db.Column(db.String(255),nullable=True )

    def __repr__(self):
        return '<User %r>' % self.username
