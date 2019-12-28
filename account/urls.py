from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('register', views.RegPage, name='register'),
    path('Sregister', views.SRegPage, name='Sregister'),
    path('login', views.LoginPage, name='login'),
    path('contact', views.ContactPage, name='contact'),
    path('services', views.ServicesPage, name='services'),
]