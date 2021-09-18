from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

def base(request: HttpRequest):
    return render(request, 'base.html')

def landing(request: HttpRequest):
    return render(request, 'landing.html')

def home(request: HttpRequest):
    return render(request, 'home.html')