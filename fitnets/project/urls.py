from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^new/?$', 'project.views.new'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w_-]+)\.html?$', 'project.views.show'),
)
