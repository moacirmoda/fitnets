# coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from account.forms import NumberInput, DateInput
from datetime import datetime
from django import forms
from models import *

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ('comment', 'finished')

    init = forms.CharField(label="Data de Início", widget=DateInput())
    duration = forms.CharField(label="Duração (em meses)", widget=NumberInput(attrs={'min': 1, 'max': 12}))
    frequency = forms.CharField(label="Frequência (em dias)", widget=NumberInput(attrs={'min': 1, 'max': 7}))

    creator = forms.CharField(label="", widget=forms.HiddenInput(), required=False)
    updater = forms.CharField(label="", widget=forms.HiddenInput(), required=False)
    created = forms.CharField(label="", widget=forms.HiddenInput(), required=False)
    updated = forms.CharField(label="", widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        cleaned_data['creator'] = get_current_user()
        cleaned_data['updater'] = get_current_user()
        cleaned_data['created'] = datetime.now()
        cleaned_data['updated'] = datetime.now()

        return cleaned_data

