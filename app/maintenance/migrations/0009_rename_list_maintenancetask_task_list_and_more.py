# Generated by Django 4.2.1 on 2023-06-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0008_remove_maintenanceplan_plan_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenancetask',
            old_name='list',
            new_name='task_list',
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
