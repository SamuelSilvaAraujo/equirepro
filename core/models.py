from django.db import models
from users.models import User

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
    name = models.CharField("Nome", max_length=60)
    email = models.EmailField("E-mail", blank=True)
    phone = models.CharField("Telefone", max_length=30, blank=True)

    def __str__(self):
        return self.name

class Haras(models.Model):
    proprietary = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Proprietario")
    name = models.CharField("Nome", max_length=60)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Endereço")
    observation = models.TextField("Observações", null=True, blank=True)

    def __str__(self):
        return self.name

class Ancillary(models.Model):
    haras = models.ForeignKey(Haras, on_delete=models.CASCADE, verbose_name="Haras")
    name = models.CharField("Nome", max_length=60)
    phone = models.CharField("Telefone", max_length=30)

    def __str__(self):
        return self.name

class Animal(models.Model):

    TYPE_CHOICES = (
        ('garanhao', 'Garanhão'),
        ('doadora', 'Égua Doadora'),
        ('receptora', 'Égua Receptora')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=60)
    proprietary = models.ForeignKey(Client, verbose_name="Proprietário", on_delete=models.CASCADE)
    allocation = models.ForeignKey(Haras, verbose_name="Locação", on_delete=models.CASCADE)
    ancillary = models.ForeignKey(Ancillary, verbose_name="Auxiliar", on_delete=models.CASCADE)
    type = models.CharField("Tipo", choices=TYPE_CHOICES, max_length=25)

    def __str__(self):
        return "{}-{}".format(self.name, self.type)

class CicloEstral(models.Model):
    date = models.DateField()
    description = models.TextField()
    egua = models.ForeignKey(Animal, on_delete=models.CASCADE)

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=50)
    price = models.FloatField("Preço")