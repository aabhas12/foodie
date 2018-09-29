import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

your_djangoproject_home = os.path.split(BASE_DIR)[0]

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'foodie.settings'
microsoftclientid = 'd0c45af0-c3d9-4d98-91de-80a5c6f18eeb'
key = '6L6J5Lnlcy09VHMy6HGjL/3nwmE1MHlnlNBqzey3ux8='
import django
django.setup()

from googletrans import Translator
from recipe.models import MainIngredients, IngredientsTranslations
from yandex import Translater
from mstranslator import Translator as mstranslate


tr = Translater()
tr.set_key('trnsl.1.1.20180928T003716Z.0794b3c0330a2aa6.1d51eeb5dc291c2a59b55b0b2b317e610a60403c')
translator = Translator()
tr.set_from_lang('en')
ingredients = ['onion', 'tomatoes', 'green chili', 'cottage cheese', 'cilantro']
language_codes = ['es', 'hi', 'pt']
mstranslator = mstranslate('e5dfe8a94f1a42229e727596bd4c3446')


for ingredient in ingredients:
    for language_code in language_codes:
        if MainIngredients.objects.filter(name=ingredient).exists():
            main_ingredient = MainIngredients.objects.get(name=ingredient)
        else:
            main_ingredient = MainIngredients.objects.create(name=ingredient)
        a = translator.translate(ingredient, src='en', dest=language_code)
        if not IngredientsTranslations.objects.filter(name=a.text.lower(), ingredient=main_ingredient).exists():
            IngredientsTranslations.objects.create(ingredient=main_ingredient, name=a.text.lower())
        if a.pronunciation:
            if not IngredientsTranslations.objects.filter(name=a.pronunciation.lower(), ingredient=main_ingredient).exists():
                IngredientsTranslations.objects.create(ingredient=main_ingredient, name=a.pronunciation.lower())
        if a.extra_data['translation']:
            extra_text = a.extra_data['translation']
            for i in extra_text:
                for j in i:
                    if j and not j.__str__().isnumeric():
                        if not IngredientsTranslations.objects.filter(name=j.lower(), ingredient=main_ingredient).exists():
                            IngredientsTranslations.objects.create(ingredient=main_ingredient, name=j.lower())

        tr.set_to_lang(language_code)
        tr.set_text(ingredient)
        if not IngredientsTranslations.objects.filter(name=tr.translate().lower(), ingredient=main_ingredient).exists():
            IngredientsTranslations.objects.create(ingredient=main_ingredient, name=tr.translate().lower())
        text = mstranslator.translate(ingredient, lang_from='en', lang_to=language_code)
        if not IngredientsTranslations.objects.filter(name=text.lower(), ingredient=main_ingredient).exists():
            IngredientsTranslations.objects.create(ingredient=main_ingredient, name=text.lower())
print('done')

