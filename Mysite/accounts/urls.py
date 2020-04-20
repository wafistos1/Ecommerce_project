from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Mettre ca temporairement ( )
urlpatterns = [
path('', views.home, name='home'),
path('accounts/login', views.login, name='login'),
path('accounts/user', views.register, name='register'),

]
