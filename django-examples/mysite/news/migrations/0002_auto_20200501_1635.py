# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-01 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='body',
            new_name='post',
        ),
    ]
