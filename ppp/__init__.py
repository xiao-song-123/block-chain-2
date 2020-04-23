from flask import Flask
from ppp.extension import db
from ppp.views.login import login_page
from ppp.views.manager import manager_page
from ppp.views.user import user_page
from ppp.models import User,Commodity
from ppp.views.commodity import commodity_page
from ppp.views.logistics import logistics_page
import os

import click

app = Flask('ppp')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.secret_key = "lalskskskskksksjsj"

app.register_blueprint(login_page)
app.register_blueprint(manager_page)
app.register_blueprint(user_page)
app.register_blueprint(commodity_page)
app.register_blueprint(logistics_page)
db.init_app(app)


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create admin."""

    click.echo('Creating user...')
    user_admin = User(username=username, password='123', identify_lable='system_administrator',
                      telephone='1234', gender='保密', address='明向')
    user_admin.set_password(password)  # 设置密码
    db.session.add(user_admin)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def manufacture(username, password):
    """Create manufacture."""

    click.echo('Creating user...')
    user_manufacture = User(username=username, password='123', identify_lable='manufacture',
                            telephone='1234', gender='保密', address='明向')
    user_manufacture.set_password(password)  # 设置密码
    db.session.add(user_manufacture)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def logistics_director(username, password):
    """Create logistics_director."""
    click.echo('Creating user...')
    user_logistics_director = User(username=username, password='123', identify_lable='logistics_director',
                                   telephone='1234', gender='保密', address='明向')
    user_logistics_director.set_password(password)  # 设置密码
    db.session.add(user_logistics_director)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def warehouse_keeper(username, password):
    """Create warehouse_keeper."""

    click.echo('Creating user...')
    user_warehouse_keeper = User(username=username, password='123', identify_lable='warehouse_keeper',
                                 telephone='1234', gender='保密', address='明向')
    user_warehouse_keeper.set_password(password)  # 设置密码
    db.session.add(user_warehouse_keeper)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')
