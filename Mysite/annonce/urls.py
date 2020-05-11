from django.urls import path
from annonce import views
from annonce.views import annonceListView, updateAnnonce, AnnonceDeletelView, add_annonce, annonceDetaiView

urlpatterns = [
    path('', views.home, name='home'),
    path('annonce/add', views.add_annonce, name='add_annonce'),
    path('annonce/detail/<uuid:pk>', views.annonceDetaiView, name='annonce_detail'),
    # path('annonce/detail/<uuid:pk>', AnnonceDetailView.as_view(), name='annonce_detail'),
    path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    path('annonce/delete/<uuid:pk>', AnnonceDeletelView.as_view(), name='annonce_delete'),
    path('annonce/update/<uuid:pk>', views.updateAnnonce, name='annonce_update'),
    ]