# Generated by Django 3.0.8 on 2020-08-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0010_preference_promoted_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='footer_copyright',
            field=models.CharField(blank=True, default='', help_text='Optional.', max_length=255),
        ),
    ]