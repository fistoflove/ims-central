# Generated by Django 4.2.1 on 2023-06-02 20:00

from django.db import migrations, models
import django.db.models.deletion
import maintenance.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenancePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(default='PLAN NAME', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=200)),
                ('website_url', models.URLField(max_length=500, null=True, validators=[maintenance.models.RequireHttpOrHttpsUrl()])),
                ('maintenance_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.maintenanceplan')),
            ],
        ),
    ]
