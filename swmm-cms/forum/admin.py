from django.contrib import admin
from models import *

class AttributesInline (admin.TabularInline):

    model = Comment.attributes.through
    extra = 1

class CommentAdmin (admin.ModelAdmin):

    fieldsets = [(None, {'fields': ['thread','username','email','text']})]
    list_display = ('id','thread','timestamp','username','email')
    list_filter = ['thread','timestamp','username','email']
    search_fields = ['username', 'email', 'text', 'thread__name']

    inlines = [AttributesInline]
    exclude = ('attributes',)

class CommentInline (admin.StackedInline):

    fieldsets = [(None, {'fields': ['username','email','text']})]
    ordering = ['-timestamp']
    model = Comment
    extra = 1

class ThreadAdmin (admin.ModelAdmin):

    inlines = [CommentInline]    
    list_display = ('name', 'number_of_comments', 'id')
    search_fields = [
        'name', 'comment__username', 'comment__email', 'comment__text'
    ]

admin.site.register (Comment, CommentAdmin)
admin.site.register (Thread, ThreadAdmin)
