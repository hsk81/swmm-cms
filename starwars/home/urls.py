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

    ##
    ## urls: views
    ##

    url(
        r'^$',
        View.main,
        name="view.main"
    ),

    url(
        r'^all/$',
        View.galleries_all,
        name="view.galleries_all"
    ),

    url(
        r'^(?P<id>\d+)/$',
        View.galleries_by_collection,
        name="view.galleries_by_collection"
    ),

    ##
    ## urls: ajax
    ##

    url (
        r'^ajax/info/$',
        Ajax.info,
        name='ajax.info'
    ),

    url (
        r'^ajax/query-layout/$',
        Ajax.query_layout,
        name='ajax.query-layout'
    ),

    url (
        r'^ajax/toggle-layout/$',
        Ajax.toggle_layout,
        name='ajax.toggle-layout'
    ),

)
