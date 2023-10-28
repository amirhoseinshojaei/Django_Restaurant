from django.shortcuts import render
from .models import Food , Gallery , Staff
from django.views.generic import ListView
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
    return render('food/gallery.html',context)

class StaffList(ListView):
    model = Staff
    context_object_name = 'objects_staff'
    template_name = 'staff/staff.html'