# Generated by Django 5.0.4 on 2024-04-28 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biling', '0002_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
    ]
