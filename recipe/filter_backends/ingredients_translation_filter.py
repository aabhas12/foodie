from django.db.models import Case, When, IntegerField
from rest_framework.filters import BaseFilterBackend


class IngredientTranslationFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            ingredient = request.GET.get('ing', None)
            search_list = []
            final_queryset = queryset
            output_dict = {}
            compare_value = None
            final_list = []
            if ingredient:
                for i in range(len(ingredient)):
                    a = ''
                    for j in range(i + 1):
                        a += ingredient[j]
                    search_list.append(a)
                for key, search_field in enumerate(search_list):
                    queryset = queryset.annotate(rank=Case(
                           When(name__icontains=search_field,
                                then=key+1
                        ), output_field=IntegerField(), default=0
                    )).filter(rank__gt=0).order_by('-rank').distinct()

                    for query in queryset:
                        if query.id in output_dict:
                            output_dict[query.id] = query.rank + output_dict[query.id]
                        else:
                            output_dict[query.id] = query.rank
                sorted_dict = [(k, output_dict[k]) for k in sorted(output_dict, key=output_dict.get, reverse=True)]
                if sorted_dict:
                    compare_value = sorted_dict[0][1]
                for key, value in sorted_dict:
                   if value > (compare_value/2.0):
                       final_list.append(key)
            return final_queryset.filter(id__in=final_list)

        except Exception as ex:
            print(ex)