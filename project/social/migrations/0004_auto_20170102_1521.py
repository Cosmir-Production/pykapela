# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20170102_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='widget_code',
            field=models.TextField(blank=True, default=''),
        ),
    ]
