# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20160511_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profilepic',
        ),
    ]
