# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20170221_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='responsibilities',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
