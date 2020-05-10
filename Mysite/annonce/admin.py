from django.contrib import admin
from .models import Categorie, Annonce, Image

# Register your models here.
admin.site.register(Categorie)  # delete group
admin.site.register(Annonce)  # delete group
admin.site.register(Image)  # delete group
