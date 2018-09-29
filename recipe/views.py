from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recipe.filter_backends.ingredients_translation_filter import IngredientTranslationFilter
from recipe.models import IngredientsTranslations
from user.serializers import IngredientsTranslationSerializer


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = IngredientsTranslations.objects.all()
    serializer_class = IngredientsTranslationSerializer
    filter_backends = (IngredientTranslationFilter,)

