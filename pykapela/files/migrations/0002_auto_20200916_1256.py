# Generated by Django 3.1.1 on 2020-09-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
