from django.conf import settings
from django.conf.urls.defaults import *
from home.views import *
from home.models import *

urlpatterns = patterns('django.views.generic.simple',

 ## url (
 ##     r'^$', 'direct_to_template', {
 ##         'template': 'index.html',
 ##         'extra_context': {'galleries': Gallery.objects.all()}
 ##     }, name="master"
 ## ),

    url(
        r'^$',
        galleries_all,
        name="galleries_all"
    ),

    url(
        r'^(?P<id>\d+)/$',
        galleries_by_collection,
        name="galleries_by_collection"
    ),

)
