#! coding: utf-8
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

    def __unicode__(self):
        return unicode(self.objective)
