
from django import forms
from .models import Categorie, Annonce, Image, Comment, MpUser


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
            'title': forms.TextInput({'class': 'checkout__input'}),
            'product': forms.TextInput({'class': 'checkout__input'}),
            'price': forms.TextInput({'class': 'checkout__input'}),
            'type_annonce': forms.Select({'class': 'checkout__inputl'}),
            'categories': forms.Select({'class': 'checkout__input'}),
            'description': forms.Textarea({'class': 'checkout__input'}),
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
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text here', 'rows': '3', 'cols':'40'})) 
    
    class Meta:
        model = Comment
        fields = ("content",)


class MpUserForm(forms.ModelForm):
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Subject', }))    
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'input1', 'placeholder': 'Message', 'name': 'message', 'rows': '5', 'cols':'40'}))    
    
    class Meta:
        model = MpUser
        fields = ("subject","message",)
    
