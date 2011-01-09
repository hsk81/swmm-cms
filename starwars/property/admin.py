from django.contrib.sessions.models import Session
from django.contrib import admin
from property.models import *

class PropertyValueAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['data']}
    )]

    list_display = ['data','property']

admin.site.register (PropertyValue, PropertyValueAdmin)

class PropertyValueInline (admin.StackedInline):

    fieldsets = [(
        None, {'fields': ['data']}
    )]

    model = PropertyValue
    extra = 1

class PropertyAdmin (admin.ModelAdmin):

    fieldsets = [(
        None, {'fields': ['name','type']}
    )]

    inlines = [PropertyValueInline]
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
