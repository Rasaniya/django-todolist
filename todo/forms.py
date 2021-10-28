from django import forms
from django.forms import ModelForm

from .models import *

class TodoForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Todo
        fields='__all__'