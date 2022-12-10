from django.shortcuts import render
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
      new_classification = form.cleaned_data['new_classification']
      new_species = form.cleaned_data['new_species']
      new_common_name = form.cleaned_data['new_common_name']
      new_name = form.cleaned_data['new_name']

      new_animal = Animal(
        classification = new_classification,
        species = new_species,
        common_name = new_common_name,
        name = new_name
      )

      new_animal.save()
      return render(request, './add.html', {
        'form': AnimalForm,
        'success': True
      })
  else:
    form = AnimalForm()
  return render(request, './add.html', {
    'form': AnimalForm()
  })

  return render(request, 'add.html')

