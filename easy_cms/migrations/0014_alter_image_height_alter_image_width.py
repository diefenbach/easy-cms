# Generated by Django 4.2.7 on 2023-11-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0013_alter_image_alt_alter_image_height_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="image",
            name="width",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]