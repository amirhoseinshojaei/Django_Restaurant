from .views import (FoodList , gallery_list ,StaffList,AboutPage,MenuView)
from django.urls import path
# Write code here
urlpatterns=[
    path('',FoodList.as_view(), name= 'food_list'),
    path('staff',StaffList.as_view(), name= 'staff_list'),
    path('gallery',gallery_list, name= 'gallery_list'),
    path("about",AboutPage.as_view(), name='about'),
    path('menu',MenuView.as_view(), name='menu_list'),
]