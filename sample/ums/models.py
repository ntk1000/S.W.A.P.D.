# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class DemoUser(AbstractUser):
	"""DemoUser Model Class."""
	url = models.URLField(u'URL',blank=True,null=True)
	birthyear = models.PositiveSmallIntegerField(u'生年',blank=True,null=True,max_length=4)
	birthmonth = models.PositiveSmallIntegerField(u'月',blank=True,null=True,max_length=2)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'password']
	
	def __unicode__(self):
		return self.username

	class Meta:
		db_table = 'user'
		swappable = 'AUTH_USER_MODEL'
