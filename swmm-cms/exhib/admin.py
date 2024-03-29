from django.contrib import admin
from models import *

class GalleryInline (admin.TabularInline):

    model = Gallery
    extra = 2

class CollectionAdmin (admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']})
    ]

    inlines = [GalleryInline]
    list_display = ('id','name')
    search_fields = ['name','id']

class ImageInline (admin.StackedInline):

    fieldsets = [(
        None, {
            'fields': [
                'gallery','name','rate','url','url_large','url_info','ignore'
            ]
        }
    )]

    model = Image
    extra = 2

class GalleryAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {
            'fields': ['collection','name','color','type','url','ignore']
        }
    )]

    inlines = [ImageInline]
    list_display = ('id','collection','name','color','type','url','ignore')
    list_filter = ['collection','color','ignore']
    search_fields = ['name','id']

class ImageAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {
            'fields': [
                'gallery','name','url','url_large','url_info','rate','ignore'
            ]
        }
    )]

    list_display = ('id','gallery','name','url','rate','ignore')
    list_filter = ['ignore','rate']
    search_fields = ['name','id']

admin.site.register (Collection, CollectionAdmin)
admin.site.register (Gallery, GalleryAdmin)
admin.site.register (Image, ImageAdmin)
