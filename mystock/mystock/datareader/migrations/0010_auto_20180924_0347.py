# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-24 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datareader', '0009_auto_20180924_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketdateanalyse',
            name='pre_sum_cnt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketdateanalyse',
            name='sum_cnt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
