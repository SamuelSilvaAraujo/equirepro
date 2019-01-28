from django.contrib.auth.forms import UserCreationForm
from authentication.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'crmv', 'name']