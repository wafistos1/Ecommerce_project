from django.shortcuts import render, redirect, HttpResponseRedirect
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import annonceFrom, ImageForm, editAnnonceForm, commentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Annonce, Categorie, Image, Comment

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

    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4)

    # 'extra' means the number of photos that you can upload   ^

    print(request.POST)
    if request.method == "POST":
        a_form = annonceFrom(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        print(request.POST)
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


def annonceDetaiView(request, pk):
    details = get_object_or_404(Annonce, pk=pk)
    comment = Comment.objects.filter(for_post=details).order_by('-create_content')

    if request.method == "POST":
        c_form = commentForm(request.POST or None)
        if c_form.is_valid():
            content = request.POST.get('content')
            comment_use = Comment(commented_by=request.user,  for_post=details, content=content)
            comment_use.save()
            return HttpResponseRedirect(details.get_absolute_url())
    else:
        c_form = commentForm() 

    context = {
        'details': details,
        'comment': comment,
        'commentform': c_form,
        }

    return render(request, 'annonce/detail.html', context)


class AnnonceDeletelView(DeleteView):
    model = Annonce
    context_object_name = 'obj_delte'
    template_name = 'annonce/delete.html'
    success_url = reverse_lazy('profile')


# class annonceUpdateView(UpdateView):
    # """Simple UpdateView to update a Annonce"""
    # model = Annonce
    
    # fields = ['title', 'price', 'description']
    # template_name = 'annonce/update.html'   # ame template

    # def get_object(self):
    #     obj = get_object_or_404(Annonce, pk=self.kwargs.get('pk'))
    #     return obj

    # def get_success_url(self):
    #     return reverse_lazy('profile')
    
    # def get_context_data(self, **kwargs):
    #     context = super(annonceUpdateView, self).get_context_data(**kwargs)
    #     owner = self.request.user

    #     if not self.request.POST:
    #         context['annonceFrom'] = annonceFrom()
    #         context['ImageForm'] = ImageForm()
    #         return context

    #     def post(self, request, *args, **kwargs):
    #         self.object = self.get_object()
    #         user = self.request.user
    #         context['annonceFrom'] = annonceFrom(self.request.POST, instance=self.object)
    #         context['ImageForm'] = ImageForm(self.request.POST, self.request.FILES)
    #         return super(annonceUpdateView, self).post(request, *args, **kwargs)

    #     def form_valid(self, form):
    #         context = self.get_context_data(form=annonceFrom)
    #         user = self.request.user

    #         annonce = context['annonceFrom'].save(commit=False)
    #         image = context['ImageForm']
    #         annonce = context['annonceFrom']
    #         annonce.owner = user
    #         annonce.save()
    #         return super(annonceUpdateView, self).form_valid(form)

def updateAnnonce(request, pk=None):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4, max_num=4)
    obj_annonce = get_object_or_404(Annonce, pk=pk)
    if request.POST:
        form = annonceFrom(request.POST or None, instance=obj_annonce)
        formset = ImageFormSet(request.POST or None, request.FILES or None)     
        if form.is_valid() and formset.is_valid():
            print('is valid')
            form.save()
            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                try:    
                    image = form['image']
                    photo = Image(annonce_images=obj_annonce, image=image)
                    photo.save()
                except:
                    print('Forme image non valide')
                    
            return redirect('profile')
        else:
            print('is not valid')
            print(form.errors)
            form = editAnnonceForm()
            return render(request, 'annonce/update.html', {'form': form})
    form = editAnnonceForm(instance=obj_annonce)
    formset = ImageFormSet(queryset=Image.objects.filter(annonce_images=obj_annonce))
    print('is no thing')
    return render(request, 'annonce/update.html', {'form': form, 'formset': formset}) 


