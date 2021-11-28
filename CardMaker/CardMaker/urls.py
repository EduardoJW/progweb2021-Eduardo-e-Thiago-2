"""AloMundo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.base import reverse_lazy
from CardMakerApp import views
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'homepage'),
    path('register/', views.register, name = 'registerOLD'),
    path('login/', views.login, name = 'loginOLD'),
    path('createCard/', views.createCard, name = 'createCard'),
    path('CardMakerApp/', include('CardMakerApp.urls') ),
    path('accounts/', views.homeSec, name='sec-home' ),
    path('accounts/register/', views.register, name = 'register'),
    path('accounts/login/', LoginView.as_view(template_name = 'registro/login.html'), name = 'login'),
    path('accounts/profile/', views.userProfile, name = 'profile'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name = 'logout'),
    path('accounts/passwordChange/',
     PasswordChangeView.as_view(template_name = 'registro/passwordChange.html', success_url = reverse_lazy('passwordChangeDone')), 
     name = 'passwordChange'),
     path('accounts/passwordChangeDone', PasswordChangeDoneView.as_view(template_name = 'registro/passwordChangeDone.html'), name='passwordChangeDone'),

]
