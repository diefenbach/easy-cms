# Generated by Django 4.2.7 on 2023-11-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0008_alter_page_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="title",
            field=models.CharField(default="Page", max_length=50),
            preserve_default=False,
        ),
    ]
