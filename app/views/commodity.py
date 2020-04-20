from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..models import User
from ..models import Commodity
from ..extension import db
#创建Blueprint实例
commodity_page=Blueprint('commodity_page',__name__)

@commodity_page.route('/')
@commodity_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            if session.get('user_id'):
                print(user.username)
                print(user.identify_lable)
                if user.identify_lable == 'system_administrator':
                   # return render_template('user/manager.html')
                    return redirect(url_for('manager_page.manager_jump'))
                elif user.identify_lable == 'manufacture':
                    print("成功")
                    return redirect(url_for('commodity_page.commodity_query'))
                elif user.identify_lable == 'logistics_director':
                    return redirect(url_for('logistics_page.commodity_query'))
                elif user.identify_lable == 'warehouse_keeper':
                    return redirect(url_for('logistics_page.commodity_query'))
        else:
            flash('登陆失败')
            return render_template('user/login.html')


@commodity_page.route('/logistics', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_query():      #全部查询
        coms = Commodity.query.all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/fahuo', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_fa():      #全部查询
        coms = Commodity.query.filter( Commodity.status == "待发货" ).all()
        return render_template('goods/commodity_fa.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/yunshu', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_yun():      #全部查询
        coms = Commodity.query.filter( Commodity.status == "待运输" ).all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/yunshu1', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_yun1():      #全部查询
        coms = Commodity.query.filter( Commodity.status == "待运输" ).all()
        return render_template('logistics/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/yunshuzhong', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_zhong():      #全部查询
        coms = Commodity.query.filter( Commodity.status == "运输中" ).all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/yunshuzhong1', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_zhong1():  # 全部查询
    coms = Commodity.query.filter( Commodity.status == "运输中" ).all()
    return render_template( 'base/index.html', coms=coms )  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/ruku', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_ru():      #全部查询
        coms = Commodity.query.filter( Commodity.status == "入库" ).all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@commodity_page.route('/commodity_search', methods=['POSt'])# 查询商品
def commodity_search():
    search_select = request.form.get('search_select')
    search_td = request.form.get('search_td')
    # print(search_select)
    # print(search_td)
    # print("查询成功&&&")

    if search_select == '0':
        coms = Commodity.query.all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。
    if search_select == '1':   # 按商品名查找
        coms = Commodity.query.filter(Commodity.name == search_td ).all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。
    if search_select == '3':   # 按商品名查找
        coms = Commodity.query.filter(Commodity.status == "待发货" ).all()
        return render_template('goods/logistics_index.html', coms=coms)
    else:                       # 按商品编号查找
        coms = Commodity.query.filter(Commodity.product_id == search_td).all()
        return render_template('goods/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。


@commodity_page.route('/modify_status/<id>', methods=['get', 'post'])# 修改商品的当前状态
def modify_status(id):
    com1 = Commodity.query.get(id)
    # print(com1.name)
    # print(com1.name)
    # print(com1.status)
    com1.status="待运输"
    db.session.commit()
    coms = Commodity.query.filter( Commodity.status == "待发货" ).all()
    return render_template('goods/logistics_index.html', coms=coms)

@commodity_page.route('/modify_status1/<id>', methods=['get', 'post'])# 修改商品的当前状态
def modify_status1(id):
    com1 = Commodity.query.get(id)
    # print(com1.name)
    # print(com1.name)
    # print(com1.status)
    com1.status="运输中"
    db.session.commit()
    coms = Commodity.query.filter( Commodity.status == "待运输" ).all()
    return render_template('logistics/logistics_index.html', coms=coms)

@commodity_page.route('/modify_status2/<id>', methods=['get', 'post'])# 修改商品的当前状态
def modify_status2(id):
    com1 = Commodity.query.get(id)
    # print(com1.name)
    # print(com1.name)
    # print(com1.status)
    com1.status="入库"
    db.session.commit()
    coms = Commodity.query.filter( Commodity.status == "运输中" ).all()
    return render_template('base/index.html', coms=coms)


@commodity_page.route('/modifycom/<id>',methods=['GET', 'PoSt'])  #记得改为'/modifycom/<id>'前提是前一个页面要传id
def modifycom(id):
    commodities = Commodity.query.get(id)
    if request.method == 'GET':
        return render_template('goods/modifycom.html',com=commodities)
    else:
        name = request.form.get('name')
        price = request.form.get('price')
        number = request.form.get('number')
        type = request.form.get('type')
        product_id = request.form.get('product_id')
        data_pd = request.form.get('data_pd')
        weight = request.form.get('weight')

        commodities.name = name
        commodities.price = price
        commodities.number = number
        commodities.type = type
        commodities.product_id = product_id
        commodities.data_pd = data_pd
        commodities.weight = weight

        db.session.commit()
        flash('修改成功')
        coms = Commodity.query.all()
        return render_template('goods/logistics_index.html',coms=coms)

@commodity_page.route('/detail/<id>',methods=['GET', 'PoSt'])
def modify_detail(id):
    commodities = Commodity.query.get( id )
    if request.method == 'GET':
        return render_template('goods/modify_detail.html',com=commodities)

@commodity_page.route('/addcommodity', methods=['GET', 'PoSt'])
def addcommodity():
    if request.method == 'GET':
        return render_template('goods/addcommodity.html')
    else:
        name = request.form.get('name')
        price = request.form.get('price')
        number = request.form.get('number')
        type = request.form.get('type')
        status = request.form.get('status')
        product_id = request.form.get('product_id')
        data_pd = request.form.get('data_pd')
        weight = request.form.get('weight')

        goods = Commodity(name,price,number,type,status,product_id,data_pd,weight)
        db.session.add(goods)
        db.session.commit()
        coms = Commodity.query.all()
        flash('新增成功')
        return render_template('goods/logistics_index.html',coms=coms)


