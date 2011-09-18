from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from property.views import *
from models import *

import sys
import json

class HomeController:

    @csrf_exempt
    def info (request):

        js_string = json.dumps ({
            'application': 'home',
            'version': 'v0.0.1'
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    info = staticmethod (info)

    @csrf_protect
    def init (request):

        pass

    init = staticmethod (init)

    @csrf_protect
    def default (request):

        if request.session.has_key ('timestamp') != True:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

            HomeController.init (request)

        else:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

        print >> sys.stderr, "== "
        print >> sys.stderr, "== Session ID: %s" % request.session.session_key
        print >> sys.stderr, "== Time Stamp: %s" % request.session['timestamp']
        print >> sys.stderr, "== "

        return HomeController.main (request)

    default = staticmethod (default)

    @csrf_protect
    def main (request):

        return HomeController.galleries_by_collection (request, 1)

    main = staticmethod (main)

    @csrf_protect
    def type_or_default (request):

        return request.session.has_key ('type') and request.session['type'] \
            or 'figure'

    type_or_default = staticmethod (type_or_default)

    @csrf_protect
    def galleries_by_collection (request, id):

        collection = Collection.objects.get (pk=id)

        gs = Gallery.objects.filter (
            collection = collection,
            ignore = False,
            type = HomeController.type_or_default (request)
        )

        cs = Collection.objects.all ()
        
        try: return direct_to_template (
            request,
            template = 'index.html',
            extra_context = {
                'collection' : collection,
                'collections': cs,
                'galleries': gs,
                'type': HomeController.type_or_default (request),
                'properties': PropertyController.datas (request),
            }
        )

        except TemplateDoesNotExist: raise Http404()

    galleries_by_collection = staticmethod (galleries_by_collection)

    @csrf_protect
    def query_layout (request):

        if request.session.has_key ('overflow') != True:

            request.session['overflow'] = 'hidden'

        js_string = json.dumps ({
            'overflow': request.session['overflow'],
            'success': True
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    query_layout = staticmethod (query_layout)

    @csrf_protect
    def toggle_layout (request):

        if request.POST.has_key ('overflow') != True:

            js_string = json.dumps ({
                'success': False
            })

        else:

            request.session['overflow'] = request.POST['overflow']
            
            js_string = json.dumps ({
                'overflow': request.session['overflow'],
                'success': True
            })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    toggle_layout = staticmethod (toggle_layout)

    @csrf_protect
    def show_vehicle (request, id):
        
        request.session['type'] = 'vehicle'
        return HomeController.galleries_by_collection (request, id)

    show_vehicle = staticmethod (show_vehicle)

    @csrf_protect
    def show_figure (request, id):

        request.session['type'] = 'figure'
        return HomeController.galleries_by_collection (request, id)

    show_figure = staticmethod (show_figure)

    @csrf_protect
    def update_rate (request):

        if request.POST.has_key ('id') and request.POST.has_key ('rate'):

            if request.session.has_key ("image-id%s" % request.POST['id']):

                dt = datetime.now () - datetime.fromtimestamp (
                    float (request.session["image-id%s" % request.POST['id']])
                )

                if dt.seconds < 60: ## rating only once per minute!

                    js_string = json.dumps ({
                        'success': False
                    })

                else:

                    request.session["image-id%s" % request.POST['id']] \
                        = "%s" % datetime.now ()
                    
                    image = Image.objects.get (pk = request.POST['id'])
                    image.update_rate (float (request.POST['rate']))
                    image.save ()

                    js_string = json.dumps ({
                        'success': True,
                        'rate': image.rate
                    })

            else:

                request.session["image-id%s" % request.POST['id']] \
                    = "%s" % datetime.now ()

                image = Image.objects.get (pk = request.POST['id'])
                image.update_rate (float (request.POST['rate']))
                image.save ()

                js_string = json.dumps ({
                    'success': True,
                    'rate': image.rate
                })

        else:

            js_string = json.dumps ({
                'success': False
            })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    update_rate = staticmethod (update_rate)
