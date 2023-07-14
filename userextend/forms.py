from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.forms import TextInput, EmailInput


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                 'username'
                  ]
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume',
            'email': 'E-mail',
            'username': 'Username'
        }

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Te rog sa introduci prenumele'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Te rog sa introduci numele'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Te rog sa introduci adresa de e-mail'}),
           'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Te rog sa introduci un username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa introduci parola'})
        self.fields['password1'].label = 'Parola'
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa confirmi parola'})
        self.fields['password2'].label = 'Confirma parola'
        self.fields['password2'].help_text = None



class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa introduci username-ul'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa introduci parola'})
        self.fields['password'].label = 'Parola'


class PasswordChangeNewForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa introduci parola veche'})
        self.fields['old_password'].label = 'Parola veche'
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa introduci noua parola'})
        self.fields['new_password1'].label = 'Parola noua'
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Te rog sa repeti noua parola'})
        self.fields['new_password2'].label = 'Repeta noua parola'



