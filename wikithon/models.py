from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# change model name to "Wikithon"
class Wikithons(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date = models.DateField(auto_now=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    location = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name


class Profile(models.Model):
    wikithon = models.ForeignKey(Wikithons)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    twitter = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    def __unicode__(self):
        return self.name


# gives me an error
class Team(models.Model):
    name = models.CharField(max_length=100)
    founder = models.ForeignKey(User)
    #members = models.ManyToManyField(User)
    logo = models.ImageField(null=True)
    articles = models.ManyToManyField('Article')
    description = models.TextField(max_length=1000)
    invitation_code = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    slug = models.SlugField(max_length=100)

# gives me an error
class Article (models.Model):
    en_name = models.CharField(max_length=100, null=True)
    #ar_name = models.CharField(max_length=100)
    contributor = models.ForeignKey(User, null=True)
    category = models.ForeignKey(Category)
    quality = models.CharField(max_length=100)
    importance = models.CharField(max_length=100)
    words = models.IntegerField(null=True)
    #is_available = models.BooleanField( default=True)
    url = models.URLField()
    status_choices = (('AVAILABLE','Available'),('RESERVED','Reserved'), ('SUBMITTED','Submitted'), ('PUBLISHED','Published'), ('REJECTED','Rejected'))
    status = models.CharField(max_length=100,choices=status_choices)

# change model name to "Reservation"
class Submission (models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    contributor = models.ForeignKey(User)
    articles = models.ForeignKey(Article)

