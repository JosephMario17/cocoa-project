# Generated by Django 4.2.7 on 2025-03-13 03:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_rename_farmers_farmer_rename_services_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmer",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
