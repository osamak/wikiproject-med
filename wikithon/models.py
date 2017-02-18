from __future__ import unicode_literals
from django.db import models


class Wikithons(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=False)
    duration = models.DurationField
    location = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    twitter = models.URLField
    description = models.TextField(max_length=1000)
    avatar = models.ImageField
    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    founder = models.OneToOneField(Profile)
    members = models.ManyToManyField
    logo = models.ImageField
    articles = models.ManyToManyField
    description = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.name
#password = models.TextField(max_length=1000)


class Category (models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField
    slug = models.SlugField(max_length=100)


class Article (models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(Profile)
    quality = models.CharField(max_length=100)
    importance = models.CharField(max_length=100)
    words = models.IntegerField
#status_choices = ((AVAILABLE,'Available'),(RESERVED,'Reserved'), (SUBMITTED,'Submitted'), (PUBLISHED,'Published'), (REJECTED,'Rejected'))
#status = models.CharField(max_length=100,choices=status_choices)


class Submission (models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
