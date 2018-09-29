from rest_framework.filters import BaseFilterBackend



class IngredientTranslationFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            ingredient = request.GET.get('ing', None)

            if ingredient:
                queryset = queryset.filter(name__icontains=ingredient)
            return queryset

        except Exception as ex:
            print(ex)