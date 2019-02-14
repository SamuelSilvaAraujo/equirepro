from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import *
from core.forms import *

class IndexView(TemplateView):
    template_name = 'index.html'

class AgendaView(LoginRequiredMixin, TemplateView):
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)
        context["agenda_page"] = "active"
        return context

class GaranhaoListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'garanhao_list.html'
    queryset = Animal.objects.filter(type='garanhao')

    def get_context_data(self, **kwargs):
        context = super(GaranhaoListView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        context["animais_page"] = "active"
        return context

class DoadoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'doadora_list.html'
    queryset = Animal.objects.filter(type='doadora')

    def get_context_data(self, **kwargs):
        context = super(DoadoraListView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        context["animais_page"] = "active"
        return context

class ReceptoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'receptora_list.html'
    queryset = Animal.objects.filter(type='receptora')

    def get_context_data(self, **kwargs):
        context = super(ReceptoraListView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        context["animais_page"] = "active"
        return context

class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = AnimalForm

    def get_context_data(self, **kwargs):
        context = super(AnimalCreateView, self).get_context_data(**kwargs)
        context["type_url"] = "{}_list".format(self.kwargs['type'])
        context["animais_page"] = "active"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        type = self.kwargs['type']
        obj.type = type
        obj.save()
        return HttpResponseRedirect(reverse_lazy("{}_list".format(type)))

class ClienteListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class ClienteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cliente_create.html'
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy("client_list"))

class HarasListView(LoginRequiredMixin, ListView):
    model = Haras
    template_name = 'haras_list.html'

    def get_context_data(self, **kwargs):
        context = super(HarasListView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        return context

class AuxiliarListView(LoginRequiredMixin, ListView):
    model = Ancillary
    template_name = 'auxiliar_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuxiliarListView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class ServicosView(LoginRequiredMixin, TemplateView):
    template_name = 'servicos.html'

    def get_context_data(self, **kwargs):
        context = super(ServicosView, self).get_context_data(**kwargs)
        context["service_page"] = "active"
        return context