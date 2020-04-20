from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..extension import db
from ..models import User, Commodity

#创建Blueprint实例
logistics_page = Blueprint('logistics_page',__name__)


@logistics_page.route('/logistics1', methods=['get','POST'])# 查询运输状态为--“待运输”的商品信息
def commodity_query():      #全部查询
        coms = Commodity.query.filter(Commodity.status == "待运输").all()
        return render_template('logistics/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。

@logistics_page.route('/commodity_search1', methods=['PoSt'])# 查询商品
def commodity_search():
    search_select = request.form.get('search_select')
    search_td = request.form.get('search_td')
    # print(search_select)
    # print(search_td)
    # print("查询成功&&&")

    if search_select == '0':
        coms = Commodity.query.filter(Commodity.status == '待运输').all()
        return render_template('logistics/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。
    if search_select == '1':   # 按商品名查找
        coms = Commodity.query.filter(Commodity.name == search_td , Commodity.status == '待运输').all()
        return render_template('logistics/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。
    else:                       # 按商品编号查找
        coms = Commodity.query.filter(Commodity.product_id == search_td, Commodity.status == '待运输').all()
        return render_template('logistics/logistics_index.html', coms=coms)  # Flask 会在 templates 文件夹内寻找模板。


@logistics_page.route('/modify_status1/<id>', methods=['get', 'post'])# 修改商品的当前状态
def modify_status(id):
    com1 = Commodity.query.get(id)
    # print(com1.name)
    # print(com1.name)
    # print(com1.status)
    com1.status="运输中"
    db.session.commit()
    coms = Commodity.query.filter(Commodity.status == "待运输").all()
    return render_template('logistics/logistics_index.html', coms=coms)



