from django.conf.urls.defaults import *
from django.contrib            import admin

admin.autodiscover ()

urlpatterns = patterns ('',

    (r'^home/', include('exhib.urls', namespace='exhib')),
    (r'^about/', include('about.urls', namespace='about')),
    (r'^comment/', include('forum.urls', namespace='forum')),
    (r'^contact/', include('contact.urls', namespace='contact')),

    (r'^admin/', include(admin.site.urls)),
 ## (r'^admin/doc/', include('django.contrib.admindocs.urls')),
 ## (r'^comments/', include('django.contrib.comments.urls'))

)
