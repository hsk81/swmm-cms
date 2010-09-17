from django.conf.urls.defaults import *
from django.contrib            import admin

admin.autodiscover ()

urlpatterns = patterns ('',

    (r'^home/', include('home.urls', namespace='home')),
    (r'^about/', include('about.urls', namespace='about')),
 ## (r'^comment/', include('comment.urls', namespace='comment')),

    (r'^admin/', include(admin.site.urls)),
 ## (r'^admin/doc/', include('django.contrib.admindocs.urls')),
 ## (r'^comments/', include('django.contrib.comments.urls'))

)
