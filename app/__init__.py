from flask import Flask
from app.extension import db
from app.views.login import login_page
from app.views.manager import manager_page
from app.views.user import user_page
from app.models import User,Commodity
from app.views.commodity import commodity_page
from app.views.logistics import logistics_page
import os



app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.secret_key = "lalskskskskksksjsj"

app.register_blueprint(login_page)
app.register_blueprint(manager_page)
app.register_blueprint(user_page)
app.register_blueprint(commodity_page)
app.register_blueprint(logistics_page)

db.init_app(app)