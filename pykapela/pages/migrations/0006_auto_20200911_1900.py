# Generated by Django 3.1.1 on 2020-09-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200728_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='portrait_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/pages/', verbose_name='Main Image'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/pages/', verbose_name='Main Image'),
        ),
    ]
