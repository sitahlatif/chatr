# Generated by Django 2.1.7 on 2019-03-20 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_messages', '0012_auto_20190320_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
