from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^dashboard/?$', 'account.views.dashboard'),
    url(r'^(?P<username>[\w_-]+)/?$', 'account.views.profile'),
)
