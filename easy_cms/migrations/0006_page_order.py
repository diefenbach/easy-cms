# Generated by Django 4.2.7 on 2023-11-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0005_page_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="order",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
