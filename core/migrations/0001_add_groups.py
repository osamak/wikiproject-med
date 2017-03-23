# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 20:13
from __future__ import unicode_literals

from django.db import migrations

def add_groups(apps, schema_editor):
    Group = apps.get_model('auth','Group')
    Group.objects.create(name="Organizers")
    Group.objects.create(name="Reviewers")

def remove_groups(apps, schema_editor):
    Group = apps.get_model('auth','Group')
    Group.objects.filter(name__in=["Organizers", "Reviewers"])

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length')
    ]

    operations = [
       migrations.RunPython(
            add_groups,
            reverse_code=remove_groups),
    ]
