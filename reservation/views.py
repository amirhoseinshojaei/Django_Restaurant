from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
def reservation_form(request):
    reservation_form = ReservationForm
    if request.method=='POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid:
            reservation_form.save()
    else:
        reservation_form = ReservationForm()
    context = {
        "form":reservation_form
    }

    return render(request,'reserve/reservation.html',context)