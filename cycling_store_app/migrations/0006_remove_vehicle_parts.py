# Generated by Django 5.0.6 on 2024-05-16 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_store_app', '0005_remove_vehicle_parts_in_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='parts',
        ),
    ]
