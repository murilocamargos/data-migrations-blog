# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bought',
            field=models.IntegerField(),
        ),
    ]