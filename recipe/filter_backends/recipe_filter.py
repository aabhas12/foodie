from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class NameFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        name = request.GET.get('name')
        if name:
                return queryset.filter(name__icontains=type)
        return queryset


class RecipeFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        keyword = request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) |
                                       Q(user__username__icontains=keyword)).distinct()
        return queryset
