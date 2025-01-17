# Generated by Django 5.1.1 on 2024-09-30 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exoplanets", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz",
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
                ("question", models.CharField(max_length=250)),
                ("options", models.TextField()),
                (
                    "exoplanet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quizzes",
                        to="exoplanets.exoplanet",
                    ),
                ),
            ],
        ),
    ]
