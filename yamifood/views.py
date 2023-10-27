from django.shortcuts import render
from .models import Food
from django.views.generic import ListView
# Create your views here.
class FoodList(ListView):
    queryset = Food.objects.filter(status=True)
    context_object_name = 'objects-list'
    template_name = 'food/food_list/html'