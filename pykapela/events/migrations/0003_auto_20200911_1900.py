# Generated by Django 3.1.1 on 2020-09-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200701_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(blank=True, max_length=256, verbose_name='Where is it?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/concerts/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_promoted',
            field=models.BooleanField(default=False, help_text='Promoted events will be first. Otherwise sorted by datetime'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='Use only small caps, no spaces, just hyphens. Must be unique.', verbose_name='URL slug'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text='Create nice name for this venue! No location here.', max_length=256, verbose_name='Venue name'),
        ),
    ]
