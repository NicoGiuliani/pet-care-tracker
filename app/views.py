from django.shortcuts import render
from .models import Animal

# Create your views here.
def index(request):
  return render(request, 'index.html', {
    'animals': Animal.objects.all()
  })

