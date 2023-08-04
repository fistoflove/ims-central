# Generated by Django 4.2.1 on 2023-07-25 21:24

from django.db import migrations, models
import maintenance.models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0020_websiteevent_data_websiteevent_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='testing_url',
            field=models.URLField(blank=True, max_length=500, null=True, validators=[maintenance.models.RequireHttpOrHttpsUrl()]),
        ),
    ]
