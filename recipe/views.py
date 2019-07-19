# Create your views here.
from rest_framework import viewsets
from recipe.filter_backends.recipe_filter import NameFilter
from recipe.models import Recipe, RecipeType, CuisineType
from recipe.permissions.user_permission import IsUser
from recipe.serializers import RecipeSerializer, RecipeRetrieveSerializer, \
    RecipeListSerializer, RecipeTypeSerializer, CuisineTypeSerializer


class RecipeTypeViewSet(viewsets.ModelViewSet):

    queryset = RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer
    filter_backends = (NameFilter,)


class CuisineTypeViewSet(viewsets.ModelViewSet):

    queryset = CuisineType.objects.all()
    serializer_class = CuisineTypeSerializer
    filter_backends = (NameFilter,)


class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all().select_related('Ingredients', 'Instructions')
    permission_classes = [IsUser]
    filter_backends = ()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeRetrieveSerializer
        elif self.action == 'list':
            return RecipeListSerializer
        else:
            return RecipeSerializer
