from django.conf.urls.defaults import *

from views import *
from models import *

urlpatterns = patterns ('django.views.generic.simple',

    url(
        r'^info/$',
        ForumController.info,
        name="info"
    ),

    url(
        r'^$',
        ForumController.default,
        name="default"
    ),

    url(
        r'^thread/(?P<id>\d+)/$',
        ForumController.thread,
        name="thread"
    ),

)
