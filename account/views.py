from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Account

def IndexPage(request):
    return render(request, 'homeapp/index.html')

def RegPage(request):
    return render(request, 'homeapp/register.html')

def SRegPage(request):
    return render(request, 'homeapp/Sregister.html')

def LoginPage(request):
    return render(request, 'homeapp/login.html')

def ContactPage(request):
    return render(request, 'homeapp/contact.html')

def ServicesPage(request):
    return render(request, 'homeapp/services.html')

