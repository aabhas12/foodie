from django.contrib import admin

# Register your models here.
from recipe.models import CuisineType, RecipeType, Recipe

admin.site.register(CuisineType)
admin.site.register(RecipeType)
admin.site.register(Recipe)
