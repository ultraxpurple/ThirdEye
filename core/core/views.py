# core/core/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the ThirdEye Home Page!")
