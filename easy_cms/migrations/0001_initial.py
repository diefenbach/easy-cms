# Generated by Django 4.2.7 on 2023-11-04 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Component",
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
                ("order", models.IntegerField()),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Page",
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
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "component_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="easy_cms.component",
                    ),
                ),
                ("image_file", models.ImageField(upload_to="images")),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("easy_cms.component",),
        ),
        migrations.CreateModel(
            name="Paragraph",
            fields=[
                (
                    "component_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="easy_cms.component",
                    ),
                ),
                ("content", models.TextField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("easy_cms.component",),
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "component_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="easy_cms.component",
                    ),
                ),
                ("content", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("easy_cms.component",),
        ),
        migrations.AddField(
            model_name="component",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="components",
                to="easy_cms.page",
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
    ]
