from django.http import HttpResponse
from django.shortcuts import render
from product_manager.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request, "bootstrap-admin-template-free/home.html")

def login(request):
    # Verificar se o usuário já está logado
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, "bootstrap-admin-template-free/login.html")
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        user = authenticate(username=name, password=password)
        
        if user:
            login_django(request, user)
            return redirect('/')
        else:
            return HttpResponse("Usuário ou senha inválidos")


def register(request):
    if request.method == "GET":
        return render(request, "bootstrap-admin-template-free/register.html")
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Verificar se o usuário já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "O email já está cadastrado.")
            return render(request, "bootstrap-admin-template-free/register.html")
        
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        return HttpResponse("Usuário criado com sucesso")

def logout(request):
    logout_django(request)
    return redirect('/login')

def listagem(request):
    products = Product.objects.all()
    return render(request, 'bootstrap-admin-template-free/listagem.html', {'products': products})