# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras import widgets
import datetime
from ums.models import DemoUser
from ums.widgets import MonthYearWidget

class DemoUserForm(forms.ModelForm):
	help_base=u'{0}文字以内で入力してください'
	username_len=30
	email_len=75
	password_len=128

	username = forms.CharField(label=u'お名前',help_text=help_base.format(username_len),max_length=username_len)
	email = forms.EmailField(label=u'メールアドレス',help_text=u'有効なメールアドレスを'+help_base.format(email_len),max_length=email_len)
	password = forms.CharField(label=u'パスワード',help_text=help_base.format(password_len),widget=forms.PasswordInput(),max_length=password_len)
	password2 = forms.CharField(label=u'パスワード(再)',widget=forms.PasswordInput(),max_length=password_len)
	url = forms.URLField(label=u'URL',required=False)
	birth = forms.DateField(label=u'生年月',
		widget=MonthYearWidget(years=range(1900, datetime.datetime.today().year+1)),
		required=False)

	class Meta:
		model = DemoUser
		fields = ('username','email','password','password2','url','birth')

	def clean_password2(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password and password2:
			if password != password2:
				raise forms.ValidationError("パスワードが一致しません")
		return password2