from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.contrib.auth.decorators import login_required
from .forms import annonceFrom, ImageForm, editAnnonceForm, commentForm, MpUserForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Annonce, Categorie, Image, Comment, MpUser
from accounts.models import Profile


def home(request):
    """View of my home page whith list  all annonces of all user
    return: all annonces , all categories, all images
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
    """
    View to add annonces
    """
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=4)

    # 'extra' means the number of photos that you can upload   ^

    print(request.POST)
    if request.method == "POST":
        a_form = annonceFrom(request.POST)
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=Image.objects.none()
            )
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
    """
        Class to display all annonces 
    """
    model = Annonce
    context_object_name = 'lists'
    paginate_by = 12
    template_name = 'annonce/home.html'


class AnnonceDetailView(DetailView):
    """
        Class to display a details of annonces 
    """
    model = Annonce
    context_object_name = 'details'
    template_name = 'annonce/detail.html'


def annonceDetaiView(request, pk):
    """
        Class to display all annonces
    """
    details = get_object_or_404(Annonce, pk=pk)
    comment = Comment.objects.filter(
        for_post=details,
        reply=None).order_by('-create_content')

    is_favorite = False

    if details.favorite.filter(id=request.user.id).exists():
        is_favorite = True
        # print('favorite is now true')
    else:
        print('favorite is now False')

    if request.method == "POST":

        print(request.POST)

        c_form = commentForm(request.POST or None)

        if c_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment-id')
            comment_qs = None  # reply is null
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)  
                # set reply as reply_id

            comment_use = Comment(
                commented_by=request.user,
                for_post=details,
                content=content,
                reply=comment_qs
                )
            comment_use.save()

            # return HttpResponseRedirect(details.get_absolute_url())
    else:
        c_form = commentForm()
    print(f'send {is_favorite}')
    context = {
        'is_favorite': is_favorite,
        'details': details,
        'comment': comment,
        'commentform': c_form,
        }
    if request.is_ajax():
        print('Ajax is true')
        html = render_to_string(
            'annonce/comment.html',
            context, request=request
            )
        return JsonResponse({'form': html})
    return render(request, 'annonce/detail.html', context)


def annonce_favorite_list(request):
    user = request.user
    favorite_list = user.favorite.all()

    context = {
        'favorite_list': favorite_list
    }
    return render(request, 'annonce/favorite.html', context)


class AnnonceDeletelView(LoginRequiredMixin, DeleteView):
    model = Annonce
    context_object_name = 'obj_delte'
    template_name = 'annonce/delete.html'
    success_url = reverse_lazy('profile')


def updateAnnonce(request, pk=None):
    ImageFormSet = modelformset_factory(
        Image,
        form=ImageForm,
        extra=4,
        max_num=4
        )
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


def favorite(request, pk):
    favorite_annonce = get_object_or_404(Annonce, pk=pk)
    # # Verifier si l'object existe dans la BD 
    # print('je suis dans favorite views')
    if favorite_annonce.favorite.filter(pk=request.user.id).exists():
        # print('je suis dans favorite qui vaux True')
        favorite_annonce.favorite.remove(request.user)
    else:
        # print('je suis dans favorite qui vaux False')
        favorite_annonce.favorite.add(request.user)

    return HttpResponseRedirect(favorite_annonce.get_absolute_url())


def message_mp(request, user_pk):
    mp_form = MpUserForm(request.POST)
    print('request.is valid')
    print(request.user.pk)
    print(user_pk)
    if mp_form.is_valid():
        f = mp_form.save(commit=False)
        f.sender = Profile.objects.get(pk=request.user.pk)
        f.reciever = Profile.objects.get(pk=user_pk)
        # message = MpUser(sender=mp_form.sender, receiver=mp_form.reciever, message=mp_form.message)
        mp_form.save()
        messages.add_message(request, SUCCESS, ('Message envoyee avec succès '))
        return redirect('home')
    else:
        mp_form = MpUserForm()
        messages.add_message(
                request, ERROR,
                (" Une erreur c'est produite ")
                )
    context = {
        'mp_form': mp_form,
        'messages': messages,
    }
    print(context)
    return render(request, 'annonce/message.html', context)


def message_list(request):
    messages = MpUser.objects.filter(reciever=request.user.pk).order_by('-created_at')

    context = {
        'message_list': messages,
    }

    return render(request, 'annonce/message_list.html', context)