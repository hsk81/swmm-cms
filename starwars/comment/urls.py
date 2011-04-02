from django.conf.urls.defaults import *

from comment.views import *
from comment.models import *

urlpatterns = patterns ('django.views.generic.simple',

    url(
        r'^info/$',
        CommentController.info,
        name="info"
    ),

    url(
        r'^$',
        CommentController.default,
        name="default"
    ),

    url(
        r'^thread/(?P<id>\d+)/$',
        CommentController.thread,
        name="thread"
    ),

)
