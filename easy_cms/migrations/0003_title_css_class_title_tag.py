# Generated by Django 4.2.7 on 2023-11-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0002_image_alt_image_height_image_image_title_image_width"),
    ]

    operations = [
        migrations.AddField(
            model_name="title",
            name="css_class",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AddField(
            model_name="title",
            name="tag",
            field=models.CharField(default="h1", max_length=20),
        ),
    ]