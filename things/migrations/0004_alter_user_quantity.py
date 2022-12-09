# Generated by Django 3.2.5 on 2022-12-09 06:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_alter_user_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
