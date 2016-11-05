# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='admin-base-base-time-model-created')),
                ('changed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='admin-base-base-time-model-changed')),
                ('title', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('secret_key', models.CharField(max_length=256, null=True)),
                ('is_promoted', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('position', models.IntegerField(default=0)),
                ('widget_code', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]