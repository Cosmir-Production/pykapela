# Generated by Django 3.0.8 on 2020-08-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0009_auto_20200729_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='promoted_gallery',
            field=models.IntegerField(default=1, help_text='ID of gallery to be promoted on homepage.'),
        ),
    ]
