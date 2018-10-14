from django.contrib import admin

# Register your models here.
from recipe.models import MainIngredients, IngredientsTranslations, CuisineType, RecipeType, Recipe

admin.site.register(MainIngredients)
admin.site.register(IngredientsTranslations)
admin.site.register(CuisineType)
admin.site.register(RecipeType)
admin.site.register(Recipe)