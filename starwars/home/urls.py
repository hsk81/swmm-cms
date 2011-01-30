from django.conf import settings
from django.conf.urls.defaults import *

from home.views import *
from home.models import *

urlpatterns = patterns ('django.views.generic.simple',

 ## url (
 ##     r'^$', 'direct_to_template', {
 ##         'template': 'index.html',
 ##         'extra_context': {'galleries': Gallery.objects.all()}
 ##     }, name="master"
 ## ),

    url(
        r'^$',
        HomeController.main,
        name="default"
    ),

    url(
        r'^all/$',
        HomeController.galleries_all,
        name="view.galleries-all"
    ),

    url(
        r'^(?P<id>\d+)/$',
        HomeController.galleries_by_collection,
        name="view.galleries-by-collection"
    ),

    url (
        r'^ajax/query-layout/$',
        HomeController.query_layout,
        name='ajax.query-layout'
    ),

    url (
        r'^ajax/toggle-layout/$',
        HomeController.toggle_layout,
        name='ajax.toggle-layout'
    ),

    url (
        r'^ajax/show-vehicle/$',
        HomeController.show_vehicle,
        name='ajax.show-vehicles'
    ),

    url (
        r'^ajax/show-figure/$',
        HomeController.show_figure,
        name='ajax.show-figures'
    ),

    url (
        r'^ajax/update-rate/$',
        HomeController.update_rate,
        name='ajax.update-rate'
    ),

)
