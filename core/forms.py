from django import forms
from core.models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'proprietary', 'allocation', 'ancillary',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proprietary': forms.Select(attrs={'class': "select form-control"}),
            'allocation': forms.Select(attrs={'class': 'select form-control'}),
            'ancillary': forms.Select(attrs={'class': 'select form-control'}),
        }