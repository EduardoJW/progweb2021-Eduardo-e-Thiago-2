from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from CardMakerApp.forms import CardModel2Form
from django.views.generic.base import View
from CardMakerApp.models import Carta
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

#Home Page
def home(request):
    return render(request, 'CardMakerApp/home.html')

#User login page
def login(request):
    return render(request, 'CardMakerApp/login.html')

#User register page
def register(request):
    #return render(request, 'CardMakerApp/login.html')
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    contexto = {'formulario': formulario, }
    return render(request, 'CardMakerApp/register.html', contexto)

#Lista todas as cartas
class listCards(View):
    def get(self, request, *args, **kwards):
        #Buscar todas as cartas do banco de dados
        objCartas = Carta.objects.all()
        #Enviar cartas para o template
        context = {'cartas' : objCartas, }
        return render(request, 'CardMakerApp/listCards.html', context)
        
#Card creator view
class createCard(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': CardModel2Form, }
        return render(request, "CardMakerApp/createCard.html", context)

    def post(self, request, *args, **kwargs):
        formulario = CardModel2Form(request.POST)
        if formulario.is_valid():
            carta = formulario.save()
            carta.save()
            return HttpResponseRedirect(reverse_lazy("CardMakerApp:lista-cartas"))
        pass


#Card Update View
class updateCard(View):
    #busca os dados de uma carta e exibe como um formulario
    def get(self, request, pk, *args, **kwargs):
        carta = Carta.objects.get(pk=pk)
        formulario = CardModel2Form(instance=carta)
        context = {'formulario': formulario, }
        return render(request, 'CardMakerApp/updateCard.html', context)

    #recebe os dados de uma carta e atualiza no bando de dados
    def post(self, request, pk, *args, **kwargs):
        carta = get_object_or_404(Carta, pk=pk)
        formulario = CardModel2Form(request.POST, instance=carta)
        if formulario.is_valid():
            carta = formulario.save()
            carta.save()
            return HttpResponseRedirect(reverse_lazy("CardMakerApp:lista-cartas"))
        else:
            context = {'formulario': formulario, }
            return render(request, 'CardMakerApp/updateCard.html', context)

#Remove uma carta
class deleteCard(View):
    
    def get(self, request, pk, *args, **kwargs):
        carta = Carta.objects.get(pk=pk)
        context = {'carta': carta}
        return render(request, 'CardMakerApp/deleteCard.html', context)

    def post(self, request, pk, *args, **kwargs):
        carta = Carta.objects.get(pk=pk)
        carta.delete()
        return HttpResponseRedirect(reverse_lazy("CardMakerApp:lista-cartas"))


