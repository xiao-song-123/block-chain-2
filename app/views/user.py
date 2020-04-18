from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..models import User
from app.extension import db

#创建Blueprint实例
user_page=Blueprint('user_page',__name__)

@user_page.route('/users')
def users():
    if session.get('user_id'):
        users = User.query.all()
        user_id = session['user_id']
        return render_template('user/index.html', users=users ,user_id=user_id)
    else:
        return redirect('/')

@user_page.route('/users/detail')
def users_message():
    if session.get('user_id'):
        users = User.query.filter_by( username='admin' ).first()
        return render_template('user/index.html',users=users)
    else:
        return redirect('/')

@user_page.route('/users/<id>', methods=['GET', 'PoSt'])
def change_password(id):
    user = User.query.get(id)

    if request.method == 'GET':
        return render_template('user/password.html', user=user)
    else:
        pwd = request.form.get('password1')
        if pwd == user.password:
            password1 = request.form.get('password2')
            password2 = request.form.get('password3')
            if password1 == password2:
                user.password = password1
                db.session.commit()
                return redirect(url_for('user_page.users'))

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
            #session['user_username'] = user.username
            return redirect(url_for('user_page.users'))
            # return '1'
        else:
            flash('登陆失败')
            return render_template('user/login.html')
            #return '0'
