# Generated by Django 2.1.7 on 2019-03-20 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_messages', '0011_auto_20190320_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
