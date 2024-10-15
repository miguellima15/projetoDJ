
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def my_view(request):
    return HttpResponse("Uma teste string de resposta")

def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")

def root_view(request):
    return HttpResponse("Estamos na Raiz 2. Porta 8000")
def contexto(request):
    return render(request,'contexto.html')
