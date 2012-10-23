from django import forms
from models import *

class NumberInput(forms.widgets.TextInput):
    """ Custom widget para adaptar com HTML5 """
    input_type = 'number'

class DateInput(forms.widgets.TextInput):
    """ Custom widget para adaptar com HTML5 """
    input_type = 'date'

class EditUserForm(forms.ModelForm):

    weight = forms.CharField(label="Peso", widget=NumberInput(attrs={'min': '0', 'step': '1'}))
    height = forms.CharField(label="Altura", widget=NumberInput(attrs={'min': '0', 'step': '1'}))
    born = forms.CharField(label="Data de Nascimento", widget=DateInput())

    class Meta:
        model = UserProfile
        exclude = ('user', )
