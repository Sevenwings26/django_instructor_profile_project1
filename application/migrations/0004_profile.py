# Generated by Django 4.2.16 on 2024-11-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "application",
            "0003_alter_generalinfo_bio_alter_generalinfo_fb_link_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("occupation", models.CharField(max_length=250)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=7
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=400, null=True)),
                ("fb_link", models.URLField()),
                ("ig_link", models.URLField()),
                ("linkedIn_link", models.URLField()),
                ("x_link", models.URLField()),
            ],
        ),
    ]
