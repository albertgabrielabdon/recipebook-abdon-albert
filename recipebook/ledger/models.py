from django.db import models
from datetime import datetime
from django.urls import reverse

class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
     return '{}'.format(self.name)
  
class Recipe(models.Model):
  name = models.CharField(max_length=50)
  author = models.CharField(max_length=50, null=True)
  created_on = models.DateTimeField(auto_now_add=True, null=True)
  updated_on = models.DateTimeField(auto_now=True, null=True)
  
  def __str__(self):
     return '{}'.format(self.name, self.author)
   
  def get_absolute_url(self):
   return reverse('ledger:recipe', args=[str(self.pk)])
  
class RecipeIngredient(models.Model):
  quantity = models.CharField(max_length=50)
  ingredient = models.ForeignKey(
      Ingredient,
      on_delete=models.CASCADE,
      related_name = "recipe",
   )  
  recipe = models.ForeignKey(
      Recipe,
      on_delete=models.CASCADE,
      related_name = "ingredient",
   )  

# Create your models here.
