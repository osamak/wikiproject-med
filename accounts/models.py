# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, verbose_name=u"المستخدمـ/ـة")
    name = models.CharField('الاسم', max_length=100)
    twitter = models.CharField('حساب تويتر', max_length=20, blank=True)
    bio = models.TextField('نبذرة ذاتية')
    avatar = models.ImageField('الصورة الشخصية', null=True, blank=True)

    def __unicode__(self):
        return self.name
