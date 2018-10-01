from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recipe.filter_backends.ingredients_translation_filter import IngredientTranslationFilter
from recipe.models import IngredientsTranslations, Recipe
from user.serializers import IngredientsTranslationSerializer, RecipeSerializer


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = IngredientsTranslations.objects.all()
    serializer_class = IngredientsTranslationSerializer
    filter_backends = (IngredientTranslationFilter,)


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
