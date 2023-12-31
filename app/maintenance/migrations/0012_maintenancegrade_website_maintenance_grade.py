# Generated by Django 4.2.1 on 2023-06-02 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0011_alter_website_login_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='A', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Maintenance Plans',
            },
        ),
        migrations.AddField(
            model_name='website',
            name='maintenance_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.maintenancegrade'),
        ),
    ]
