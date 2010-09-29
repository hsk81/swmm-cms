from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from home.models import *

def galleries_all (request):

    gs = Gallery.objects.all()
 ## gs = sorted (gs, lambda x,y: x.id > y.id)

    try: return direct_to_template (
        request,
        template = 'index.html',
        extra_context = {
            'galleries': gs
        }
    )

    except TemplateDoesNotExist: raise Http404()

def galleries_by_episode (request, episode_id):

    gs = filter (lambda g: true, Gallery.objects.all())
 ## gs = sorted (gs, lambda x,y: x.id > y.id)

    try: return direct_to_template (
        request,
        template = 'index.html',
        extra_context = {
            'galleries': gs
        }
    )

    except TemplateDoesNotExist: raise Http404()
