# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-13 22:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
