# Generated by Django 4.2.7 on 2023-11-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0011_alter_image_height_alter_image_width"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="height",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="image",
            name="image_file",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="image",
            name="width",
            field=models.IntegerField(default=0),
        ),
    ]
