# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-26 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_formula_seq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formula',
            options={'ordering': ['seq']},
        ),
        migrations.AddField(
            model_name='formula',
            name='manual',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='adds',
            field=models.ManyToManyField(blank=True, related_name='adds', to='report.Item'),
        ),
    ]
