# Generated by Django 4.1.2 on 2022-10-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_recipe_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(
                default="images/rsp_default.webp", upload_to="images/"
            ),
        ),
    ]