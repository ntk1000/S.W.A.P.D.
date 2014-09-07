# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras import widgets
from ums.models import DemoUser

class DemoUserForm(forms.ModelForm):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	birth = forms.DateField(widget=widgets.SelectDateWidget())
	class Meta:
		model = DemoUser
		fields = ('username','email','password','url','birth')