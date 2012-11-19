#! coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from utils.thumbs import ImageWithThumbsField
from django.db import models
from datetime import datetime, date

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

class CommentProject(Generic):

    class Meta:
        verbose_name = "Comentário em Projeto"
        verbose_name_plural = "Comentários em Projeto"

    project = models.ForeignKey(Project)
    comment = models.TextField("comentário")

    def __unicode__(self):
        return unicode(self.comment)

class TrainingDay(Generic):

    DAY_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
    )

    class Meta:
        verbose_name = "Dia de Treino"
        verbose_name_plural = "Dias de Treino"

    project = models.ForeignKey(Project)
    day = models.CharField("Dia", choices=DAY_CHOICES, max_length=1)
    init = models.DateField("Início")
    duration = models.IntegerField("Duração")

    def __unicode__(self):
        return unicode("%s (inicio em: %s)" % (self.day, self.init))

class TrainingExercise(Generic):

    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"

    day = models.ForeignKey(TrainingDay)
    exercise = models.CharField("exercício", max_length=255)
    serie = models.IntegerField("séries")
    repetition = models.IntegerField("Repetições")

    def __unicode__(self):
        return unicode(self.exercise)

class Evolution(Generic):

    class Meta:
        verbose_name = "Evolução"
        verbose_name_plural = "Evoluções"

    project = models.ForeignKey(Project)
    photo = ImageWithThumbsField("Foto", upload_to='images', sizes=((94,94),(640,480)))
    date = models.DateField("Data", default=date.today())

class Food(Generic):

    meal = models.ForeignKey('Meal')
    food = models.CharField('alimento', max_length=255)

    def __unicode__(self):
        return unicode(self.food)

class Meal(Generic):

    MEAL_CHOICES = (
        ('1ª', '1'),
        ('2ª', '2'),
        ('1ª', '3'),
        ('1ª', '4'),
        ('1ª', '5'),
        ('1ª', '6'),
        ('1ª', '7'),
    )

    class Meta:
        verbose_name = "Refeição"
        verbose_name_plural = "Refeições"

    project = models.ForeignKey(Project)
    meal = models.CharField('refeição', max_length=1, choices=MEAL_CHOICES)

    def __unicode__(self):
        return unicode(self.meal)

    def foods(self):
        return Food.objects.filter(meal=self).order_by('-id')

class Suplemento(Generic):

    class Meta:
        verbose_name = "Suplementação"
        verbose_name_plural = "Suplementações"

    project = models.ForeignKey(Project)
    cat = models.ForeignKey('CatSuplemento', verbose_name="Categoria")
    suplement = models.ForeignKey('TypeSuplemento', verbose_name="Suplemento")
    product = models.CharField("Produto / Marca", max_length=255)

class CatSuplemento(Generic):

    class Meta:
        verbose_name = "Categoria de Suplemento"
        verbose_name_plural = "Categorias de Suplemento"

    product = models.CharField("Categoria", max_length=255)

    def __unicode__(self):
        return unicode(self.product)

class TypeSuplemento(Generic):

    class Meta:
        verbose_name = "Tipo de Suplemento"
        verbose_name_plural = "Tipos de Suplemento"

    title = models.CharField("Tipo de Suplemento", max_length=255)

    def __unicode__(self):
        return unicode(self.title)
