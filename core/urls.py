from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('agenda/', AgendaView.as_view(), name="agenda"),
    path('garanhoes/', GaranhaoListView.as_view(), name="garanhao_list"),
    path('garanhao/novo/', GaranhaoCreateView.as_view(), name="garanhao_create"),
    path('doadoras/', DoadoraListView.as_view(), name="doadora_list"),
    path('doadora/novo/', DoadoraCreateView.as_view(), name="doadora_create"),
    path('receptoras/', ReceptoraListView.as_view(), name="receptora_list"),
    path('receptora/novo/', ReceptoraCreateView.as_view(), name="receptora_create"),
    path('clientes/', ClientListView.as_view(), name="client_list"),
    path('cliente/novo/', ClientCreateView.as_view(), name="client_create"),
    path('cliente/modal/novo/', ClientCreateModalView.as_view(), name="client_modal_create"),
    path('haras/', HarasListView.as_view(), name="haras_list"),
    path('haras/novo/', HarasCreateView.as_view(), name="haras_create"),
    path('auxiliares/', AuxiliarListView.as_view(), name="auxiliar_list"),
    path('novoauxiliar/', AuxiliarCreateView.as_view(), name="auxiliar_create"),
    path('servicos/', ServiceReliazedListView.as_view(), name="service_realized_list"),
    path('servico/novo/', ServiceRealizedCreateView.as_view(), name="service_realized_create"),
    path('servico/modal/create/', ServiceModalCreateView.as_view(), name="service_create"),
]