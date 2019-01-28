from django import forms
from core.models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'proprietary', 'allocation', 'ancillary', 'tipo', ]