# Generated by Django 2.2 on 2020-10-13 12:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_auto_20201013_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否上架'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否上架'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 12, 50, 58, 489972, tzinfo=utc), verbose_name='优惠券的启用时间'),
        ),
    ]