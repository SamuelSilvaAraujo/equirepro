from django.urls import path

from authentication.views import Login, Register

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
]