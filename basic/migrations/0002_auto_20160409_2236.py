# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
