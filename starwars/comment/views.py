from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

from datetime import datetime
from comment.forms import *
from comment.models import *
from property.views import *
from attribute.models import *

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

        if Thread.objects.count () > 0:
            return CommentController.thread (request, 1)
        else:
            return CommentController.main (request)

    default = staticmethod (default)

    def main (request, id = 0, form = None):

        threads = Thread.objects.all ()
        comments = Comment.objects.filter (thread__id = id)

        try: return direct_to_template (
            request, template = 'comment.html', extra_context = {
                'threads': threads,
                'comments': comments.order_by('-timestamp'),
                'properties': PropertyController.datas (request),
                'thread_id': id,
                'form': form,
            }
        )

        except TemplateDoesNotExist: raise Http404()

    main = staticmethod (main)

    def thread (request, id):

        if request.method == 'POST':

            form = CommentForm (request.POST)
            if form.is_valid ():

                comment = Comment (
                    thread = Thread.objects.get (pk = id),
                    username = form.cleaned_data['sender'],
                    text = form.cleaned_data['message'],
                    email = form.cleaned_data['email'],
                )

                comment.save ()

                for (key,value) in request.META.items ():

                    if key == None or value == None:

                        continue

                    else:

                        key = repr (key[0:32])
                        value = repr (value)

                    keys = AttributeKey.objects.filter (content = key)
                    if not keys:
                        attribute_key = AttributeKey (content = key)
                        attribute_key.save ()
                    else:
                        attribute_key = keys[0]

                    values = AttributeValue.objects.filter (content = value)
                    if not values:
                        attribute_value = AttributeValue (content = value)
                        attribute_value.save ()
                    else:
                        attribute_value = values[0]

                    attributes = Attribute.objects.filter (
                        key = attribute_key, value = attribute_value
                    )

                    if not attributes:
                        attribute = Attribute (
                            key = attribute_key, value = attribute_value
                        ); attribute.save ()
                    else:
                        attribute = attributes[0]

                    comment.attributes.add (attribute)

                return HttpResponseRedirect (
                    '?sender=%s&email=%s' % (comment.username, comment.email)
                )

        else:

            form = CommentForm ()

        return CommentController.main (request, id, form)

    thread = staticmethod (thread)
