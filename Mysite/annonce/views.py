from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import annonceFrom, ImageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Annonce, Categorie, Image

# Create your views here.


def home(request):
    """
    """
    categorie = Categorie.objects.all()
    annonce = Annonce.objects.all().order_by('-created')
    images = Image.objects.all()
    # todo: ajouter la paginations

    page = request.GET.get('page', 1)
    paginator = Paginator(annonce, 9)
    try:
        annonce = paginator.page(page)
    except PageNotAnInteger:
        annonce = paginator.page(1)
    except EmptyPage:
        annonce = paginator.page(paginator.num_pages)
    context = {'categories': categorie, 'annonces': annonce, 'image': images}
    return render(request, 'base.html', context)

@login_required(login_url='account_login')
def add_annonce(request):

    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=4)

    # 'extra' means the number of photos that you can upload   ^

    print(request.POST)
    if request.method == "POST":
        a_form = annonceFrom(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
        if a_form.is_valid() and formset.is_valid():
            print('Is valid')
            user = request.user
            annonceForm = a_form.save(commit=False)
            annonceForm.owner = user
            annonceForm.save()
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Image(annonce_images=annonceForm, image=image)
                    photo.save()

            print(annonceForm)
            messages.add_message(
                request, messages.SUCCESS, 'annonce ajouter avec succès'
            )
            return redirect('home')
        else:
            print('Is not valid')
            print(annonceForm.errors, formset.errors)
            a_form = annonceFrom()
    
    else:
        print('Is not valid')
        a_form = annonceFrom()
        formset = ImageFormSet(queryset=Image.objects.none())
    
    a_form = annonceFrom()
    formset = ImageFormSet(queryset=Image.objects.none())

    return render(request, 'annonce/add.html', {
        "a_form": a_form,
        "formset": formset,
        })


class annonceListView(ListView):
    model = Annonce
    context_object_name = 'lists'
    paginate_by = 12
    template_name = 'annonce/home.html'


class AnnonceDetailView(DetailView):
    model = Annonce
    context_object_name = 'details'
    template_name = 'annonce/detail.html'

# TODO: ADD remove annonce view
