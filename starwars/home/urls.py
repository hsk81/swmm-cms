from django.conf.urls.defaults import *

from home.views import *
from home.models import *

urlpatterns = patterns ('django.views.generic.simple',

    url(
        r'^info/$',
        HomeController.info,
        name="info"
    ),

    url(
        r'^$',
        HomeController.default,
        name="default"
    ),

    url(
        r'^(?P<id>\d+)/$',
        HomeController.galleries_by_collection,
        name="view.galleries-by-collection"
    ),

    url (
        r'^show-vehicles/(?P<id>\d+)/$',
        HomeController.show_vehicle,
        name='view.show-vehicles'
    ),

    url (
        r'^show-figures/(?P<id>\d+)/$',
        HomeController.show_figure,
        name='view.show-figures'
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
        r'^ajax/update-rate/$',
        HomeController.update_rate,
        name='ajax.update-rate'
    ),

)
