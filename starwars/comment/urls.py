from django.conf               import settings
from django.conf.urls.defaults import *

from property.views import *

urlpatterns = patterns ('django.views.generic.simple',

    url (
        r'^$', 'direct_to_template', {
            'template': 'comment.html',
            'extra_context': {
                'properties': PropertyController.datas (None)
            }
        }, name="master"
    ),

)
