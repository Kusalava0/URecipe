# Generated by Django 4.1.2 on 2022-10-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_alter_ingredients_recipe_alter_recipe_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredients",
            name="name",
            field=models.TextField(max_length=15, unique=True),
        ),
        migrations.RemoveField(model_name="ingredients", name="recipe",),
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.TextField(max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name="ingredients",
            name="recipe",
            field=models.ManyToManyField(related_name="ingredient", to="polls.recipe"),
        ),
    ]
