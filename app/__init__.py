from flask import Flask

from app.views.manager import user_page
from .extension import db

app = Flask('first_flask')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:lichao199877@127.0.0.1/block_chain'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "lalskskskskksksjsj"

app.register_blueprint(user_page)

db.init_app(app)