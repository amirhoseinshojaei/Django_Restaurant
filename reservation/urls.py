from .views import *
from django.urls import path
#Write Code here
urlpatterns=[
    path ('reserve',reservation_form , name= 'reservation')
]