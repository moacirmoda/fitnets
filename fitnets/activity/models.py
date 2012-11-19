#! coding: utf-8
from django.core.urlresolvers import reverse
from django.db.models import signals 
from django.db import models
from project.models import *
from datetime import datetime

class Activity(models.Model):

    class Meta:
        verbose_name = "Atividade de amigos"
        verbose_name_plural = "Atividades de amigos"
    
    created = models.DateTimeField(default=datetime.now(), editable=False)
    creator = models.ForeignKey(User)
    message = models.CharField(max_length=255)
    link = models.URLField()

    def __unicode__(self):
        return unicode(self.message)

def create_activity(sender, instance, created, **kwargs):

    classname = instance.__class__.__name__

    activity = Activity()
    
    if classname == "Project":
        project = instance
        activity.message = "criou um novo projeto"
        activity.creator = project.creator

    if classname == "CommentProject":
        project = instance.project
        activity.message = "comentou em um projeto"
        activity.creator = project.creator

    if classname == "TrainingDay":
        project = instance.project
        activity.message = "criou um dia de treino"
        activity.creator = project.creator

    if classname == "TrainingExercise":
        project = instance.project
        activity.message = "criou um novo exercício"
        activity.creator = project.creator

    if classname == "Evolution":
        project = instance.project
        activity.message = "adicionou uma foto de sua evolução"
        activity.creator = project.creator

    if classname == "Meal":
        project = instance.project
        activity.message = "adicionou uma nova dieta"
        activity.creator = project.creator

    if classname == "Suplemento":
        project = instance.project
        activity.message = "adicionou um novo suplemento"
        activity.creator = project.creator

    activity.link = reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()})
    activity.save()

signals.post_save.connect(create_activity, sender=Project, dispatch_uid="1")
signals.post_save.connect(create_activity, sender=CommentProject, dispatch_uid="2")
signals.post_save.connect(create_activity, sender=TrainingDay, dispatch_uid="3")
signals.post_save.connect(create_activity, sender=TrainingExercise, dispatch_uid="4")
signals.post_save.connect(create_activity, sender=Evolution, dispatch_uid="5")
signals.post_save.connect(create_activity, sender=Meal, dispatch_uid="6")
signals.post_save.connect(create_activity, sender=Suplemento, dispatch_uid="7")
