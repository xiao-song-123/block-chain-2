from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..models import User
from app.extension import db
from .config import Global
from .config import set_id
from .config import get_id


#创建Blueprint实例
user_page=Blueprint('user_page',__name__)

@user_page.route('/My Profile', methods=['GET', 'PoSt'])
def my_profile():
    user = User.query.filter( User.id == Global.u_id ).first()
    if request.method == 'GET':
        if session.get('user_id'):
            return render_template('user/manager_detail.html', users=user)
        else:
            return redirect('user/manager.html')


@user_page.route('/change_password', methods=['GET', 'PoSt'])
def change_password():
    user = User.query.filter(User.id==Global.u_id).first()
    print(user.id)
    if request.method == 'GET':
        return render_template('user/password.html')
    else:
        pwd = request.form.get('password')
        if pwd == user.password:
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            if password1 == password2:
                user.password = password1
                db.session.commit()
                return redirect(url_for('manager_page.manager_jump'))
            else:
                render_template('user/password.html')

            #return '0'
