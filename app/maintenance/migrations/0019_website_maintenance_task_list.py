# Generated by Django 4.2.1 on 2023-06-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0018_websiteevent_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='maintenance_task_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.maintenancetasklist'),
        ),
    ]
