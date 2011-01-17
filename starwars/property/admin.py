from django.contrib.sessions.models import Session
from django.contrib import admin
from property.models import *

class PropertyTextAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['property','text']}
    )]

    list_display = ['text','property']

admin.site.register (PropertyText, PropertyTextAdmin)

class PropertyDataAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['property','data']}
    )]

    list_display = ['data','property']

admin.site.register (PropertyData, PropertyDataAdmin)

class PropertyDataInline (admin.StackedInline):

    fieldsets = [(
        None, {'fields': ['data']}
    )]

    model = PropertyData
    extra = 1

class PropertyAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['name','type']}
    )]

    inlines = [PropertyDataInline]
    list_display = ['name','type']

admin.site.register (Property, PropertyAdmin)

class PropertyInline (admin.StackedInline):

    fieldsets = [(
        None, {'fields': ['name']}
    )]

    model = Property
    extra = 1

class PropertyTypeAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['name','regex']}
    )]

    inlines = [PropertyInline]
    list_display = ('name','regex')
    list_filter = ['name','regex']
    search_fields = ['name','regex']

admin.site.register (PropertyType, PropertyTypeAdmin)
