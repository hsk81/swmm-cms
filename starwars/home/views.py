from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from time import time
from datetime import datetime
from property.views import *
from home.models import *

import sys
import json

class HomeController:

    def info (request):

        js_string = json.dumps ({
            'application': 'home',
            'version': 'v0.0.1'
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    info = staticmethod (info)

    def init (request):

        pass

    init = staticmethod (init)

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

    def main (request):

        if Gallery.objects.count () > 0:
            return HomeController.galleries_by_collection (request, 1)
        else:
            return HomeController.galleries_all (request)

    main = staticmethod (main)

    def type_or_default (request):

        return request.session.has_key ('type') and request.session['type'] \
               or 'figure'

    type_or_default = staticmethod (type_or_default)

    def galleries_all (request):

        cs = Collection.objects.all ()

        gs = Gallery.objects.filter (
            ignore = False,
            type = HomeController.type_or_default (request)
        )

        try: return direct_to_template (
            request,
            template = 'index.html',
            extra_context = {
                'collections': cs,
                'galleries': gs,
                'type': HomeController.type_or_default (request),
                'properties': PropertyController.datas (request)
            }
        )

        except TemplateDoesNotExist: raise Http404()

    galleries_all = staticmethod (galleries_all)

    def galleries_by_collection (request, id):

        collection = Collection.objects.get (pk=id)
        cs = Collection.objects.all ()

        gs = Gallery.objects.filter (
            collection = collection,
            ignore = False,
            type = HomeController.type_or_default (request)
        )

        try: return direct_to_template (
            request,
            template = 'index.html',
            extra_context = {
                'collection' : collection,
                'collections': cs,
                'galleries': gs,
                'type': HomeController.type_or_default (request),
                'properties':  dict ([
                    PropertyController.data (request, 'lhs-image-href'),
                    PropertyController.data (request, 'lhs-image-desc'),
                    PropertyController.data (request, 'rhs-image-href'),
                    PropertyController.data (request, 'rhs-image-desc'),

                    PropertyController.data (request, 'sub-title'),
                    PropertyController.data (request, 'title')
                ])
            }
        )

        except TemplateDoesNotExist: raise Http404()

    galleries_by_collection = staticmethod (galleries_by_collection)

    def query_layout (request):

        if request.session.has_key ('overflow') != True:

            request.session['overflow'] = 'hidden'

        js_string = json.dumps ({
            'overflow': request.session['overflow'],
            'success': True
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    query_layout = staticmethod (query_layout)
    
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

    def show_vehicle (request):

        request.session['type'] = 'vehicle'

        js_string = json.dumps ({
            'type': request.session['type'],
            'success': True
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    show_vehicle = staticmethod (show_vehicle)

    def show_figure (request):

        request.session['type'] = 'figure'

        js_string = json.dumps ({
            'type': request.session['type'],
            'success': True
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    show_figure = staticmethod (show_figure)

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
                        = "%s" % time ()
                    
                    image = Image.objects.get (pk = request.POST['id'])
                    image.update_rate (float (request.POST['rate']))
                    image.save ()

                    js_string = json.dumps ({
                        'success': True,
                        'rate': image.rate
                    })

            else:

                request.session["image-id%s" % request.POST['id']] \
                    = "%s" % time ()

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
