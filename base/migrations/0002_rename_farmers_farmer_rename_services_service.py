# Generated by Django 4.2.7 on 2025-03-13 02:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Farmers",
            new_name="Farmer",
        ),
        migrations.RenameModel(
            old_name="Services",
            new_name="Service",
        ),
    ]
