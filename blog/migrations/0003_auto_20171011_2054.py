# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171011_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='updated_ap',
            new_name='updated_at',
        ),
    ]