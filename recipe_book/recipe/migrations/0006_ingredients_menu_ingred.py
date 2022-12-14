# Generated by Django 4.1.1 on 2022-09-25 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0005_remove_menu_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredients",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredients", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="menu",
            name="ingred",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe.ingredients",
            ),
        ),
    ]
