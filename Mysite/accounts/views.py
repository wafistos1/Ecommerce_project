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
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        adresse_form = adresseForm(request.POST)
        profile_form = profileForm(request.POST, request.FILES)
        if user_form.is_valid() and adresse_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            adresse = adresse_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.adresse = adresse
            profile.save()
            messages.add_message(
                request, messages.SUCCESS, 'Profile inscrit avec succès veuillez vous connectez'
                )
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        adresse_form = adresseForm()
        profile_form = profileForm()
    

    return render(request, 'accounts/user.html', {
        'user_form': user_form, 
        'adresse_form': adresse_form, 
        "profile_form": profile_form
        })

    
@login_required(login_url='login')
def compte(request):
    """ Display Details of User
    """
    return render(request, 'accounts/compte.html', locals())