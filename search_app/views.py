import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from annonce.models import Annonce, Categorie, Comment
from datetime import datetime
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import AnnonceFilter
from .serializers import AnnonceSerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers

from django.template.loader import render_to_string

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
    print(f'request search {request}')
    if query:
        try:
            search_list = Annonce.objects.filter(
                Q(title__icontains=query) |
                Q(product__icontains=query) |
                Q(description__icontains=query)
                )
        except:
            message = ("Erreur de recherche")
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
        message = (f"Désole mais votre recherche '' {query} '' à générer aucune correspondance, essayez une autre recherche.")
    context = {
        'search_list': search_list,
        'message': message,
        'count_list': count,
        'categories': categories,
        'filter': f,
    }
    return render(request, 'search_app/search.html', context)


def filter_search(request):
    """ Display the search resultat with advanced filter """
    categories = request.GET.get('categories')
    type_annonce = request.GET.get('type_annonce')
    date_gt = request.GET.get('date_gt') 
    date = request.GET.get('date') 
    date_lt = request.GET.get('date_lt') 
    price = request.GET.get('price')
    price_gt = request.GET.get('price_gt') 
    price_lt = request.GET.get('price_lt')
    conditions = {}
    print(f'request: {request}')
    if categories or type_annonce or date_gt or date_lt or price or price_gt or price_lt or date:
        
        for filter_key, form_key in (
            ('categories', 'categories'), 
            ('type_annonce', 'type_annonce'), 
            ('price', 'price'),  
            ('price__gt', 'price_gt'),  
            ('price__lt', 'price_lt'),  
            ('created', 'date'),  
            ('created__lt', 'date_lt'),  
            ('created__gt', 'date_gt'),  
            ):
            value = request.GET.get(form_key, None)
            if value:
                conditions[filter_key] = value
                print(conditions)
    resultat_filter = Annonce.objects.filter(**conditions).order_by('-created')
    print(resultat_filter.count())
    context = {
        'resultat': resultat_filter,
        'count_list': resultat_filter.count(),
    }
    if request.is_ajax():
        print('Ajax is true')
        html = render_to_string(
            'search_app/filter.html',
            context, request=request
            )
        return JsonResponse({'form': html})
    # return render(request, 'search_app/search.html', context)
    return JsonResponse(context, safe=False)


def search_categorie(request, search):
    # search = search.lower()
    print(search)
    categorie = None
    try:
        categorie = Annonce.objects.filter(categories__name=search)
        count = categorie.count()
    except :
        print('toto')
        message = 'Aucun corespendances'
        categorie = {}
    print(categorie)
    
    context = {
        'categories': categorie,
        'count_list': count,

    }
    return render(request, 'search_app/search.html', context)