from django.conf.urls.defaults import *

from about.views import *
from about.models import *

urlpatterns = patterns ('django.views.generic.simple',

    url(
        r'^info/$',
        AboutController.info,
        name="info"
    ),

    url(
        r'^$',
        AboutController.default,
        name="default"
    ),

)
