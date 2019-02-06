from django.urls import path, include

from core.views import *

urlpatterns = [
    path('agenda/', Agenda.as_view(), name="agenda"),
    path('animais/', include([
        path('garanhao/list/', Garanhoes.as_view(), name="garanhao_list"),
        path('doadora/list/', Doadoras.as_view(), name="doadora_list"),
        path('receptora/list/', Receptoras.as_view(), name="receptora_list"),
        path('<str:type>/novo/', NewAnimal.as_view(), name="new_animal"),
    ])),
    path('cliente/list/', Clientes.as_view(), name="client_list"),
    path('haras/list/', HarasList.as_view(), name="haras_list"),
    path('auxiliar/list/', Auxiliares.as_view(), name="auxiliar_list"),
]