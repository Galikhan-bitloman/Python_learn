from django.shortcuts import render

# Create your views here.

def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'index.html')