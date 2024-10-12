from django import forms
from .models import contactMessage

class contact_form(forms.ModelForm):
    class Meta:
        model = contactMessage
        fields = ['name', 'email', 'message', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'reason': forms.Select(attrs={'placeholder': 'Why are you getting in contact?'}),  
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }