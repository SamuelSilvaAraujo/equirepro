from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import PasswordInput, TextInput

from authentication.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'crmv', 'name',]
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            'crmv': forms.TextInput(attrs={'placeholder': 'CRMV', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirme sua Senha'})