from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.core.mail import send_mail

from time import time
from datetime import datetime
from contact.forms import *
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

        if request.method == 'POST':

            form = ContactForm (request.POST)

            if form.is_valid ():
                
                sender = form.cleaned_data['sender']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                send_mail (
                    'Star Wars - Micro Machines', 
                    message, 
                    sender, 
                    ['swmm.sk@gmail.com', 'serdarkalfa@hotmail.com']                    
                )

                return HttpResponseRedirect ('?sender=%s&email=%s' % (sender, email))

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

