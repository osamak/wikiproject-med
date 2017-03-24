# -*- coding: utf-8  -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from .managers import ArticleQuerySet

class Category(models.Model):
    name = models.CharField("االاسم", max_length=100)
    image = models.ImageField("الصورة")
    slug = models.SlugField("الرابط", max_length=40, unique=True)

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "تصانيف"

    def get_article_count(self):
        return self.article_set.count()

    def __unicode__(self):
        return self.name

class Article (models.Model):
    en_name = models.CharField("الاسم الإنجليزي", max_length=100)
    ar_name = models.CharField("الاسم العربي", max_length=100,
                               blank=True)
    assignee = models.ForeignKey(User, verbose_name="المساهمـ/ـة",
                                    null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="التصنيف",
                                 blank=True, null=True)
    quality = models.CharField("الجودة", max_length=100, blank=True)
    importance = models.CharField("الأهمية", max_length=100, blank=True)
    word_count = models.IntegerField("عدد الكلمات", null=True)
    is_available = models.BooleanField("متوفرة؟", default=True)
    objects = ArticleQuerySet.as_manager()

    class Meta:
        verbose_name = "مقالة"
        verbose_name_plural = "مقالات"

    def __unicode__(self):
        return self.en_name

class Reservation(models.Model):
    comment = models.TextField("تعليق")
    reservation_date = models.DateTimeField("تاريخ الحجز", auto_now=True)
    submission_date = models.DateTimeField("تاريخ الإرسال")
    contributor = models.ForeignKey(User, verbose_name="المساهمـ/ـة",
                                    related_name="reservations_submitted")
    reviewer = models.ForeignKey(User, verbose_name="المساهمـ/ـة",
                                 null=True, blank=True,
                                 related_name="reservations_reviewed")
    article = models.ForeignKey(Article, verbose_name="المقالة")
    status_choices = [('RES','محجوزة'), ('SUB','أرسلت'),
                      ('PUB','منشورة'), ('REJ','مرفوضة')]
    status = models.CharField("الحالة", max_length=3,choices=status_choices, default='AVL')

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "حجوزات"

    def __unicode__(self):
        return "{}'s reservation of {}".format(contributor.username, article.en_name)
