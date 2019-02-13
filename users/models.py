from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, crmv, name, password=None):
        if not email:
            raise ValueError('Os usuários devem ter um endereço de e-mail')

        user = self.model(
            email=self.normalize_email(email),
            crmv=crmv,
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, crmv, name, password):
        user = self.create_user(
            email,
            password=password,
            crmv=crmv,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField("E-mail", unique=True)
    crmv = models.CharField("CRMV", max_length=14, unique=True)
    name = models.CharField("nome", max_length=40)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['crmv', 'name', ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin