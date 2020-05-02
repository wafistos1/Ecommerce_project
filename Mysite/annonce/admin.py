from django.contrib import admin
from .models import Categorie, Annonce

# Register your models here.
admin.site.register(Categorie)  # delete group
admin.site.register(Annonce)  # delete group
