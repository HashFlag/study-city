# Generated by Django 2.2 on 2020-10-13 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20201013_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 28, 9, 199754, tzinfo=utc), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 28, 9, 199726, tzinfo=utc), verbose_name='开始时间'),
        ),
    ]
