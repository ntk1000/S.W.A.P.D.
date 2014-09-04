# -*- coding: utf-8 -*-
from django.db import models

class DemoUser(models.Model):
	"""DemoUser Model Class."""
	name = models.CharField(u'名前',max_length=50)
	email = models.EmailField(u'メールアドレス')
	passw = models.CharField(u'パスワード',max_length=50)
	url = models.URLField(u'URL',null=True)
	birthdate = models.DateField(u'生年月',null=True)
	
	def __unicode__(self):
		return self.name