#! coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class Generic(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField("Data de criação", default=datetime.now())
    updated = models.DateTimeField("Data de atualização", default=datetime.now())
    creator = models.ForeignKey(User, default=get_current_user(), related_name="+", null=True, blank=True)
    updater = models.ForeignKey(User, default=get_current_user(), related_name="+", null=True, blank=True)

    def save(self):
        self.updated = datetime.now()
        self.updater = get_current_user()
        super(Generic, self).save()

class Post(Generic):

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

    user = models.ForeignKey(User)
    message = models.TextField("Publicação")
    like = models.IntegerField("Gostei", default=0)
    non_like = models.IntegerField("Não Gostei", default=0)
    parent = models.ForeignKey("Post", null=True, blank=True)

    def __unicode__(self):
        msg = self.message
        size = 20
        if(len(msg) > size):
            return unicode(self.message[:size] + "...")
        else:
            return unicode(self.message)