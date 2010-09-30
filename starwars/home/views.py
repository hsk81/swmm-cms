from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from home.models import *

def galleries_all (request):

    cs = Collection.objects.all ()
    gs = Gallery.objects.filter (ignore=False)

    try: return direct_to_template (
        request,
        template = 'index.html',
        extra_context = {
            'collections': cs,
            'galleries': gs
        }
    )

    except TemplateDoesNotExist: raise Http404()

def galleries_by_collection (request, id):

    cs = Collection.objects.all ()
    gs = Collection.objects.get (pk=id).galleries ()
 
    try: return direct_to_template (
        request,
        template = 'index.html',
        extra_context = {
            'collections': cs,
            'galleries': gs
        }
    )

    except TemplateDoesNotExist: raise Http404()
