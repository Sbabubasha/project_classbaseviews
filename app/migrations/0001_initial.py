# Generated by Django 4.1.7 on 2023-05-14 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "topic_name",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Webpage",
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
                ("name", models.CharField(max_length=30)),
                ("url", models.URLField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "topic_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.topic"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accessrecord",
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
                ("author", models.CharField(max_length=30)),
                ("date", models.DateField()),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.webpage"
                    ),
                ),
            ],
        ),
    ]
