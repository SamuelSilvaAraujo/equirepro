from django import forms
from core.models import Ancillary, Animal, Client, Haras, Service

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'proprietary', 'allocation', 'ancillary', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proprietary': forms.Select(attrs={'class': "selectP form-control"}),
            'allocation': forms.Select(attrs={'class': 'selectL form-control'}),
            'ancillary': forms.Select(attrs={'class': 'selectA form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class AuxiliarForm(forms.ModelForm):
    class Meta:
        model = Ancillary
        fields = ['name', 'phone', 'haras', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            'haras': forms.Select(attrs={'class': 'select form-control'}),
        }

class HarasForm(forms.ModelForm):
    class Meta:
        model = Haras
        fields = ['name', 'proprietary', 'address', 'observation', ]

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }