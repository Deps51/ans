# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-12 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180812_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='link',
            field=models.CharField(default='Default', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=250),
        ),
    ]
