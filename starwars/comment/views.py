from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from time import time
from datetime import datetime
from property.views import *
from comment.models import *

import sys
import json

class CommentController:

    def info (request):

        js_string = json.dumps ({
            'application': 'comment',
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

            CommentController.init (request)

        else:

            request.session['timestamp'] = datetime.now ()
            request.session.save ()

        print >> sys.stderr, "== "
        print >> sys.stderr, "== Session ID: %s" % request.session.session_key
        print >> sys.stderr, "== Time Stamp: %s" % request.session['timestamp']
        print >> sys.stderr, "== "

        return CommentController.main (request)

    default = staticmethod (default)

    def main (request):

        threads = Thread.objects.all ()
        comments = Comment.objects.all ()

        try: return direct_to_template (
            request, template = 'comment.html', extra_context = {
                'threads': threads,
                'comments': comments,
                'properties': PropertyController.datas (request)
            }
        )

        except TemplateDoesNotExist: raise Http404()

    main = staticmethod (main)
