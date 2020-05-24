from django.shortcuts import render
from annonce.models import Annonce, Categorie, Comment
from datetime import datetime
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import AnnonceFilter

# Create your views here.
# Global variable
query = None


def search(request):
    global query
    search_list = Annonce.objects.all()
    categories =  Categorie.objects.all()
    query = request.GET.get('q')
    f = AnnonceFilter(request.GET, queryset=Annonce.objects.all())
    print(query)
    if query:
        try:
            search_list = Annonce.objects.filter(
                Q(title__icontains=query) |
                Q(product__icontains=query) |
                Q(description__icontains=query)
                )

        except:
            message = ("Essayez un autre produit.")
            produit = query
            return render(request, 'search_app/search.html', {'message': message, })
    paginator = Paginator(search_list, 9)
    page = request.GET.get('page')
    message = False
    count = search_list.count()
    if search_list:
        try:
            search_list = paginator.page(page)
        except PageNotAnInteger:
            search_list = paginator.page(1)
        except EmptyPage:
            search_list = paginator.page(paginator.num_pages)
    else:
        query = query.upper() 
        message = (f"Désole mais votre recherche '' {query} '' à générer aucune correspondance, essayez un autre produit.")
    context = {
        'search_list': search_list,
        'message': message,
        'count_list': count,
        'categories': categories,
        'filter': f,
    }
    return render(request, 'search_app/search.html', context)