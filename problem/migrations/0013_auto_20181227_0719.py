# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-27 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0012_auto_20180501_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='pe_ignored',
            field=models.BooleanField(default=False),
        ),
    ]