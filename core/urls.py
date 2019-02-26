from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('agenda/', AgendaView.as_view(), name="agenda"),
    path('garanhoes/', GaranhaoListView.as_view(), name="garanhao_list"),
    path('garanhao/', include([
        path('cadastro/', GaranhaoCreateView.as_view(), name="garanhao_create"),
        path('editar/<int:pk>/', GaranhaoUpdateView.as_view(), name="garanhao_update"),
        path('excluir/<int:pk>/', GaranhaoDeleteView.as_view(), name="garanhao_delete"),
    ])),
    path('doadoras/', DoadoraListView.as_view(), name="doadora_list"),
    path('doadora/', include([
        path('cadastro/', DoadoraCreateView.as_view(), name="doadora_create"),
        path('editar/<int:pk>/', DoadoraUpdateView.as_view(), name="doadora_update"),
        path('exluir/<int:pk>/', DoadoraDeleteView.as_view(), name="doadora_delete"),
    ])),
    path('receptoras/', ReceptoraListView.as_view(), name="receptora_list"),
    path('receptora/', include([
        path('cadastro/', ReceptoraCreateView.as_view(), name="receptora_create"),
        path('editar/<int:pk>/', ReceptoraUpdateView.as_view(), name="receptora_update"),
        path('exluir/<int:pk>/', ReceptoraDeleteView.as_view(), name="receptora_delete"),
        path('<int:pk>/cicloestral/', ReceptoraCicloEstralView.as_view(), name="receptora_ciclo_estral"),
        path('<int:pk>/cicloestral/cadastro/', ReceptoraCicloEstralCreateView.as_view(), name="receptora_ciclo_estral_create"),
    ])),
    path('clientes/', ClientListView.as_view(), name="client_list"),
    path('cliente/', include([
        path('cadastro/', ClientCreateView.as_view(), name="client_create"),
        path('modal/novo/', ClientCreateModalView.as_view(), name="client_modal_create"),
    ])),
    path('haras/', include([
        path('', HarasListView.as_view(), name="haras_list"),
        path('cadastro/', HarasCreateView.as_view(), name="haras_create"),
    ])),
    path('auxiliares/', AuxiliarListView.as_view(), name="auxiliar_list"),
    path('auxiliar', include([
        path('cadastro/', AuxiliarCreateView.as_view(), name="auxiliar_create"),
    ])),
    path('servicos/', ServiceReliazedListView.as_view(), name="service_realized_list"),
    path('servico/', include([
        path('cadastro/', ServiceRealizedCreateView.as_view(), name="service_realized_create"),
        path('modal/create/', ServiceModalCreateView.as_view(), name="service_create"),
    ])),
]