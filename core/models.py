from django.db import models
from authentication.models import User

class Address(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    number = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.street, self.number)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Haras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    proprietary = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    observation = models.TextField("Observações",null=True, blank=True)

    def __str__(self):
        return self.name

class Ancillary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    haras = models.ForeignKey(Haras, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)

class Animal(models.Model):

    TIPO_CHOICES = (
        ('GANHARAO', 'Ganharão'),
        ('DOADORA', 'Égua Doadora'),
        ('RECEPTORA', 'Égua Receptora')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    proprietary = models.ForeignKey(Client, on_delete=models.CASCADE)
    allocation = models.ForeignKey(Haras, on_delete=models.CASCADE)
    ancillary = models.ForeignKey(Ancillary, on_delete=models.CASCADE)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=25)

    def __str__(self):
        return "{}-{}".format(self.name, self.tipo)

class CicloEstral(models.Model):
    date = models.DateField()
    description = models.TextField()
    egua = models.ForeignKey(Animal, on_delete=models.CASCADE)