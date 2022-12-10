from django.shortcuts import render
from django.contrib import messages
from .models import Animal
from .forms import AnimalForm

# Create your views here.
def index(request):
  return render(request, 'index.html', {
    'animals': Animal.objects.all()
  })

def add(request):
  if request.method == 'POST':
    form = AnimalForm(request.POST)
    if form.is_valid():
      new_classification = form.cleaned_data['classification']
      new_species = form.cleaned_data['species']
      new_common_name = form.cleaned_data['common_name']
      new_name = form.cleaned_data['name']

      new_animal = Animal(
        classification = new_classification,
        species = new_species,
        common_name = new_common_name,
        name = new_name
      )

      new_animal.save()
      messages.success(request, 'New animal saved successfully')
      return render(request, './add.html', {
        'form': AnimalForm,
        'success': True
      })
  else:
    form = AnimalForm()
  return render(request, './add.html', {
    'form': AnimalForm()
  })
