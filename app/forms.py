from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
  class Meta:
    model = Animal
    fields = ['classification', 'species', 'common_name', 'name']
    labels = {
      'classification': 'Classification',
      'species': 'Species',
      'common_name': 'Common Name',
      'name': 'Name',
    }
    widgets = {
      'classification': forms.TextInput(attrs={'class': 'form-control'}),
      'species': forms.TextInput(attrs={'class': 'form-control'}),
      'common_name': forms.TextInput(attrs={'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control'}),
    }