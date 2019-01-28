from django.urls import path

from core.views import Agenda, Animais, NovoAnimal

urlpatterns = [
    path('agenda/', Agenda.as_view(), name="agenda"),
    path('animal/list/', Animais.as_view(), name="animal_list"),
    path('animal/novo/', NovoAnimal.as_view(), name="animal_novo"),
]