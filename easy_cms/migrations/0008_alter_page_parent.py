# Generated by Django 4.2.7 on 2023-11-04 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("easy_cms", "0007_alter_page_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="easy_cms.page",
            ),
        ),
    ]