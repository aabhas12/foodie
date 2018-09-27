from django.contrib import admin

# Register your models here.
from recipe.models import MainIngredients, IngredientsTranslations

admin.site.register(MainIngredients)
admin.site.register(IngredientsTranslations)