from django.contrib import admin
from .models import Food , Gallery
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'type',
        'pub_date',
        'price'
    ]
    list_filter = ['type']
    search_fields = ['name']
    ordering = ["pub_date"]

admin.site.register(Food,FoodAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display =[
        'name',
        'date'
    ]
    list_filter = ['date']
    search_fields = ['name']
    ordering = ['date']

admin.site.register(GalleryAdmin,Gallery)