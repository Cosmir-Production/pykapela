# Generated by Django 3.1.1 on 2020-09-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0017_preference_custom_css'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='google_analytics',
            field=models.TextField(blank=True, default=''),
        ),
    ]
