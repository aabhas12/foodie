# Create your views here.
from rest_framework import viewsets

from recipe.filter_backends.recipe_filter import IngredientTranslationFilter, NameFilter
from recipe.models import IngredientsTranslations, Recipe, RecipeType, CuisineType
from recipe.serializers import IngredientsTranslationSerializer, RecipeSerializer, RecipeRetrieveSerializer, \
    RecipeListSerializer, RecipeTypeSerializer, CuisineTypeSerializer


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = IngredientsTranslations.objects.all()
    serializer_class = IngredientsTranslationSerializer
    filter_backends = (IngredientTranslationFilter,)


class RecipeTypeViewSet(viewsets.ModelViewSet):

    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer
    filter_backends = (NameFilter,)


class CuisineTypeViewSet(viewsets.ModelViewSet):

    queryset = CuisineType.objects.all()
    serializer_class = CuisineTypeSerializer
    filter_backends = (NameFilter,)


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeRetrieveSerializer
        elif self.action == 'list':
            return RecipeListSerializer
        else:
            return RecipeSerializer
