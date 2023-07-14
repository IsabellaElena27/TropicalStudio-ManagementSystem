from django import forms
from django.forms import TextInput, EmailInput

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'full_name', 'email',
            'phone_number', 'message'
        ]
        labels = {
            'full_name': 'Nume si prenume',
            'email': 'E-mail',
            'phone_number': 'Numar de telefon',
            'message': 'Mesaj'
        }
        widgets = {
            'full_name': TextInput(attrs={'placeholder': 'Te rog sa introduci numele si prenumele', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Te rog sa introduci numarul de telefon', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Te rog sa introduci numarul de telefon', 'class': 'form-control'}),
            'message': TextInput(attrs={'placeholder': 'Te rog sa introduci mesajul', 'class': 'form-control'})
        }
