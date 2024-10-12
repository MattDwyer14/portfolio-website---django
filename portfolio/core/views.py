#core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def education(request):
    return render(request, 'core/education.html')

def contact(request):
    return render(request, 'core/contact.html')
