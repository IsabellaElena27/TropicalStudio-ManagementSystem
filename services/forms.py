from django import forms
from django.forms import TextInput, Select

from employee.models import Employee
from services.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name_of_service', 'price', 'employee'
        ]
        labels = {
            'name_of_service': 'Serviciu',
            'price': 'Pret',
            'employee': 'Angajat'
        }
        widgets = {
            'name_of_service': TextInput(attrs={'placeholder': 'Denumirea serviciului', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Pret', 'class': 'form-control'}),
            'employee': Select(attrs={'class': 'form-control'})
        }


class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name_of_service', 'price', 'employee'
        ]
        labels = {
            'name_of_service': 'Serviciu',
            'price': 'Pret',
            'employee': 'Angajat'
        }
        widgets = {
            'name_of_service': TextInput(attrs={'placeholder': 'Denumirea serviciului', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Pret', 'class': 'form-control'}),
            'employee': Select(attrs={'class': 'form-control'})
        }


class SelectareDataOraForm(forms.Form):
    data_ora = forms.DateTimeField(label='Data și ora programării', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

