# Generated by Django 4.2.11 on 2024-05-15 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0020_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
