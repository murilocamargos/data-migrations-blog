# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0003_remove_old_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewAddress',
            new_name='Address',
        ),
    ]
