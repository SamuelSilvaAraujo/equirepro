from django import forms
from django.forms import inlineformset_factory
from core.models import *

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'proprietary', 'allocation', 'ancillary', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':"Nome do animal", 'class': 'form-control'}),
            'proprietary': forms.Select(attrs={'class': "selectP form-control"}),
            'allocation': forms.Select(attrs={'class': 'selectL form-control'}),
            'ancillary': forms.Select(attrs={'class': 'selectA form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Fulano Silva'}),
            'phone': forms.TextInput(attrs={'class': "form-control", 'data-mask': '(99) 99999-9999', 'placeholder': 'Ex.: (99) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: fulano@gmail.com'}),
        }

class AncillaryForm(forms.ModelForm):
    class Meta:
        model = Ancillary
        fields = ['name', 'phone', 'haras', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Fulano Silva'}),
            'phone': forms.TextInput(attrs={'class': "form-control", 'data-mask': '(99) 99999-9999', 'placeholder': 'Ex.: (99) 99999-9999'}),
            'haras': forms.Select(attrs={'class': 'selectH form-control'}),
        }

class HarasForm(forms.ModelForm):
    class Meta:
        model = Haras
        fields = ['name', 'proprietary', 'observation', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Haras Esperança'}),
            'proprietary': forms.Select(attrs={'class': "selectP form-control"}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações sobre o haras'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }

class AddresForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Rua 15 de outubro'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: N° 232'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Centro'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Arapiraca'}),
            'state': forms.Select(attrs={'class': 'selectE form-control'}),
        }

class ServiceRealizedForm(forms.ModelForm):
    class Meta:
        model = ServiceRealized
        fields = ['client' ]
        widgets = {
            'client': forms.Select(attrs={'class': 'selectC form-control'}),
        }

class ServiceRealizedLineForm(forms.ModelForm):
    class Meta:
        model = ServiceRealizedLine
        fields = ['service', 'animal', ]
        widgets = {
            'service': forms.Select(attrs={'class': 'selectS form-control'}),
            'animal': forms.Select(attrs={'class': 'selectA form-control'}),
        }

ServiceRealizedLineFormset = inlineformset_factory(ServiceRealized, ServiceRealizedLine, form=ServiceRealizedLineForm, extra=1)


class CicloEstralForm(forms.ModelForm):
    class Meta:
        model = CicloEstral
        fields = ['date', 'description', ]
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }