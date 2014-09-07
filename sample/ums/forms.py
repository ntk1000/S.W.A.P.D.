# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras import widgets
from ums.models import DemoUser

class DemoUserForm(forms.ModelForm):
	username = forms.CharField(label=u'お名前')
	email = forms.EmailField(label=u'メールアドレス')
	password = forms.CharField(label=u'パスワード',widget=forms.PasswordInput())
	url = forms.URLField(label=u'URL',required=False)
	birth = forms.DateField(label=u'生年月日',widget=widgets.SelectDateWidget(),required=False)
	class Meta:
		model = DemoUser
		fields = ('username','email','password','url','birth')