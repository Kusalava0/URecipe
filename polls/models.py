from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.TextField(max_length = 35, blank = False, unique = True)
    description = models.TextField(blank = False)
    image = models.ImageField(upload_to='images',default = 'images/007.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', blank = False)

    def __str__(self) -> str:
        return self.user.username

class Ingredients(models.Model):
    name = models.TextField(max_length = 20, blank = False, unique = True)
    image = models.ImageField(upload_to='images',default = 'images/ing_def.webp')
    ing_recipe = models.ManyToManyField(Recipe, related_name='ingredient', blank = False)
