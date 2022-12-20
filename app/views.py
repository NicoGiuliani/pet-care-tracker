from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        'animals': Animal.objects.all(),
        'success': True,
      })
  else:
    form = AnimalForm()
  return render(request, './add.html', {
    'form': AnimalForm(),
    'animals': Animal.objects.all()
  })


def delete(request, id):
  if request.method == 'POST':
    animal = Animal.objects.get(pk=id)
    animal.delete()
  return HttpResponseRedirect(reverse('index'))

def edit(request, id):
  if request.method == 'POST':
    animal = Animal.objects.get(pk=id)
    form = AnimalForm(request.POST, instance=animal)
    if form.is_valid():
      form.save()
      messages.success(request, 'Record saved successfully')
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else: 
    animal = Animal.objects.get(pk=id)
    form = AnimalForm(instance=animal)
  return render(request, 'edit.html', {
    'form': form
  })
