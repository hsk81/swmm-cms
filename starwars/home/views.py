from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from datetime import datetime
from home.models import *

import sys
import json

class View:

    def init (request):

        pass

    init = staticmethod (init)

    def main (request):

        if request.session.has_key ('timestamp') != True:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

            View.init (request)

        else:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

        print >> sys.stderr, "== "
        print >> sys.stderr, "== Session ID: %s" % request.session.session_key
        print >> sys.stderr, "== Time Stamp: %s" % request.session['timestamp']
        print >> sys.stderr, "== "

        return View.galleries_all (request)

    main = staticmethod (main)

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

    galleries_all = staticmethod (galleries_all)

    def galleries_by_collection (request, id):

        collection = Collection.objects.get (pk=id)
        cs = Collection.objects.all ()
        gs = collection.galleries ()

        try: return direct_to_template (
            request,
            template = 'index.html',
            extra_context = {
                'collection' : collection,
                'collections': cs,
                'galleries': gs
            }
        )

        except TemplateDoesNotExist: raise Http404()

    galleries_by_collection = staticmethod (galleries_by_collection)

class Ajax:

    def info (request):

        js_string = json.dumps ({
            'version' : '0.1'
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    info = staticmethod (info)

    def query_layout (request):

        if request.session.has_key ('overflow') != True:

            js_string = json.dumps ({
                'success' : False
            })

        else:

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
