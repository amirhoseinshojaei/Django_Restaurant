from django.urls import path
from .views import contact_form
#Write Code here
urlpatterns=[
    path ('contact',contact_form, name= 'contact')
]