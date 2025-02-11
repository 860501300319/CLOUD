# Generated by Django 5.0.4 on 2024-05-12 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biling', '0012_alter_orders_end_date_alter_orders_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacenter',
            name='city_id',
            field=models.IntegerField(default=701),
        ),
        migrations.AlterField(
            model_name='orders',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
