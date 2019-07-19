from rest_framework.filters import BaseFilterBackend


class NameFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            type = request.GET.get('type')
            if type:
                return queryset.filter(name__icontains=type)
            else:
                return queryset
        except Exception as ex:
            print(ex)


class RecipeFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset