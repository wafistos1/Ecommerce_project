from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import editform
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# # Create your views here.

def edit(request):
    if request.POST:
        form = editform(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = editform(request.POST, request.FILES, instance=request.user)
            return render(request, 'edit_profile.html', {'form': form})
    form = editform()  
    
    return render(request, 'accounts/edit_profile.html', {'form': form})
# def login(request):
#     return render(request, 'accounts/login.html')

# def register(request):
#     print(request.POST)
#     if request.method == "POST":
#         user_form = UserRegisterForm(request.POST)
#         adresse_form = adresseForm(request.POST)
#         profile_form = profileForm(request.POST, request.FILES)
#         if user_form.is_valid() and adresse_form.is_valid() and profile_form.is_valid():
#             print('Is valid')
#             user = user_form.save()
#             adresse = adresse_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.adresse = adresse
#             profile.save()
#             messages.add_message(
#                 request, messages.SUCCESS, 'Profile inscrit avec succès veuillez vous connectez'
#                 )
#             return redirect('home')
#     else:
#         print('Is not valid')

#         user_form = UserRegisterForm()
#         adresse_form = adresseForm()
#         profile_form = profileForm()
    

#     return render(request, 'accounts/user.html', {
#         'user_form': user_form, 
#         'adresse_form': adresse_form, 
#         "profile_form": profile_form
#         })


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, "Username Or password is incorrect")
            
            
#     context = {}
#     return render(request, 'accounts/login.html', locals())  

# def logoutPage(request):
#     auth_logout(request)
#     return redirect('login')
    
@login_required(login_url='login')
def compte(request):
    """ Display Details of User
    """
    return render(request, 'accounts/compte.html', locals())