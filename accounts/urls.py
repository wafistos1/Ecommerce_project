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
# Mettre ca temporairement ( )
urlpatterns = [

    # path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),

    # path('accounts/user', views.register, name='register'),
    # path('accounts/login', views.loginPage, name='login'),
    path('accounts/edit_profile', views.edit, name='edit'),
    path('accounts/compte', views.compte, name='profile'),
    path('accounts/list_annonces', views.annonce_list, name='list_annonces'),

# # reset password urls

# path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
# path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
# path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
# path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]
