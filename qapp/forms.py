from django.forms import ModelForm
from django import forms

from qapp.models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body','date_added')
        