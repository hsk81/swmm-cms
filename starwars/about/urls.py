from django.conf               import settings
from django.conf.urls.defaults import *

from about.views import *

urlpatterns = patterns ('django.views.generic.simple',

 ## url (
 ##     r'^$', 'direct_to_template', {
 ##         'template': 'about.html',
 ##         'extra_context': {
 ##             'properties': PropertyController.values (None)
 ##         }
 ##     }, name="master"
 ## ),

    url(
        r'^$', AboutController.default, name="default"
    ),

)
