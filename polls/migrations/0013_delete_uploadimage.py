# Generated by Django 4.1.2 on 2022-10-12 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0012_uploadimage_alter_recipe_recipe_image"),
    ]

    operations = [
        migrations.DeleteModel(name="UploadImage",),
    ]
