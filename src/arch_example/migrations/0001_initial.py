# Generated by Django 5.0 on 2024-01-04 17:51

import django.core.validators
from django.db import migrations, models

import main.base_models


def set_default_values(apps, schema_editor):
    if schema_editor.connection.alias != "default":
        return

    ArchExample = apps.get_model("arch_example", "ArchExample")

    arch_example_list = [
        ArchExample(test_name="Test1", test_age=1),
        ArchExample(test_name="Test2", test_age=20),
        ArchExample(test_name="Test3", test_age=30),
    ]

    ArchExample.objects.bulk_create(arch_example_list)


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArchExample",
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
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Updated at"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "uuid",
                    models.CharField(
                        default=main.base_models.generate_uuid4,
                        max_length=42,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "test_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Test name"
                    ),
                ),
                (
                    "test_age",
                    models.IntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(130),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="Test age",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RunPython(
            set_default_values, migrations.RunPython.noop, elidable=True
        ),
    ]
