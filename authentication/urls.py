from django.urls import path

from authentication.views import Login, Register

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register")
]