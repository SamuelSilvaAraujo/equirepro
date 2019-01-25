from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    number = models.IntegerField()

class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

class Haras(models.Model):
    name = models.CharField(max_length=60)
    proprietary = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    observation = models.TextField()

class Ancillary(models.Model):
    haras = models.ForeignKey(Haras, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)

class Animal(models.Model):

    TIPO_CHOICES = (
        ('GANHARAO', 'Ganharão'),
        ('EGUADOADORA', 'Égua Doadora'),
        ('EGUARECEPTORA', 'Égua Receptora')
    )

    name = models.CharField(max_length=60)
    proprietary = models.ForeignKey(Client, on_delete=models.CASCADE)
    allocation = models.ForeignKey(Haras, on_delete=models.CASCADE)
    ancillary = models.ForeignKey(Ancillary, on_delete=models.CASCADE)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=25)

class CicloEstral(models.Model):
    date = models.DateField()
    description = models.TextField()
    egua = models.ForeignKey(Animal, on_delete=models.CASCADE)