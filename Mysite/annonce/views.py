from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import annonceFrom, categorieFrom

from .models import Annonce, Categorie

# Create your views here.


@login_required(login_url='account_login')
def add_annonce(request):
    print(request.POST)
    if request.method == "POST":
        a_form = annonceFrom(request.POST, request.FILES)
        if a_form.is_valid():
            print('Is valid')
            user = request.user
            annonce = a_form.save(commit=False)
            annonce.owner = user
            annonce.save()
            print(annonce)
            messages.add_message(
                request, messages.SUCCESS, 'annonce ajouter avec succès'
            )
            return redirect('home')
        else:
            print('Is not valid')
            a_form = annonceFrom()
    
    else:
        print('Is not valid')
        a_form = annonceFrom()
    
    a_form = annonceFrom()
    return render(request, 'annonce/add.html', {
        "a_form": a_form
    })


class annonceListView(ListView):
    model = Annonce
    context_object_name = 'lists'
    paginate_by = 4
    template_name = 'base.html'


class AnnonceDetailView(DetailView):
    model = Annonce
    context_object_name = 'details'
    template_name = 'annonce/detail.html'

