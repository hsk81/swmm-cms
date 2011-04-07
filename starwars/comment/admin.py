from django.contrib import admin
from comment.models import *

class CommentAdmin (admin.ModelAdmin):

    fieldsets = [(None, {'fields': ['thread','username','email', 'attributes', 'text']})]
    list_display = ('thread','timestamp','username','email','id')    
    search_fields = ['username', 'email', 'text', 'thread__name']

class CommentInline (admin.StackedInline):

    fieldsets = [(None, {'fields': ['username','email', 'attributes', 'text']})]    
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
