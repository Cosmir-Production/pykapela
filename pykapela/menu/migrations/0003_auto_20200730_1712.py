# Generated by Django 3.0.8 on 2020-07-30 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200730_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='tree',
            field=models.ForeignKey(help_text='Site tree this item belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='menuitem_tree', to='menu.MenuTree', verbose_name='Site Tree'),
        ),
    ]