# Generated by Django 4.1.6 on 2023-02-14 00:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("generate", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RenderWorkerDevice",
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
                ("host", models.CharField(blank=True, max_length=255, null=True)),
                ("device_id", models.IntegerField(blank=True, null=True)),
                (
                    "device_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_update_at", models.DateTimeField(auto_now=True)),
                ("allocated_memory", models.FloatField(blank=True, null=True)),
                ("total_memory", models.FloatField(blank=True, null=True)),
                ("cached_memory", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
