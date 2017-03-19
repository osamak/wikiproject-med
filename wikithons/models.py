# -*- coding: utf-8  -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Use
from django.db import models


class Wikithon(models.Model):
    name = models.CharField("الاسم", max_length=100)
    description = models.TextField("الوصف", max_length=1000)
    date = models.DateField("التاريخ", auto_now=False)
    start_time = models.TimeField("وقت البداية", auto_now=False)
    end_time = models.TimeField("وقت النهاية", auto_now=False)
    location = models.CharField("المكان", max_length=100)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField("اسم الفريق", max_length=100)
    founder = models.ForeignKey(User, verbose_name="المؤسسـ/ـة",
                                related_name="teams_founded")
    members = models.ManyToManyField(User, verbose_name="العضوات والأعضاء",
                                     related_name="team_memberships")
    logo = models.ImageField("الشعار", null=True)
    articles = models.ManyToManyField('Article', verbose_name="المقالات")
    description = models.TextField("الوصف", max_length=1000)
    invitation_code = models.CharField("رمز الدعوة", max_length=10)
    is_deleted = models.BooleanField("محذوف؟", default=False)

    def __unicode__(self):
        return self.name
