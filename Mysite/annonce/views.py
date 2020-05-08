from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import annonceFrom, ImageForm, editAnnonceForm
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
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Image(annonce_images=annonceForm, image=image)
                    photo.save()

            print(annonceForm)
            messages.add_message(
                request, messages.SUCCESS, 'Annonce ajouter avec succès'
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


class annonceUpdateView(UpdateView):
    """Simple UpdateView to update a Annonce"""
    model = Annonce
    fields = ['title', 'price', 'description']
    template_name = 'annonce/update.html'   # ame template

    def get_object(self):
        obj = get_object_or_404(Annonce, pk=self.kwargs.get('pk'))
        return obj

    def get_success_url(self):
        return reverse_lazy('profile')

# def updateAnnonce(request, pk):
#     obj_annonce = get_object_or_404(Annonce, pk=pk)
#     print(obj_annonce.product)
#     print(request.POST)
#     if request.POST:
#         form = editAnnonceForm(request.POST, request.FILES, instance=obj_annonce)
#         if form.is_valid():
#             print('is valid')
#             form.save()
#             return redirect('profile')
#         else:
#             print(form)
#             print('is not valid')
#             form = editAnnonceForm(request.POST, request.FILES, instance=obj_annonce)
#             return render(request, 'annonce/update.html', {'form': form})
#     form = editAnnonceForm()
#     print('is no thing')
#     return render(request, 'annonce/update.html', {'form': form}) 
