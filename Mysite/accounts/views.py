from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import profileForm, UserRegisterForm, adresseForm
# Create your views here.
def home(request):
    return render(request, 'base.html')
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    print(request.POST)

    user_form = UserRegisterForm()
    adresse_form = adresseForm()
    profile_form = profileForm()
    

    return render(request, 'accounts/user.html', {
        'user_form': user_form, 
        'adresse_form': adresse_form, 
        "profile_form": profile_form
        })