from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from authentication.forms import RegisterForm, LoginForm

class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class Register(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')