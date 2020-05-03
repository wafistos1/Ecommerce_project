
from django import forms
from .models import Categorie, Annonce


class categorieFrom(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'


class annonceFrom(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['owner']
