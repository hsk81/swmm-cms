from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from datetime import datetime
from about.models import *
from property.views import *

import sys
import json

class AboutController:

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

    def init (request):

        pass

    init = staticmethod (init)

    def main (request):

        try: return direct_to_template (
            request, template = 'about.html', extra_context = {
                'properties': PropertyController.values (request)
            }
        )

        except TemplateDoesNotExist: raise Http404()

    main = staticmethod (main)
    