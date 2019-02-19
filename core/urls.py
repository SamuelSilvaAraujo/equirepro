from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('agenda/', AgendaView.as_view(), name="agenda"),
    path('garanhoes/', GaranhaoListView.as_view(), name="garanhao_list"),
    path('doadoras/', DoadoraListView.as_view(), name="doadora_list"),
    path('receptoras/', ReceptoraListView.as_view(), name="receptora_list"),
    path('animais/', AnimalListView.as_view(), name="animal_list"),
    path('novoanimal/', AnimalCreateView.as_view(), name="animal_create"),
    path('clientes/', ClienteListView.as_view(), name="client_list"),
    path('novocliente/', ClienteCreateView.as_view(), name="client_create"),
    path('haras/', HarasListView.as_view(), name="haras_list"),
    path('auxiliares/', AuxiliarListView.as_view(), name="auxiliar_list"),
    path('novoauxiliar/', AuxiliarCreateView.as_view(), name="auxiliar_create"),
    path('servicos/', ServicosView.as_view(), name="servicos"),
]