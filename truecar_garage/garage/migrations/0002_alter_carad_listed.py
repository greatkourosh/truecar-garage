# Generated by Django 5.0.1 on 2024-01-17 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carad",
            name="listed",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Listed On"
            ),
        ),
    ]
