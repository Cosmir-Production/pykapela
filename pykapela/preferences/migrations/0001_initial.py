# Generated by Django 3.0.2 on 2020-01-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='admin-base-base-time-model-created')),
                ('changed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='admin-base-base-time-model-changed')),
                ('name', models.CharField(max_length=256)),
                ('type', models.IntegerField(choices=[(0, 'Text'), (1, 'True or False')], default=0)),
                ('content', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]