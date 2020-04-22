
from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile, Adresse
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """ Class form for user registration
    """
    

    def __init__(self, *args, **kwargs):
        """Hide help message for register user
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['email'].widget.attrs.update({'class': 'form-control'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})
            self.fields[fieldname].help_text = None

    class Meta:
        """ Display field to input text
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']

class adresseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rue'].widget.attrs.update({'class': 'form-control'})
        self.fields['ville'].widget.attrs.update({'class': 'form-control'})
        self.fields['Zip'].widget.attrs.update({'class': 'form-control'})
        self.fields['pays'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Adresse
        fields = "__all__"
        

class profileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Profile
        fiels = ('avatar', 'telephone' )
        exclude = ['user', 'adresse']