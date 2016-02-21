# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='commodity',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
