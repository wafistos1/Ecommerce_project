from django.shortcuts import render

# Create your views here.


def add_annonce(request):
    context = {}
    return render(request, "annonce/add.html", context)


def annonce_detail(request):
    context = {}
    return render(request, "annonce/detail.html", context)