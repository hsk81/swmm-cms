from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from datetime import datetime
from contact.forms import *
from property.views import *
from property.models import *

import sys
import json

class ContactController:

    @csrf_exempt
    def info (request):

        js_string = json.dumps ({
            'application': 'contact',
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

    @csrf_protect
    def main (request):

        if request.method == 'POST':

            form = ContactForm (request.POST)
            if form.is_valid ():
                
                sender = form.cleaned_data['sender']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                from django.core.mail import send_mail
                send_mail (
                    'Star Wars - Micro Machines', message, sender, map (
                        lambda p: str (p), Property.datas ('contact-email')
                    )
                )

                return HttpResponseRedirect (
                    '?sender=%s&email=%s' % (sender, email)
                )

        else:

            if request.GET.has_key ('sender') and request.GET.has_key ('email'):

                form = ContactForm ({
                    'sender': request.GET['sender'],
                    'email': request.GET['email'],
                    'message': 'Your email has been sent! Thank you.'
                })

            else:

                form = ContactForm ()

        try: return direct_to_template (
            request, template = 'contact.html', extra_context = {
                'properties': PropertyController.datas (None),
                'form': form
            }
        )

        except TemplateDoesNotExist: raise Http404 ()

    main = staticmethod (main)
