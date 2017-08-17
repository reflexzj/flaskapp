#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import render_template, Blueprint
from flask_login import login_required
from models import *



blueprint = Blueprint('order', __name__, static_folder='../static/order')
# Basic_Info_Form = Basic_Info_Form()
# Avator = Avator()


@blueprint.route('/index/<int:page>')
@login_required
def blank(page):
    """
        路由：index.html
        初始主页，即分页第一页
        分页显示了所有数据
    """
    # Professor.get_many(11, 1589, 'flaskapp/static/order/avator').all()
    pagination = basic_info.query.paginate(page=page, per_page=6, error_out=False)
    return render_template('order/index.html', title='三螺旋', pagination=pagination)


# @blueprint.route('/searchbox')
# @login_required
# def searchbox():
#     """
#     用户自定义搜索，主要是根据专家（导师）和学校搜索
#     :return: 专家陈列页面，指定学校陈列页
#     """
#     info_text = select_box()
#     return render_template('order/search.html', title='三螺旋', pagination=info_text, con=info_text)


# @blueprint.route('/insti_search/<int:page>')
# @login_required
# def insti_search(page):
#     """
#     对机构信息的查看
#     :return:
#     """
#     if not page:
#         page = 1
#     lab_info = Lab_Form()
#     pagination = lab_info.select_info().paginate(page=page, per_page=6, error_out=False)
#     return render_template('laboratory/lab_index.html', title='三螺旋', pagination=pagination)


@blueprint.route('/search/<int:page>')
@login_required
def search(page):
    """
    :param page: 结果从第几页展示
    :return: 根据条件进行模糊匹配的结果陈列
    """
    if not page:
        page = 1
    info_address_list, info_address = Basic_Info_Form.select_address_radio(page=page)
    print info_address_list
    return render_template('order/search.html', title='三螺旋', pagination=info_address_list, address=info_address)





@blueprint.route('/order_confirm')
@login_required
def about():
    """
        路由：order_confirm.html
        跳转订单确认页面
    """
    return render_template('order/order_confirm.html')


@blueprint.route('/order_list')
@login_required
def order():
    """
        路由：order_list.html
        跳转订单列表页面
    """
    return render_template('order/order_list.html')


@blueprint.route('/<string:con>/<int:page>')
@login_required
def add(con, page):
    """
        路由：add.html
        按地址或公司名查询
        返回结果在add.html中显示
    """
    # pagination = search_engine(area, page)
    pagination = select_paginate_by_add(con, page)
    return render_template('order/add.html', title="三螺旋", pagination=pagination, name=con)


@blueprint.route('/demand')
@login_required
def demand():
    """
        路由：
        触发搜索
        返回add方法
    """
    content = request.args.get('requirement')
    return add(content, 1)


@blueprint.route('/profile/<int:id>')
@login_required
def profile(id):
    info = Professor(id)
    return render_template('order/profile.html', title="三螺旋", info=info)

@blueprint.route('/lab_infoshow/<string:name>')
def lab_infoshow(name):
    labform = Lab_Form()
    info = labform.get_info(name=name)
    return render_template('laboratory/lab_infoshow.html', title="三螺旋", info=info)

