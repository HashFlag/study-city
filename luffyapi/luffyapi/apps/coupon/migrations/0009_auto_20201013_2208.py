# Generated by Django 2.2 on 2020-10-13 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0008_auto_20201013_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 14, 8, 35, 264747, tzinfo=utc), verbose_name='优惠券的启用时间'),
        ),
    ]
