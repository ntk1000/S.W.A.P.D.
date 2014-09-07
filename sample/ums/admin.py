# -*- coding: utf-8 -*-
from django.contrib import admin
from ums.models import DemoUser

class DemoUserAdmin(admin.ModelAdmin):
	list_display = ('id','username','email','password')
	list_display = ('id','username','email','password')

admin.site.register(DemoUser,DemoUserAdmin)