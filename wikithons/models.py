# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from .managers import WikithonQuerySet

class Location(models.Model):
    name = models.CharField("الاسم", max_length=100)
    description = models.TextField("تفاصيل المكان", help_text='الوصف مثلا', blank=True)
    long_position   = models.DecimalField ("خط الطول", max_digits=10, decimal_places=5, blank=True, null=True)
    lat_position   = models.DecimalField("خط العرض", max_digits=10, decimal_places=5, blank=True, null=True)
    google_maps_url = models.URLField("رابط خرائط غوغل")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "مكان"
        verbose_name_plural = "أماكن"

class Wikithon(models.Model):
    name = models.CharField("الاسم", max_length=100)
    description = models.TextField("الوصف", max_length=1000)
    date = models.DateField("التاريخ", auto_now=False)
    start_time = models.TimeField("وقت البداية", auto_now=False)
    end_time = models.TimeField("وقت النهاية", auto_now=False)
    location = models.ForeignKey(Location, null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="الموقع")
    announcement_date = models.DateTimeField("تاريخ الإعلان",
                                             auto_now=False,
                                             null=True, blank=True)
    submission_date = models.DateTimeField("تاريخ الإرسال",
                                           auto_now_add=True)
    modification_date = models.DateTimeField("تاريخ التعديل",
                                             auto_now=True)
    available_to_choices = (
        ('A', u'الجميع'),
        ('F', u'النساء'),
        ('M', u'الرجال'),
        )
    available_to = models.CharField("متاح لـ", max_length=1,
                                    default="A",
                                    choices=available_to_choices)
    objects = WikithonQuerySet.as_manager()

    def is_announced(self):
        if self.announcement_date:
            return self.announcement_date < timezone.now()
        else:
            return True

    def is_attendable(self):
        end_datetime = datetime.combine(self.date, self.end_time)
        end_datetime = timezone.make_aware(end_datetime,
                                           timezone.get_current_timezone())
        if self.is_announced() and end_datetime > timezone.now():
            return True
        else:
            return False

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "ويكيثون"
        verbose_name_plural = "ويكيثونات"

class Team(models.Model):
    name = models.CharField("اسم الفريق", max_length=100)
    wikithon = models.ForeignKey(Wikithon, verbose_name="الويكيثون")
    founder = models.ForeignKey(User, verbose_name="المؤسسـ/ـة",
                                related_name="teams_founded")
    members = models.ManyToManyField(User, verbose_name="العضوات والأعضاء",
                                     related_name="team_memberships")
    logo = models.ImageField("الشعار")
    articles = models.ManyToManyField('articles.Article', verbose_name="المقالات")
    description = models.TextField("الوصف")
    invitation_code = models.CharField("رمز الدعوة", max_length=10)
    is_deleted = models.BooleanField("محذوف؟", default=False)
    submission_date = models.DateTimeField("تاريخ الإرسال",
                                           auto_now_add=True)
    modification_date = models.DateTimeField("تاريخ التعديل",
                                             auto_now=True)

    def get_member_count(self):
        return self.members.count()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "فريق"
        verbose_name_plural = "فرق"

class Registration(models.Model):
    wikithon = models.ForeignKey(Wikithon, verbose_name="الويكيثون")
    user = models.ForeignKey(User, verbose_name="المستخدمـ/ـة")
    articles = models.ManyToManyField('articles.Article',
                                      verbose_name="المقالات")
    is_deleted = models.BooleanField("محذوف؟", default=False)
    submission_date = models.DateTimeField("تاريخ الإرسال",
                                           auto_now_add=True)
    modification_date = models.DateTimeField("تاريخ التعديل",
                                             auto_now=True)
    def __unicode__(self):
        return "{}'s registration in {}".format(self.user.username,
                                                self.wikithon.name)
    class Meta:
        verbose_name = "تسجيل"
        verbose_name_plural = "تسجيلات"
