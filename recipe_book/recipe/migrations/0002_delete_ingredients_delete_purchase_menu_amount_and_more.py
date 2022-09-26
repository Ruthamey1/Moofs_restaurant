# Generated by Django 4.1.1 on 2022-09-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Ingredients",),
        migrations.DeleteModel(name="Purchase",),
        migrations.AddField(
            model_name="menu", name="amount", field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name="menu",
            name="strength",
            field=models.CharField(default="-", max_length=20),
        ),
        migrations.AlterField(
            model_name="menu",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="menu", name="price", field=models.IntegerField(default=20),
        ),
    ]
