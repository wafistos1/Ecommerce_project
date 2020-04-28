

from .models import Profile
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    picture = forms.FileField()
    adress1 = forms.CharField(max_length=255)
    adress2 = forms.CharField(max_length=255)
    ville = forms.CharField(max_length=255)
    codezip = forms.CharField(max_length=50)
    contry = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    discriptions = forms.CharField(max_length=255)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1',  'password2', 'first_name', 'last_name','picture',)
    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.picture = self.cleaned_data['picture']
        user.adress1 = self.cleaned_data['adress1']
        user.adress2 = self.cleaned_data['adress2']
        user.ville = self.cleaned_data['ville']
        user.codezip = self.cleaned_data['codezip']
        user.phone = self.cleaned_data['phone']
        user.discriptions = self.cleaned_data['discriptions']
        user.save()


