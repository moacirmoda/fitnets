from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^new/?$', 'project.views.new'),
)
