from django.shortcuts import render
from .models import (Blog,Category,Tag,Comment)
from django.core.paginator import Paginator
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    paginator = Paginator(blogs,6)
    page_number = request.Get.get('page')
    blog_list = paginator.get_page('page_number')

    return render (request,'blogs/blog_list.html',context)



