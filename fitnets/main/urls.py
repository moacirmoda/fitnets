from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'main.views.dashboard'),
)
