# Generated by Django 4.2.1 on 2023-06-02 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_maintenancetasklist_maintenancetasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaintenanceTasks',
            new_name='MaintenanceTask',
        ),
    ]