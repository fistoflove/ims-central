# Generated by Django 4.2.1 on 2023-06-19 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0017_tag_remove_websiteevent_event_type_website_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteevent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]