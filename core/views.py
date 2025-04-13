from django.core.mail import send_mail
from django.shortcuts import render, redirect
import os
from django.contrib import messages
from .forms import contact_form
from .models import HomePageContent
from datetime import datetime


def home(request):
    content = HomePageContent.objects.all()
    return render(request, 'core/home.html', {'content': content})

def education(request):
    return render(request, 'core/education.html')

def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)

        # Honeypot field validation (renamed to 'contact_website')
        if request.POST.get('contact_website'):
            messages.error(request, "Bot detected. Submission blocked.")
            return redirect('contact')

        # Check for fast form submission (timestamp field)
        timestamp_str = request.POST.get('timestamp')
        if timestamp_str:
            try:
                form_time = datetime.fromisoformat(timestamp_str)
                if (datetime.now() - form_time).total_seconds() < 3:
                    messages.error(request, "Submission too fast. Bot suspected.")
                    return redirect('contact')
            except ValueError:
                pass  # Invalid timestamp, skip this check

        # Extra keyword filtering (e.g., 'phoff')
        name = request.POST.get('name', '').lower()
        message_content = request.POST.get('message', '').lower()
        if 'phoff' in name or 'phoff' in message_content:
            messages.error(request, "Spam detected in content.")
            return redirect('contact')

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

            messages.success(request, "I've received your message!")
            return redirect('contact')
    else:
        form = contact_form()

    timestamp = datetime.now().isoformat()
    return render(request, 'core/contact.html', {'form': form, 'timestamp': timestamp})
