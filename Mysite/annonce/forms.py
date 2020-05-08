
from django import forms
from .models import Categorie, Annonce, Image


class categorieFrom(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'


class annonceFrom(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['owner']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('image', )


class editAnnonceForm(forms.ModelForm):
    template_name = '/annonce/update.html'

    class Meta:
        model = Annonce
        exclude = ['owner']
        
