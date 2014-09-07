# -*- coding: utf-8 -*-
from django import forms
from ums.models import DemoUser

class DemoUserForm(forms.ModelForm):
	class Meta:
		model = DemoUser
		fields = ('username','email','password','url','birthyear','birthmonth')