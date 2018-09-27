from django.shortcuts import render

# Create your views here.
from rest_framework import status, mixins, generics
from rest_framework.response import Response

from recipe.models import Recipe


class Recipe(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Recipe.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)