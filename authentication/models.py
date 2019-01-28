from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, crmv, name, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, crmv=crmv, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, crmv, name, password=None, **extra_fields):
        if password is None:
            password = User.objects.make_random_password()
        return self._create_user(email, crmv, name, password)

    def create_superuser(self, email, crmv, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, crmv, name, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField("E-mail", unique=True)
    crmv = models.CharField("CRMV", max_length=14, unique=True)
    name = models.CharField("nome",max_length=40)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['crmv', 'name', ]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True