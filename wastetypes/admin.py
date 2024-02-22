from django.contrib import admin 
from .models import BiowasteModel,NonbiowasteModel,HazardouswasteModel

# Register your models here.
admin.site.register(BiowasteModel)
admin.site.register(NonbiowasteModel)
admin.site.register(HazardouswasteModel)

