from django.utils import timezone
from django.db import models
from users.models import User

class Address(models.Model):
    STATES_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

    state = models.CharField("Estado", max_length=2, choices=STATES_CHOICES)
    city = models.CharField("Cidade", max_length=20)
    district = models.CharField("Bairro", max_length=20)
    street = models.CharField("Rua", max_length=20)
    number = models.IntegerField("Numero")

    def __str__(self):
        return "{}-{}".format(self.city, self.state)

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
    allocation = models.ForeignKey(Haras, verbose_name="Localização", on_delete=models.CASCADE)
    ancillary = models.ForeignKey(Ancillary, verbose_name="Auxiliar", on_delete=models.CASCADE)
    type = models.CharField("Tipo", choices=TYPE_CHOICES, max_length=25)

    def __str__(self):
        return "{}-{}".format(self.name, self.type)

class CicloEstral(models.Model):
    date = models.DateField()
    description = models.TextField()
    egua = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return "{}/{}".format(self.date, self.egua.name)

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=50)
    price = models.FloatField("Preço")

    def __str__(self):
        return self.name

class ServiceRealized(models.Model):
    status_choices = [
        ('open', 'Aberta'),
        ('paid', 'Paga'),
        ('cancelled', 'Cancelada'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=9, choices=status_choices, default='open')
    amount = models.FloatField("Valor total", default=0)

    def __str__(self):
        return self.client.name

class ServiceRealizedLine(models.Model):
    service_realized = models.ForeignKey(ServiceRealized, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.service.name, self.animal.name)