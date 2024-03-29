# Generated by Django 2.2 on 2020-10-13 12:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20201005_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 12, 40, 22, 292090, tzinfo=utc), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 12, 40, 22, 292063, tzinfo=utc), verbose_name='开始时间'),
        ),
    ]
