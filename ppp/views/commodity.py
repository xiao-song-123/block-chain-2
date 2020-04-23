from flask import Flask, render_template, url_for, request, redirect, session, flash,Blueprint
from ..models import User
from ..models import Commodity
from ..models import Blockchain
from ..extension import db
import time
from hashlib import sha256
import json
import qrcode
import ppp

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

                if user.identify_lable == 'system_administrator':
                   # return render_template('user/manager.html')
                    return redirect(url_for('manager_page.manager_jump'))
                elif user.identify_lable == 'manufacture':

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


@commodity_page.route('/modify_status/<id>', methods=['get', 'post'])# 生产商---修改商品的当前状态
def modify_status(id):
    com1 = Commodity.query.get(id)
    com1.status="待运输"
    db.session.commit()
    return render_template('addinfo/addinfo_manufacture.html', com=com1)


@commodity_page.route('/modify_status1/<id>', methods=['get', 'post'])# 物流公司---修改商品的当前状态
def modify_status1(id):
    com1 = Commodity.query.get(id)
    com1.status="运输中"
    db.session.commit()
    return render_template('addinfo/addinfo_logistics.html', com=com1)


@commodity_page.route('/modify_status2/<id>', methods=['get', 'post'])# 仓库---修改商品的当前状态
def modify_status2(id):
    com1 = Commodity.query.get(id)
    com1.status="入库"
    db.session.commit()
    return render_template('addinfo/addinfo_warehouse.html', com=com1)


@commodity_page.route('/addinfo_manufacture/<id><sel>', methods=['get', 'post'])# 生产商---增加相关信息
def addinfo_manufacture(id,sel):

    # print("1.此时sel:" + sel)
    commodities = Commodity.query.get(id)
    sel0=sel
    if request.method == 'GET':
        # print("2.此时sel:" + sel0)
        if sel0 == '0':
            return render_template('addinfo/addinfo_manufacture.html', com=commodities)
        elif sel0 == '1':
            return render_template('addinfo/addinfo_logistics.html', com=commodities)
        else:
            return render_template('addinfo/addinfo_warehouse.html', com=commodities)
    else:
        # print("3.此时sel:"+sel0)
        name_com = request.form.get('name_com')
        name_person = request.form.get('name_person')
        name_tel = request.form.get('name_tel')
        name_ini=request.form.get('name_ini')
        name_dec=request.form.get('name_dec')
        commodities.product_id=request.form.get('name_product_id')
        commodities.com=name_com
        commodities.person=name_person
        commodities.tel=name_tel
        commodities.ini=name_ini
        commodities.dec=name_dec
        time_array = time.localtime()  # 定义时间显示格式
        commodities.time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        db.session.commit()

        compute_hash(id)


        if sel0 == '0': #生产商
            print("转入生产商")
            coms = Commodity.query.filter(Commodity.status == "待发货").all()
            return render_template('goods/logistics_index.html', coms=coms)

        elif sel0 == '1' :#物流公司
            print("转入物流")
            coms = Commodity.query.filter(Commodity.status == "待运输").all()
            return render_template('logistics/logistics_index.html', coms=coms)
        else :         #仓库
            print("转入仓库")
            coms = Commodity.query.filter(Commodity.status == "运输中").all()
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
    # block = Blockchain.query.filter(Blockchain.commodity_id==id)
    one=Blockchain.query.filter(Blockchain.commodity_id==id,Blockchain.index==1).first()
    two = Blockchain.query.filter( Blockchain.commodity_id == id, Blockchain.index == 2 ).first()
    three = Blockchain.query.filter( Blockchain.commodity_id == id, Blockchain.index == 3 ).first()
    if request.method == 'GET':
        return render_template('goods/modify_detail.html',com=commodities,one=one,two=two,three=three)

@commodity_page.route('/detail0/<id>',methods=['GET', 'PoSt'])
def modify_detail0(id):
    commodities = Commodity.query.get( id )
    if request.method == 'GET':
        return render_template('goods/commodity_check.html',com=commodities)

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
        com = request.form.get('com')

        time_array = time.localtime()# 定义时间显示格式
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time_array)  # 把传入的元组按照格式，输出字符串

        ini=request.form.get('ini')

        dec = request.form.get('dec')
        person = request.form.get('person')
        tel = request.form.get('tel')


        goods = Commodity(name,price,number,type,status,product_id,data_pd,weight,com,time1,ini,dec,person,tel)
        db.session.add(goods)
        db.session.commit()
        coms = Commodity.query.all()
        flash('新增成功')
        return render_template('goods/logistics_index.html',coms=coms)




class Block:

    def __init__(self, commodity_id):
        self.nonce = 0
        print(commodity_id)
        self.commodity_id = commodity_id
        com = Commodity.query.filter(Commodity.id == self.commodity_id).first()
        self.name = com.name
        self.data = '单号:' + com.product_id + '\n公司名称:' + com.com + '\n初始地:' + com.ini + '\n目的地:' \
               + com.dec + '\n商品状态:' + com.status + '\n操作时间:' + com.time + '\n操作人:' + com.person + '\n联系方式:' + com.tel + '\n'


    def compute_hash(self):
        block_string = json.dumps(self.data + str(self.nonce))
        return sha256(block_string.encode()).hexdigest()

    def proof_of_work(self):
        self.nonce = 0

        computed_hash = self.compute_hash()
        while not computed_hash.startswith('0' * 4):
            self.nonce += 1
            computed_hash = self.compute_hash()
            print(computed_hash)
        print('最终结果是:{}, 随机数:{}'.format(computed_hash,self.nonce))

        return computed_hash


def compute_hash(id):

    block=Block(id)
    cur_hash =  block.proof_of_work()
    commodity_id = block.commodity_id
    commodity_name = block.name
    index = Blockchain.query.filter( Blockchain.commodity_id == commodity_id ).count() + 1
    print(index)
    pre=Blockchain.query.filter( Blockchain.index == index-1,  Blockchain.commodity_id == commodity_id).first()
    print(pre)
    data = block.data
    if index==1:
        pre_hash=00000
    else:
        pre_hash=pre.curhash
        print(pre_hash)
    nonce = block.nonce


    block = Blockchain( index, commodity_id, commodity_name, data, pre_hash, cur_hash, nonce )
    product = Commodity.query.get(id)
    if product.block_info:
        product.block_info = str(product.block_info)+'\n'+data
    else:
        product.block_info='商品id:' + str(product.id) + '\t商品名称:' + product.name + '\t商品价格:' + str(product.price)+ '\t商品数量:'  \
               + str(product.number) + '\t商品重量:' + str(product.weight) +'\n'+data

    db.session.add(block)
    db.session.commit()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.make( fit=True )
    qr.add_data(product.block_info)
    img = qr.make_image( fill_color="black", back_color="white" )
    src = ppp.app.static_folder + '\\images\\' + str(id) + ".png"
    img.save(src)
    # src = "../static/images/"+str(id)+".png"
    # img.save(src)




