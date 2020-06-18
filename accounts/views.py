from sentry_sdk import capture_message
from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import editform
from annonce.models import Annonce
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# # Create your views here.

@login_required(login_url='login')
def edit(request):
    """
    """
    if request.POST:
        form = editform(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()   
            capture_message(f"{request.user.username} a update son profile", level="error")
            return redirect('list_annonces')
        else:
            return render(request, 'edit_profile.html', {'form': form})
    form = editform(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required(login_url='login')
def compte(request):
    """
    """
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
        'form': form,
        }
    return render(request, 'accounts/compte.html', context)


@login_required(login_url='login')
def annonce_list(request):
    """fonction to dispaly list of all annonces

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [object with number of annonce and list of all annonces]
    """
    annonces = Annonce.objects.filter(owner=request.user)
    num_annonce = annonces.count()
    context = {
        'num_annonce': num_annonce,
        'annonces': annonces,
        }
    return render(request, 'accounts/annonce_list.html', context)


def mention(request):
    """Mentions legales
    """
    return render(request, 'mentions.html')


def my_custom_bad_request_view(request, exception):
    capture_message(f"{request.user.username} Page not found! error404", level="error")
    return render(request, 'accounts/404.html')


def my_custom_page_not_found_view(request, exception):
    capture_message(f"{request.user.username} Page not found! error404", level="error")
    return render(request, 'accounts/404.html')


def my_custom_error_view(request):
    capture_message(f"{request.user.username} Page not found! error500", level="error")
    return render(request, 'accounts/500.html')

def my_custom_permission_denied_view(request, exception):
    capture_message(f"{request.user.username} Page not found! error404", level="error")
    return render(request, 'accounts/404.html')