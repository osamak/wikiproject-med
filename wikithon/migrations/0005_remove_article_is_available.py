# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikithon', '0004_article_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_available',
        ),
    ]