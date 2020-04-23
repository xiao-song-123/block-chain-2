from flask import Flask, render_template, url_for, request, redirect, session, flash, Blueprint
from ..models import User
from ppp.extension import db
from .config import Global
from .config import set_id
from .config import get_id

# 创建Blueprint实例
user_page = Blueprint('user_page', __name__)


@user_page.route('/My Profile', methods=['GET', 'PoSt'])
def my_profile():
    user = User.query.filter(User.id == Global.u_id).first()
    if request.method == 'GET':
        if session.get('user_id'):
            return render_template('user/manager_detail.html', users=user)
        else:
            return redirect('user/manager.html')


# 判断修改密码是否正确
@user_page.route('/check_pas', methods=['GET', 'PoSt'])
def check_pas():
    user = User.query.filter(User.id == Global.u_id).first()
    pwd = request.form.get('password')
    if user.validate_password(pwd):
        return '1'
    else:
        return '0'


@user_page.route('/change_password', methods=['GET', 'PoSt'])
def change_password():
    user = User.query.filter(User.id == Global.u_id).first()
    print(user.id)
    if request.method == 'GET':
        return render_template('user/password.html')
    else:
        pwd = request.form.get('password')
        if user.validate_password(pwd):
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            if password1 == password2:
                user.set_password(password1)
                db.session.commit()
                if user.identify_lable == 'system_administrator':
                    return redirect(url_for('manager_page.manager_jump'))
                elif user.identify_lable == 'manufacture':
                    return redirect(url_for('commodity_page.commodity_query'))
                elif user.identify_lable == 'logistics_director':
                    return redirect(url_for('commodity_page.commodity_yun1'))
                elif user.identify_lable == 'warehouse_keeper':
                    return redirect(url_for('commodity_page.commodity_zhong1'))

            else:
                return render_template('user/password.html')
        else:
            return render_template('user/password.html')


# 链接跳转
@user_page.route('/change_password_jump', methods=['GET', 'PoSt'])
def change_password_jump():
    user = User.query.filter(User.id == Global.u_id).first()
    print(user.id)
    if request.method == 'GET':
        if user.identify_lable == 'system_administrator':
            return redirect(url_for('manager_page.manager_jump'))
        elif user.identify_lable == 'manufacture':
            return redirect(url_for('commodity_page.commodity_query'))
        elif user.identify_lable == 'logistics_director':
            return redirect(url_for('commodity_page.commodity_yun1'))
        elif user.identify_lable == 'warehouse_keeper':
            return redirect(url_for('commodity_page.commodity_zhong1'))
    else:
        return render_template('user/password.html')
