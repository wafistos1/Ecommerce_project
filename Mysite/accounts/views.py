from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import editform
from annonce.models import Annonce
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    form = editform(instance=request.user) 
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required(login_url='login')
def compte(request):
    annonce = Annonce.objects.filter(owner=request.user)
    num_annonce = annonce.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(annonce, 9)
    try:
        annonce = paginator.page(page)
    except PageNotAnInteger:
        annonce = paginator.page(1)
    except EmptyPage:
        annonce = paginator.page(paginator.num_pages)

    if request.POST:
        form = editform(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = editform(request.POST, request.FILES, instance=request.user)
            return render(request, 'accounts/compte.html', {'form': form})
    form = editform(instance=request.user)
    context = {
        'annonces': annonce,
        'form': form,
        'num_annonce': num_annonce
        }
    return render(request, 'accounts/compte.html', context)
