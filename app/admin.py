from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
  list_display = ['classification', 'species', 'common_name', 'name']

# Register your models here.
admin.site.register(Animal, AnimalAdmin)