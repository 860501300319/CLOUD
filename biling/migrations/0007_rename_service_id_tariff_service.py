# Generated by Django 5.0.4 on 2024-04-30 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biling', '0006_rename_tariff_id_network_network_tariff_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tariff',
            old_name='service_id',
            new_name='service',
        ),
    ]
