# Generated by Django 3.1.1 on 2020-09-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0014_auto_20200806_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='show_languages',
            field=models.BooleanField(default=True, help_text='Show languages menu on top?'),
        ),
    ]
