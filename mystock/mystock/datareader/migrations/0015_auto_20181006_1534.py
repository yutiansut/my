# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-06 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datareader', '0014_auto_20181006_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketinfo',
            name='low_liquidity_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketinfo',
            name='low_shares_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
