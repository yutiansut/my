# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-06 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datareader', '0013_auto_20181006_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodmincnt',
            name='market_liquidity_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodmincnt',
            name='market_shares_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodmincnt',
            name='min_liquidity_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodmincnt',
            name='min_shares_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
