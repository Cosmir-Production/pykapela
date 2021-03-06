# Generated by Django 3.1.1 on 2020-09-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200912_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_dark',
            field=models.BooleanField(default=True, help_text='Dark background and white font color.'),
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.IntegerField(default=1, help_text='Background images on homepage are sorted by position.'),
        ),
    ]
