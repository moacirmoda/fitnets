from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^new/?$', 'project.views.new'),
    url(r'^(?P<id>\d+)-(?P<slug>[\w_-]+)\.html?$', 'project.views.show'),
    url(r'^comment/(?P<project>\d+)/?$', 'project.views.comment'),
    url(r'^create-training-day/(?P<project>\d+)/?$', 'project.views.create_training_day'),
    url(r'^create-training-exercise/(?P<project>\d+)/?$', 'project.views.create_training_exercise'),
    url(r'^delete-train/(?P<train>\d+)/?$', 'project.views.delete_train'),
    url(r'^create-evolution/(?P<project>\d+)/?$', 'project.views.create_evolution'),
    url(r'^create-meal/(?P<project>\d+)/?$', 'project.views.create_meal'),
    url(r'^create-suplement/(?P<project>\d+)/?$', 'project.views.create_suplement'),
)
