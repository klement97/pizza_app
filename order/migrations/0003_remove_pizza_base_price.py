# Generated by Django 3.1.4 on 2020-12-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201228_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='base_price',
        ),
    ]
