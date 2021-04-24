from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('موضوع پست', {'fields':['title']}),
        ('توضیحات مطلب', {'fields': ['content']}),
        ('انتخاب نویسنده', {'fields': ['writer']}),
        ('انتخاب تصویر برای پست', {'fields': ['image']}),
        ('انتخاب ویدیو برای پست', {'fields': ['video']}),
        ('لایک', {'fields': ['like']}),
    ]
    list_display=['title', 'date', 'writer']
    search_fields=['title', 'content']

admin.site.register(Blog, BlogAdmin)
