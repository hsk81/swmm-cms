from django.contrib import admin
from home.models import *

class ImageInline (admin.TabularInline):

    model = Image
    extra = 2

class GalleryAdmin (admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['color','name','url','ignore']})
    ]

    inlines = [ImageInline]
    list_display = ('id','name','color','url','ignore')
    list_filter = ['color','ignore']
    search_fields = ['name','id']

class ImageAdmin (admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['gallery','name','url','rate','ignore']})
    ]

    list_display = ('id','gallery','name','url','rate','ignore')
    list_filter = ['ignore','rate']
    search_fields = ['name','id']

admin.site.register (Gallery, GalleryAdmin)
admin.site.register (Image, ImageAdmin)
