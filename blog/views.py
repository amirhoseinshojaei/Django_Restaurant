from django.shortcuts import render,get_object_or_404
from .models import (Blog,Category,Tag,Comment)
from django.core.paginator import Paginator
from .forms import CommentForm
from django.http import HttpResponseRedirect
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

def blog_detail(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    category = Category.objects.all()
    tags = Tag.objects.all().filter(tags = blog)
    recents = Blog.objects.all().order_by("date")[:4]
    comments = Comment.objects.all()
    context={
        "blog":blog,
        "category":category,
        "tags":tags,
        "recents":recents,
        "comments":comments
    }

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog= blog
            obj.save()
            return HttpResponseRedirect(request.path_info)
        
        else:
            form = CommentForm()

    return render(request,'blogs/blog_detail.html',context)






