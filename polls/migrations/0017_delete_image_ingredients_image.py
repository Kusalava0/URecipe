# Generated by Django 4.1.2 on 2022-10-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0016_recipe_image"),
    ]

    operations = [
        migrations.DeleteModel(name="Image",),
        migrations.AddField(
            model_name="ingredients",
            name="image",
            field=models.ImageField(default="images/ing_def.jpg", upload_to="images"),
        ),
    ]
