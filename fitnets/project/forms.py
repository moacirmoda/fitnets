# coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from account.forms import NumberInput, DateInput
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from models import *

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ('comment', 'finished', 'creator', 'created', 'updater', 'updated')

    init = forms.CharField(label="Data de Início", widget=DateInput())
    duration = forms.CharField(label="Duração (em meses)", widget=NumberInput(attrs={'min': 1, 'max': 12}))
    frequency = forms.CharField(label="Frequência (em dias)", widget=NumberInput(attrs={'min': 1, 'max': 7}))


class CommentProjectForm(forms.ModelForm):

    class Meta:
        model = CommentProject
        exclude = ('created', 'updater', 'updated')

    project = forms.CharField(label="", widget=forms.HiddenInput())
    creator = forms.CharField(label="", widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(CommentProjectForm, self).clean()
        cleaned_data['project'] = Project.objects.get(id=cleaned_data['project'])
        cleaned_data['creator'] = User.objects.get(id=cleaned_data['creator'])
        return cleaned_data

class TrainingDayForm(forms.ModelForm):

    class Meta:
        model = TrainingDay
        exclude = ('created', 'updater', 'updated', 'creator')

    project = forms.CharField(label="", widget=forms.HiddenInput())
    duration = forms.CharField(label="Duração (em meses)", widget=NumberInput(attrs={'min': 1, 'max': 12}))
    init = forms.CharField(label="Início", widget=DateInput())

    def clean(self):
        cleaned_data = super(TrainingDayForm, self).clean()
        cleaned_data['project'] = Project.objects.get(id=cleaned_data['project'])
        return cleaned_data

class TrainingExerciseForm(forms.ModelForm):

    class Meta:
        model = TrainingExercise
        exclude = ('created', 'updater', 'updated', 'creator')
    

