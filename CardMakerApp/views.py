from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'CardMakerApp/home.html')

def login(request):
    return render(request, 'CardMakerApp/login.html')

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


