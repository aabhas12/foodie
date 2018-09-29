from rest_framework.filters import BaseFilterBackend

from recipe.models import MainIngredients


class IngredientTranslationFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            ingredient = request.GET.get('ing', None)

            if ingredient:
                queryset = queryset.filter(name=ingredient)

            return queryset

        except Exception as ex:
            print(ex)