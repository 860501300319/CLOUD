# Generated by Django 5.0.4 on 2024-05-08 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biling', '0010_servicevpn_remove_network_network_tariff_and_more — копия'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='service_vpn',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biling.servicevpn'),
        ),
    ]
