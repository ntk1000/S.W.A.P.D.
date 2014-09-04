# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from ums import views

urlpatterns = patterns('',
    url(r'^demouser/$', views.demouser_list, name='demouser_list'),   # 一覧
    url(r'^demouser/add/$', views.demouser_edit, name='demouser_add'),  # 登録
    url(r'^demouser/mod/(?P<demouser_id>\d+)/$', views.demouser_edit, name='demouser_mod'),  # 修正
    url(r'^demouser/del/(?P<demouser_id>\d+)/$', views.demouser_del, name='demouser_del'),   # 削除
)