# Generated by Django 2.2 on 2020-10-13 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0007_auto_20201013_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 14, 2, 51, 599475, tzinfo=utc), verbose_name='优惠券的启用时间'),
        ),
    ]
