from django.core.mail import send_mail
from django.shortcuts import render, redirect
import os
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
            contact_message = form.save()

            # Send email
            subject = f"Web Message from {contact_message.name}"
            message = f"""
Email: {contact_message.email}
Reason: {contact_message.reason}
Message: {contact_message.message}

{contact_message.name}
            """
            from_email = os.getenv('EMAIL_HOST_USER')
            recipient_list = os.getenv('EMAIL_RECIPIENT')

            send_mail(subject, message, from_email, [recipient_list])

            messages.success(request, 'I\'ve recieved your message!')
            return redirect('contact')
    else:
        form = contact_form()

    return render(request, 'core/contact.html', {'form': form})
