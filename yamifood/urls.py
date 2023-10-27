from .views import FoodList
from django.urls import path
# Write code here
urlpatterns=[
    path('',FoodList.as_view(), name= 'food_list'),
]