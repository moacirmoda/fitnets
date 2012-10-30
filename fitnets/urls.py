from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^messages/', include('messages.urls')),
    url(r'profile/', include('account.urls')),
    url(r'wall/', include('wall.urls')),
    url(r'friends/', include('friends.urls')),
    url(r'project/', include('project.urls')),
    url(r'', include('main.urls')),

    url(r'^user/(?P<username>[\w_-]+)/?$', 'account.views.profile'),
    url(r'^user/(?P<username>[\w_-]+)/projects/?$', 'project.views.list'),
    url(r'^user/(?P<username>[\w_-]+)/projects/(?P<type>[\w_-]+)/?$', 'project.views.list'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
