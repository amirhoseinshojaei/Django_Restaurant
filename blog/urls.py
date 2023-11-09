from .views import (blog_list,blog_detail)
from django.urls import path
################
urlpatterns=[
    path ('',blog_list, name= 'blogs'),
    path ('blog/<slug:slug>',blog_detail, name= 'blog_detail')
]