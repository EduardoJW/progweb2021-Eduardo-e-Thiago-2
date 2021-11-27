from django.urls import path
from CardMakerApp import views

app_name = 'CardMakerApp'

urlpatterns = [

    path('lista/', views.listCards.as_view(), name = 'lista-cartas'),
    path('', views.home, name = 'home-app'),
    path('cria/', views.createCard.as_view(), name = 'cria-carta'),
    path('login/', views.login, name = 'login-app'),
    path('registro/', views.register, name = 'registro-app'),

    ]