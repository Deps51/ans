# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-06 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option1_percentage',
            field=models.IntegerField(default=0),
        ),
    ]