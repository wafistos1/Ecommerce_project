
from django import forms
from .models import Categorie, Annonce, Image, Comment


class categorieFrom(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'


class annonceFrom(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'product': forms.TextInput({'class': 'form-control'}),
            'price': forms.TextInput({'class': 'form-control'}),
            'type_annonce': forms.Select({'class': 'form-control'}),
            'categories': forms.Select({'class': 'form-control'}),
            'description': forms.Textarea({'class': 'form-control'}),

        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('image', )
        widgets = {
            'image' : forms.FileInput(attrs={'class': 'input-image-control'}),
        }


class editAnnonceForm(forms.ModelForm):
    template_name = '/annonce/update.html'

    class Meta:
        model = Annonce
        fields = '__all__' 
        exclude = ['owner']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class commentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)

