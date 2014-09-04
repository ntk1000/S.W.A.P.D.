# -*- coding: utf-8 -*-
from django.forms import ModelForm
from ums.models import DemoUser

class DemoUserForm(ModelForm):
    class Meta:
        model = DemoUser
        fields = ('id','name','email','passw','url','birthdate')