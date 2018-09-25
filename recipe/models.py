from django.db import models

# Create your models here.
from user.models import Users


class Recipe(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    time = models.FloatField()
    servings = models.IntegerField()
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    video = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_ingredients', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75, blank=True, null=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_instructions', on_delete=models.CASCADE)
    step = models.CharField(max_length=300, blank=True, null=True)
    image = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_images', on_delete=models.CASCADE)
    icon = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)