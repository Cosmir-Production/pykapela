# Generated by Django 2.2.13 on 2020-07-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200701_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='position',
            field=models.IntegerField(default=1),
        ),
    ]
