from django import forms
from .import models

class AddList(forms.ModelForm):
    class Meta:
        model = models.ToDo
        fields = ['title']