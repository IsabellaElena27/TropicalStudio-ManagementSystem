from django import forms
from django.forms import TextInput, EmailInput

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name',
                  'email', 'description']
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume',
            'email': 'E-mail',
            'description': 'Functie',
        }
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Te rog sa introduci prenumele', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Te rog sa introduci numele', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Te rog sa introduci adresa de e-mail', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Te rog sa introduci functia', 'class': 'form-control'})
        }

    def clean(self):  # in cadrul acestei metode clean veti putea adauga validari pentru formualar
        cleaned_data = self.cleaned_data  # stocam un dictionar cu toate valorile completate de utilizator in formular
        get_email = cleaned_data[
            'email']  # cleaned_data.get('email') -> accesam valoarea cheii email din dictionar-> valoarea introdusa de utilizator
        check_emails = Employee.objects.filter(
            email=get_email)  # cautam in tabela toti angajatii care au adresa de email = cea introdusa de utilizator
        if check_emails:  # daca exista un angajat cu adresa de email, generaram eroare
            msg = 'Acest email exista in baza de date'
            self._errors['email'] = self.error_class([msg])


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name',
                  'email', 'description']
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume',
            'email': 'E-mail',
            'description': 'Functie',
        }
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Te rog sa introduci prenumele', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Te rog sa introduci numele', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Te rog sa introduci adresa de e-mail', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Te rog sa introduci functia', 'class': 'form-control'})
        }
