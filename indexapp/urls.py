#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# Author: zxw
# @Time :2020/11/6 12:28

from django.urls import path
from . import views

# 需要加上app_name传参
app_name = 'indexapp'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]