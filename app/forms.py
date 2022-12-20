from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
  class Meta:
    model = Animal
    fields = ['classification', 'species', 'common_name', 'name']
    CLASSIFICATION_CHOICES = (
      ('', ''),
      ('Mammals', 'Mammals'),
      ('Reptiles', 'Reptiles'),
      ('Amphibians', 'Amphibians',),
      ('Birds', 'Birds'),
      ('Fish', 'Fish'),
      ('Insects', 'Insects'),
      ('Arachnids', 'Arachnids'),
    )
    labels = {
      'classification': 'Classification',
      'species': 'Species',
      'common_name': 'Common Name',
      'name': 'Name',
    }
    widgets = {
      'classification': forms.Select(choices=CLASSIFICATION_CHOICES, attrs={'class': 'form-control', 'style': 'color: black'}),
      'species': forms.TextInput(attrs={'class': 'form-control'}),
      'common_name': forms.TextInput(attrs={'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control'}),
    }