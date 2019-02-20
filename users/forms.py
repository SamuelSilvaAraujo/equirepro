from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'crmv_numero', 'crmv_estado', ]
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            'crmv_numero': forms.TextInput(attrs={'placeholder': 'CRMV Numero', 'class': 'form-control'}),
            'crmv_estado': forms.Select(attrs={'class': 'select form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirme sua Senha'})