from django.shortcuts import render
from product_manager.models import Product
# Create your views here.

def home(request):
    return render(request, "bootstrap-admin-template-free/home.html")

def login(request):
    return render(request, "bootstrap-admin-template-free/login.html")

def register(request):
    return render(request, "bootstrap-admin-template-free/register.html")

def listagem(request):
    products = Product.objects.all()
    return render(request, 'bootstrap-admin-template-free/listagem.html', {'products': products})