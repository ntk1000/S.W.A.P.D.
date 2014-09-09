# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class DemoUser(AbstractUser):
	"""DemoUser Model Class."""
	userfullname = models.CharField(u'お名前',blank=False,null=False,max_length=50)
	url = models.URLField(u'URL',blank=True,null=True)
	birth = models.DateField(u'生年月',blank=True,null=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'password']
	
	def __unicode__(self):
		return self.userfullname

	class Meta:
		db_table = 'user'
		swappable = 'AUTH_USER_MODEL'