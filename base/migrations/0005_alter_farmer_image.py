# Generated by Django 4.2.7 on 2025-03-21 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_farmer_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmer",
            name="image",
            field=models.ImageField(
                blank=True,
                default="images/placeholder.jpg",
                null=True,
                upload_to="images",
            ),
        ),
    ]
