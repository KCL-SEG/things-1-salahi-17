# Generated by Django 4.1.4 on 2022-12-09 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("things", "0005_alter_user_name_alter_user_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Thing",
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
                ("name", models.CharField(max_length=30, unique=True)),
                ("description", models.CharField(blank=True, max_length=120)),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ]
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="User",),
    ]
