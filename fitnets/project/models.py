#! coding: utf-8
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db import models
from wall.models import Generic
from datetime import datetime

class Project(Generic):

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    objective = models.CharField("objetivo", max_length=255)
    duration = models.IntegerField("duração")
    init = models.DateField("data de início", default=datetime.today())
    frequency = models.IntegerField("frequência")
    finished = models.BooleanField("finalizado?")
    comment = models.TextField("comentários", blank=True, null=True)

    def __unicode__(self):
        return unicode(self.objective)

    def slugify(self):
        return slugify(unicode(self.objective))

    def permalink(self):
        return reverse("project.views.show", kwargs={'id': self.id, 'slug': self.slugify()})

