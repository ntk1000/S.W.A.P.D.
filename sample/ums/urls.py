# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from ums import views

urlpatterns = patterns('',
	url(r'^user/edit/$', views.demouser_edit, name='demouser_edit'),
	url(r'^user/commit/(?P<demouser_id>\d+)/$', views.demouser_commit, name='demouser_commit'),
	url(r'^user/fin/(?P<demouser_id>\d+)/$', views.demouser_fin, name='demouser_fin'),
)