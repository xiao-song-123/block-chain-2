from flask import render_template, Blueprint, request, redirect, session, flash, url_for
from ..models import User
from .config import Global
from .config import set_id
from .config import get_id


login_page = Blueprint('login_page', __name__)


@login_page.route('/')
@login_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html', msg='')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        user = User.query.filter(User.username == name).first()
        if user and user.validate_password(pwd):
            session['user_id'] = user.id
            set_id(session['user_id'])
            print(Global.u_id)
            if session.get('user_id'):
                if user.identify_lable == 'system_administrator':
                    # return render_template('user/manager.html')
                    return redirect(url_for('manager_page.manager_jump'))
                elif user.identify_lable == 'manufacture':
                    return redirect(url_for('commodity_page.commodity_query'))
                elif user.identify_lable == 'logistics_director':
                    return redirect(url_for('commodity_page.commodity_yun1'))
                elif user.identify_lable == 'warehouse_keeper':
                    return redirect(url_for('commodity_page.commodity_zhong1'))
        else:
            return render_template('user/login.html')


# 判断用户名和密码是否正确
@login_page.route('/check_user', methods=['GET', 'PoSt'])
def check_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter(User.username == username).first()
    if user and user.validate_password(password):
        return '1'
    else:
        return '0'
