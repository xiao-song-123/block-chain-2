from flask import Flask
from app.views.user import user_page
from app.extension import db
from app.models import User,Commodity
import os
import click

app = Flask('app')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app.secret_key = "songasdsadxzqwasdsafa"


@app.cli.command()
def forge():
    """Generate fake data."""
    db.drop_all()
    db.create_all()

    song = User(username="SHF",password="2063",identify_lable="admin",telephone="",gender="male",address="")
    li = User( username="LYC", password="7126", identify_lable="base", telephone="", gender="female", address="" )
    wang = User( username="WGL", password="2065", identify_lable="manu", telephone="", gender="male", address="" )
    yin = User( username="YZX", password="2071", identify_lable="transfer", telephone="", gender="male", address="" )

    db.session.add(song)
    db.session.add(li)
    db.session.add(wang)
    db.session.add(yin)
    db.session.commit()
    click.echo('Done.')

db.init_app(app)
app.register_blueprint(user_page)