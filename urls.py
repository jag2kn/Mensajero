from django.conf.urls.defaults import *

#from identica.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', home, name='home'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)




