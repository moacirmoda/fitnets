from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^new/(?P<id>\d+)/?$', 'wall.views.new'),
    url(r'^like/(?P<id>\d+)/?$', 'wall.views.like'),
    url(r'^unlike/(?P<id>\d+)/?$', 'wall.views.unlike'),
    url(r'^more/(?P<user>\d+)/(?P<from_>\d+)/?$', 'wall.views.more'),
)
