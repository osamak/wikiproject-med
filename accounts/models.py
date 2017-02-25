from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from wikithon.models import Wikithons

class Profile(UserenaBaseProfile):
    wikithon = models.ForeignKey(Wikithons)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    twitter = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    def __unicode__(self):
        return self.name