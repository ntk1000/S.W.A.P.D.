# -*- coding: utf-8 -*-
from django.contrib import admin
from ums.models import DemoUser

class DemoUserAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','passw','url','birthdate')
	list_display = ('id','name','email','passw','url','birthdate')

admin.site.register(DemoUser,DemoUserAdmin)