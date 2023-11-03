from django.shortcuts import render
from .models import Contact
from .forms import ContacForm
# Create your views here.
def contact_form(request):
    contact_form = ContacForm
    if request.method == 'POST':
        contact_form = ContacForm(request.POST)
        if contact_form.is_valid:
            contact_form.save()
    else:
        contact_form = ContacForm()
    
    context={
        "contact": contact_form
    }

    return render (request,'contact/form.html',context)