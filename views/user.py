from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..models import User

#创建Blueprint实例
user_page=Blueprint('user_page',__name__)

@user_page.route('/users')
def users():
    if session.get('user_id'):
        users = User.query.all()
        return render_template('user/index.html', users=users)
    else:
        return redirect('/')


@user_page.route('/')
@user_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')
        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return redirect(url_for('user_page.users'))
        else:
            flash('登陆失败')
            return render_template('user/login.html')