# Generated by Django 4.2.16 on 2024-11-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0004_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="workplace",
            field=models.CharField(default="online", max_length=350),
        ),
    ]