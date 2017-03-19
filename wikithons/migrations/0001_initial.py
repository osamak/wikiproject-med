# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 13:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0627\u0633\u0645 \u0627\u0644\u0641\u0631\u064a\u0642')),
                ('logo', models.ImageField(null=True, upload_to=b'', verbose_name='\u0627\u0644\u0634\u0639\u0627\u0631')),
                ('description', models.TextField(max_length=1000, verbose_name='\u0627\u0644\u0648\u0635\u0641')),
                ('invitation_code', models.CharField(max_length=10, verbose_name='\u0631\u0645\u0632 \u0627\u0644\u062f\u0639\u0648\u0629')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u0645\u062d\u0630\u0648\u0641\u061f')),
                ('articles', models.ManyToManyField(to='articles.Article', verbose_name='\u0627\u0644\u0645\u0642\u0627\u0644\u0627\u062a')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_founded', to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u0644\u0645\u0624\u0633\u0633\u0640/\u0640\u0629')),
                ('members', models.ManyToManyField(related_name='team_memberships', to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u0644\u0639\u0636\u0648\u0627\u062a \u0648\u0627\u0644\u0623\u0639\u0636\u0627\u0621')),
            ],
        ),
        migrations.CreateModel(
            name='Wikithon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0627\u0644\u0627\u0633\u0645')),
                ('description', models.TextField(max_length=1000, verbose_name='\u0627\u0644\u0648\u0635\u0641')),
                ('date', models.DateField(verbose_name='\u0627\u0644\u062a\u0627\u0631\u064a\u062e')),
                ('start_time', models.TimeField(verbose_name='\u0648\u0642\u062a \u0627\u0644\u0628\u062f\u0627\u064a\u0629')),
                ('end_time', models.TimeField(verbose_name='\u0648\u0642\u062a \u0627\u0644\u0646\u0647\u0627\u064a\u0629')),
                ('location', models.CharField(max_length=100, verbose_name='\u0627\u0644\u0645\u0643\u0627\u0646')),
            ],
        ),
    ]