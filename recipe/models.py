from django.db import models

# Create your models here.
from user.models import Users


class BaseModel(models.Model):
    """
        Parent model
    """
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True


class RecipeType(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)


class CuisineType(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)


class Recipe(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    recipe_type = models.ManyToManyField(RecipeType)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    time = models.FloatField()
    servings = models.IntegerField()
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    video = models.URLField(null=True, blank=True)


class Ingredients(BaseModel):
    recipe = models.ForeignKey(Recipe, related_name='recipes_ingredients', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75, blank=True, null=True)
    icon = models.URLField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return "{}".format(self.ingredient)


class Instructions(BaseModel):
    recipe = models.ForeignKey(Recipe, related_name='recipes_instructions', on_delete=models.CASCADE)
    step = models.CharField(max_length=300, blank=True, null=True)
    image = models.URLField(null=True, blank=True)


class RecipeImage(BaseModel):
    recipe = models.ForeignKey(Recipe, related_name='recipes_images', on_delete=models.CASCADE)
    icon = models.URLField(null=True, blank=True)
