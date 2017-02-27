# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from wikithon.models import Wikithons

class Profile(UserenaBaseProfile):
    wikithon = models.ForeignKey(Wikithons, verbose_name='الويكيثون')
    user = models.OneToOneField(User, verbose_name='اسم المستخدم')
    name = models.CharField(max_length=100, verbose_name='الاسم')
    email = models.EmailField(max_length=100, verbose_name='البريد الإلكتروني')
    twitter = models.CharField(max_length=50, null=True, verbose_name='حساب تويتر')
    bio = models.TextField(null=True, verbose_name='الوصف')
    avatar = models.ImageField(null=True, verbose_name='الصورة الشخصية')
    def __unicode__(self):
        return self.name