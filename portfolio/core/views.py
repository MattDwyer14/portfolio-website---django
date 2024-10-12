from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import contact_form
from .models import HomePageContent

def home(request):
    content = HomePageContent.objects.all()
    return render(request, 'core/home.html', {'content': content})

def education(request):
    return render(request, 'core/education.html')

def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'I\'ve recieved your message!')
            return redirect('contact')
    else:
        form = contact_form()

    return render(request, 'core/contact.html', {'form': form})
