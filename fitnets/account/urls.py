from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^dashboard/?$', 'account.views.dashboard'),
    url(r'^edit_profile/?$', 'account.views.edit_profile'),
    url(r'^user/(?P<username>[\w_-]+)/?$', 'account.views.profile'),
)
