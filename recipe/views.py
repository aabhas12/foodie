# Create your views here.
from rest_framework import viewsets

from recipe.filter_backends.ingredients_translation_filter import IngredientTranslationFilter
from recipe.models import IngredientsTranslations, Recipe
from recipe.serializers import IngredientsTranslationSerializer, RecipeSerializer, RecipeRetrieveSerializer, \
    RecipeListSerializer


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = IngredientsTranslations.objects.all()
    serializer_class = IngredientsTranslationSerializer
    filter_backends = (IngredientTranslationFilter,)


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeRetrieveSerializer
        elif self.action == 'list':
            return RecipeListSerializer
        else:
            return RecipeSerializer
