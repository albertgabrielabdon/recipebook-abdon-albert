from django.urls import path
from .views import recipe_site, recipe1, recipe2

urlpatterns = [
    path('recipes/list',recipe_site, name='recipe_site'),
    path('recipe/1',recipe1, name='recipe1'),
    path('recipe/2',recipe2, name='recipe2'),
]

app_name = 'ledger'