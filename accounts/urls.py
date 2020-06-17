from django.urls import path
from django.conf.urls import handler404, handler500
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'accounts.views.my_custom_page_not_found_view'
handler400 = 'accounts.views.my_custom_bad_request_view'
handler500 = 'accounts.views.my_custom_error_view'
handler403 = 'accounts.views.my_custom_permission_denied_view'

urlpatterns = [

    path('accounts/edit_profile', views.edit, name='edit'),
    path('accounts/compte', views.compte, name='profile'),
    path('accounts/list_annonces', views.annonce_list, name='list_annonces'),
    path('accounts/mentions_legales', views.mention, name='mention'),

]
