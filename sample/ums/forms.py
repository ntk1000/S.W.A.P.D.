# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras import widgets
import datetime
from ums.models import DemoUser

class DemoUserForm(forms.ModelForm):
	help_base=u'{0}文字以内で入力してください'
	username_len=30
	email_len=75
	password_len=128

	username = forms.CharField(label=u'お名前',help_text=help_base.format(username_len),max_length=username_len)
	email = forms.EmailField(label=u'メールアドレス',help_text=u'有効なメールアドレスを'+help_base.format(email_len),max_length=email_len)
	password1 = forms.CharField(label=u'パスワード',help_text=help_base.format(password_len),widget=forms.PasswordInput(),max_length=password_len)
	password2 = forms.CharField(label=u'パスワード(再)',widget=forms.PasswordInput(),max_length=password_len)
	url = forms.URLField(label=u'URL',required=False)
	birth = forms.DateField(label=u'生年月日',widget=widgets.SelectDateWidget(years=range(1900, datetime.datetime.today().year+1)),required=False)

	class Meta:
		model = DemoUser
		fields = ('username','email','password1','password2','url','birth')

	def __init__(self, *args, **kwargs):
		super(DemoUserForm, self).__init__(*args, **kwargs)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError("パスワードが一致しません")
		return password2

	# def save(self, commit=True):
	# 	self.demouser.set_password(self.cleaned_data["password1"])
	# 	if commit:
	# 		self.demouser.save()
	# 	return self.demouser