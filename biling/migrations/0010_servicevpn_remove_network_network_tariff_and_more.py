# Generated by Django 5.0.4 on 2024-05-08 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biling', '0009_remove_service_data_center_remove_tariff_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceVPN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='network',
            name='network_tariff',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='storage_tariff',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='virtual_machine_tariff',
        ),
        migrations.AddField(
            model_name='tariff',
            name='network',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biling.network'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='storage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biling.storage'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='virtual_machine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biling.virtualmachine'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='data_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biling.datacenter'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='service_vpn',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biling.servicevpn'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
