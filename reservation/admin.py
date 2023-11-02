from django.contrib import admin
from .models import Reservation
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'number',
        'date',
        'time',
        'person'
    ]
    search_fields = ['name']
    ordering = ['date']
    list_filter = [
        'date',
        'time'
    ]
admin.site.register(Reservation,ReservationAdmin)