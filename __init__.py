from flask import Flask
form .views.user import user_page
from .extension import db

app = Flask('block-chain-2')

app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql+pymysql://root:123456@127.0.0.1/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "songasdsadxzqwasdsafa"

db.init_app(app)
app.register_blueprint(user_page)