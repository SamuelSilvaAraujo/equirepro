from django import forms
from core.models import Animal, Client

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'proprietary', 'allocation', 'ancillary', 'type', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proprietary': forms.Select(attrs={'class': "select2_demo_1 form-control"}),
            'allocation': forms.Select(attrs={'class': 'select2_demo_1 form-control'}),
            'ancillary': forms.Select(attrs={'class': 'select2_demo_1 form-control'}),
            'type': forms.Select(attrs={'class': 'select2_demo_1 form-control'}),
        }