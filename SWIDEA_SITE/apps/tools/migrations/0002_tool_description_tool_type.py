# Generated by Django 5.0.7 on 2024-07-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tools", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tool",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tool",
            name="type",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
