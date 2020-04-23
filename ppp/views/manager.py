from flask import render_template, Blueprint, request, redirect, session, flash, url_for
from ..models import User
from ..extension import db

manager_page = Blueprint('manager_page', __name__)


# 跳转到管理员主页面
@manager_page.route('/manager_jump')
def manager_jump():
    if session.get('user_id'):
        users = User.query.all()
        return render_template('user/manager.html', users=users)
    else:
        return redirect('/')


# 跳转到增加用户界面
@manager_page.route('/manager_add_jump')
def manager_add_jump():
    return render_template('user/manager_add.html')


# 跳转到修改用户界面
@manager_page.route('/manager_update_save', methods=['GET', 'PoSt'])
def manager_update_save():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter(User.username == username).first()
        if user:
            session['user_id'] = user.id
            return '1'
        else:
            return '0'
    else:
        return render_template('user/manager.html')


@manager_page.route('/manager_update_jump', methods=['GET', 'PoSt'])
def manager_update_jump():
    if request.method == 'GET':
        if session.get('user_id'):
            id = session.get('user_id')
            users = User.query.filter(User.id == id).first()
            return render_template('user/manager_update.html', users=users)
        else:
            return redirect('user/manager.html')


# 跳转到用户详情界面
@manager_page.route('/manager_detail_save', methods=['GET', 'PoSt'])
def manager_detail_save():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter(User.username == username).first()
        if user:
            session['user_id'] = user.id
            return '1'
        else:
            return '0'
    else:
        return render_template('user/manager.html')


@manager_page.route('/manager_detail_jump', methods=['GET', 'PoSt'])
def manager_detail_jump():
    if request.method == 'GET':
        if session.get('user_id'):
            id = session.get('user_id')
            users = User.query.filter(User.id == id).first()
            return render_template('user/manager_detail.html', users=users)
        else:
            return redirect('user/manager.html')


# 新增用户函数
@manager_page.route('/')
@manager_page.route('/manager_add', methods=['GET', 'PoSt'])
def manager_add():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        identify_label = request.form.get('identify_label')
        telephone = request.form.get('telephone')
        gender = request.form.get('gender')
        address = request.form.get('address')
        admin = User(username=username, password='123', identify_lable=identify_label, telephone=telephone,
                     gender=gender, address=address)
        admin.set_password(password)
        if username:
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for('manager_page.manager_jump'))
        else:
            return redirect(url_for('manager_page.manager_jump'))
    else:
        return render_template('user/manager.html')


# 删除用户函数
@manager_page.route('/manager_delete', methods=['GET', 'PoSt'])
def manager_delete():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter(User.username == username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return '1'
        else:
            # return render_template('user/manager_add.html')
            return '0'
    else:
        return render_template('user/manager.html')


# 修改用户信息函数
@manager_page.route('/')
@manager_page.route('/manager_update', methods=['GET', 'PoSt'])
def manager_update():
    if request.method == 'POST':
        if session.get('user_id'):
            id = session.get('user_id')
            users = User.query.filter(User.id == id).first()
            users.username = request.form.get('username')

            users.identify_label = request.form.get('identify_label')
            users.telephone = request.form.get('telephone')
            users.gender = request.form.get('gender')
            users.address=request.form.get('address')
            db.session.commit()
            return redirect(url_for('manager_page.manager_jump'))
        else:
            # return render_template('user/manager_add.html')
            return redirect(url_for('manager_page.manager_update_jump'))
    else:
        return render_template('user/manager.html')


# 用户信息界面
@manager_page.route('/')
@manager_page.route('/manager_detail', methods=['GET', 'PoSt'])
def manager_detail():
    if request.method == 'POST':
        if session.get('user_id'):
            return redirect(url_for('manager_page.manager_jump'))
        else:
            # return render_template('user/manager_add.html')
            return redirect(url_for('manager_page.manager_detail_jump'))
    else:
        return render_template('user/manager.html')
