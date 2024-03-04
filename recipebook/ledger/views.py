from django.shortcuts import render
from django.http import request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe
    
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_site.html' 
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'


 
# Create your views here.
