# Generated by Django 4.1.2 on 2022-10-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0009_alter_ingredients_name_alter_recipe_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(default="images/rsp_default", upload_to="images/"),
        ),
    ]
