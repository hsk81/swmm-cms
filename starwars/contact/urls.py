from django.conf               import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',

    url (
        r'^$', 'direct_to_template', {
            'template': 'contact.html',
            'extra_context': {}
        }, name="master"
    ),

)