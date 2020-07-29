# Generated by Django 3.0.8 on 2020-07-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0008_auto_20200728_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='favicon',
            field=models.FileField(blank=True, help_text='User some generator to create your favicon.ico file.', null=True, upload_to='images/', verbose_name='Favicon'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/logo/', verbose_name='Logo'),
        ),
    ]
