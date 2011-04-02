from django.conf.urls.defaults import *

from contact.views import *
from contact.models import *

urlpatterns = patterns ('django.views.generic.simple',

    url(
        r'^info/$',
        ContactController.info,
        name="info"
    ),

    url(
        r'^$',
        ContactController.default,
        name="default"
    ),

)
