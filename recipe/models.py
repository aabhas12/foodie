from django.db import models

# Create your models here.
from user.models import Users


class RecipeType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return "{}".format(self.name)


class CuisineType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name']

    def __str__(self):
        return "{}".format(self.name)

    # a = ['Italian', 'Mexican', 'Chinese', 'Indian', 'Japanese', 'Greek', 'Spanish', 'French', 'Thai', 'Vietnamese',
    #      'Lebanese', 'Vegan', 'Cuban', 'Mongolian']


class Recipe(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe_type = models.ManyToManyField(RecipeType, null=True, blank=True)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    time = models.FloatField()
    servings = models.IntegerField()
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    video = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class MainIngredients(models.Model):
    name = models.CharField(max_length=20)
    icon = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Main Ingredient'
        verbose_name_plural = 'Main Ingredients'

    def __str__(self):
        return "{}".format(self.name)


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_ingredients', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75, blank=True, null=True)
    main_ingredient = models.ForeignKey(MainIngredients, null=True, blank=True, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class IngredientsTranslations(models.Model):
    ingredient = models.ForeignKey(MainIngredients, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    language_code = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = 'Ingredients Translation'
        verbose_name_plural = 'Ingredients Translations'

    def __str__(self):
        return "{}".format(self.name)


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