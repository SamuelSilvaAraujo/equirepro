from django.urls import path

from core.views import *

urlpatterns = [
    path('agenda/', Agenda.as_view(), name="agenda"),
    path('animal/list/', Animais.as_view(), name="animal_list"),
    path('animal/novo/', NovoAnimal.as_view(), name="animal_novo"),
    path('cliente/list/', Clientes.as_view(), name="client_list"),
    path('haras/list/', HarasList.as_view(), name="haras_list"),
    path('auxiliar/list/', Auxiliares.as_view(), name="auxiliar_list"),
]