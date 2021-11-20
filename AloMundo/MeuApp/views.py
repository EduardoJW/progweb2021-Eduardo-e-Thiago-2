from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'MeuApp/home.html')

def segundoView(request):
    return render(request, 'MeuApp/segundaPagina.html')
