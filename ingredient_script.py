import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

your_djangoproject_home = os.path.split(BASE_DIR)[0]

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'foodie.settings'

import django
django.setup()

from googletrans import Translator
from recipe.models import MainIngredients, IngredientsTranslations


translator = Translator()
ingredients = ['onion', 'tomatoes', 'green chili', 'cottage cheese', 'Angelica', 'Basil', 'Basil - Thai', 'Bay', 'Borage', 'Coriander', 'cilantro', 'mint']
language_codes = ['es', 'hi', 'pt', 'ur']
for ingredient in ingredients:
    for language_code in language_codes:
        if MainIngredients.objects.filter(name=ingredient).exists():
            main_ingredient = MainIngredients.objects.get(name=ingredient)
        else:
            main_ingredient = MainIngredients.objects.create(name=ingredient)
        a = translator.translate(ingredient, src='en', dest=language_code)
        if not IngredientsTranslations.objects.filter(name=a.text, ingredient=main_ingredient,
                                                      language_code=language_code).exists():
            IngredientsTranslations.objects.create(ingredient=main_ingredient, name=a.text, language_code=language_code)
        if a.pronunciation:
            if not IngredientsTranslations.objects.filter(name=a.pronunciation, ingredient=main_ingredient,
                                                          language_code=language_code).exists():
                IngredientsTranslations.objects.create(ingredient=main_ingredient, name=a.pronunciation,
                                                       language_code=language_code)

print('done')