# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-22 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datareader', '0004_rangeanalyse_decline'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeAnalyseHelper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_period_start', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_period_end', models.CharField(blank=True, max_length=1000, null=True)),
                ('end_period_ends', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
