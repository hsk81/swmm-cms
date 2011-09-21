from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from about.models import *
from property.views import *

import sys
import json

class AboutController:

    @csrf_exempt
    def info (request):

        js_string = json.dumps ({
            'application': 'about',
            'version': 'v0.0.1'
        })

        return HttpResponse (u'%s\n' % js_string, mimetype='application/json')

    info = staticmethod (info)

    @csrf_protect
    def default (request):

        if request.session.has_key ('timestamp') != True:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

            AboutController.init (request)

        else:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

        print >> sys.stderr, "== "
        print >> sys.stderr, "== Session ID: %s" % request.session.session_key
        print >> sys.stderr, "== Time Stamp: %s" % request.session['timestamp']
        print >> sys.stderr, "== "

        return AboutController.main (request)

    default = staticmethod (default)

    @csrf_protect
    def init (request):

        pass

    init = staticmethod (init)

    @csrf_protect
    def main (request):

        try: return direct_to_template (
            request, template = 'about.html', extra_context = {'properties': dict (
                PropertyController.datas (request),
             ** PropertyController.texts (request)
            )}
        )

        except TemplateDoesNotExist: raise Http404()

    main = staticmethod (main)
