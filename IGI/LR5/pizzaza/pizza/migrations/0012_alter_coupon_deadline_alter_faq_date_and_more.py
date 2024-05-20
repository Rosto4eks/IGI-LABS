# Generated by Django 4.2.11 on 2024-05-11 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0011_alter_coupon_deadline_alter_faq_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='deadline',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='date',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
    ]
