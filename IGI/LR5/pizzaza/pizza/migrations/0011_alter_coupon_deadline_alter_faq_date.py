# Generated by Django 4.2.11 on 2024-05-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_companyinfo_text_coupon_deadline_coupon_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='deadline',
            field=models.DateTimeField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='date',
            field=models.DateTimeField(default='2000-01-01'),
        ),
    ]
