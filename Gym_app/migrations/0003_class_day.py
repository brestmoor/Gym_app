# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-16 20:55
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('Gym_app', '0002_auto_20161107_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='day',
            field=models.CharField(default=datetime.datetime(2016, 11, 16, 20, 55, 31, 849000, tzinfo=utc),
                                   max_length=50),
            preserve_default=False,
        ),
    ]
