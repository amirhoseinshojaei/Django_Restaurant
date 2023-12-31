from django.shortcuts import render
from .models import Food , Gallery , Staff
from django.views.generic import ListView,TemplateView
# Create your views here.
class FoodList(ListView):
    queryset = Food.objects.filter(status=True)
    context_object_name = 'objects-list'
    template_name = 'food/index.html'

def gallery_list(request):
    obj = Gallery.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'food/gallery.html',context)

class StaffList(ListView):
    model = Staff
    context_object_name = 'objects_staff'
    template_name = 'staff/staff.html'

class AboutPage(TemplateView):
    template_name = 'static/about.html'

class MenuView(ListView):
    queryset = Food.objects.filter(status = True)
    context_object_name = 'menu-list'
    template_name = 'food/menu.html'