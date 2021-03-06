# Generated by Django 3.0.8 on 2020-07-28 11:23

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        # ('photologue', '0012_auto_20200728_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='PykapelaGallery',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('photologue.gallery',),
        ),
        migrations.CreateModel(
            name='GalleryExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extended', to='photologue.Gallery')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Extra fields',
                'verbose_name_plural': 'Extra fields',
            },
        ),
    ]
