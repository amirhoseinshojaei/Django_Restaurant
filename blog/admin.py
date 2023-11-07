from django.contrib import admin
from .models import (Blog,Category,Tag,Comment)
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment

admin.site.register(Comment)

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine,]
    list_display = [
        'title',
        'author',
        'date',
        'time',
        'category',
        'tag'
    ]
    list_filter = ['date','time','category']
    search_fields = ['category']
    ordering = ['date']

admin.site.register(Blog,BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'publish_at'
    ]
    list_filter = ['publish_at']
    search_fields = ['title']
    ordering = ['publish_at']

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'publish_at'
    ]
    list_filter = ['publish_at']
    search_fields = ['title']
    ordering = ['publish_at']

admin.site.register(Tag,TagAdmin)