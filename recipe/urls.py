"""foodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from recipe.views import IngredientsViewSet, RecipeViewSet, RecipeTypeViewSet, CuisineTypeViewSet
from django.conf.urls import url, include

router = routers.SimpleRouter()

router.register(r'search_ingredient', IngredientsViewSet)
router.register(r'search_recipe_type', RecipeTypeViewSet)
router.register(r'search_cuisine_type', CuisineTypeViewSet)
router.register(r'store_recipe', RecipeViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
