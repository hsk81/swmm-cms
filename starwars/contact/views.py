from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from time import time
from datetime import datetime
from property.views import *

import sys
import json

class ContactController:

    def init (request):

        pass

    init = staticmethod (init)

    def default (request):

        if request.session.has_key ('timestamp') != True:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

            ContactController.init (request)

        else:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

        print >> sys.stderr, "== "
        print >> sys.stderr, "== Session ID: %s" % request.session.session_key
        print >> sys.stderr, "== Time Stamp: %s" % request.session['timestamp']
        print >> sys.stderr, "== "

        return ContactController.main (request)

    default = staticmethod (default)

    def main (request):

        try: return direct_to_template (
            request, template = 'contact.html', extra_context = {
                'properties': PropertyController.datas (None)
            }
        )

        except TemplateDoesNotExist: raise Http404()

    main = staticmethod (main)
