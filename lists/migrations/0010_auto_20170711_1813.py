# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20170707_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
