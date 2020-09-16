# Generated by Django 3.1.1 on 2020-09-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='admin-base-base-time-model-created')),
                ('changed', models.DateTimeField(auto_now=True, db_index=True, verbose_name='admin-base-base-time-model-changed')),
                ('name', models.CharField(max_length=256)),
                ('file', models.FileField(help_text='Upload your file here', upload_to='files')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
