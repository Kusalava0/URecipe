# Generated by Django 4.1.2 on 2022-10-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0019_remove_ingredients_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredients",
            name="image",
            field=models.ImageField(default="images/ing_def.webp", upload_to="images"),
        ),
    ]
