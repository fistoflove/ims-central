# Generated by Django 4.2.1 on 2023-08-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0021_website_testing_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteevent',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
