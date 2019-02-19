from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

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

    def get_queryset(self):
        return Animal.objects.filter(type='garanhao', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(GaranhaoListView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        context["animais_page"] = "active"
        return context

class DoadoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'doadora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='doadora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DoadoraListView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        context["animais_page"] = "active"
        return context

class ReceptoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'receptora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='receptora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReceptoraListView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        context["animais_page"] = "active"
        return context

class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnimalListView, self).get_context_data(**kwargs)
        animais = Animal.objects.filter(user=self.request.user)
        context["garanhoes"] = animais.filter(type="garanhao")
        context["doadoras"] = animais.filter(type="doadora")
        context["receptoras"] = animais.filter(type="receptora")
        context["animais_total"] = animais.count()
        context["animais_page"] = "active"
        return context

class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = AnimalForm

    def get_context_data(self, **kwargs):
        context = super(AnimalCreateView, self).get_context_data(**kwargs)
        context["animais_page"] = "active"
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        # type = self.kwargs['type']
        # obj.type = type
        obj.save()
        return HttpResponseRedirect(reverse_lazy("animal_list"))

class ClienteListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'cliente_list.html'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

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

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class HarasListView(LoginRequiredMixin, ListView):
    model = Haras
    template_name = 'haras_list.html'

    def get_context_data(self, **kwargs):
        context = super(HarasListView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        return context

class HarasCreateView(LoginRequiredMixin, CreateView):
    model = Haras
    template_name = 'haras_create.html'

    def get_context_data(self, **kwargs):
        context = super(HarasCreateView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        return context

class AuxiliarListView(LoginRequiredMixin, ListView):
    model = Ancillary
    template_name = 'auxiliar_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuxiliarListView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class AuxiliarCreateView(LoginRequiredMixin, CreateView):
    model = Ancillary
    template_name = 'auxiliar_create.html'
    form_class = AuxiliarForm

    def get_context_data(self, **kwargs):
        context = super(AuxiliarCreateView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class ServicosView(LoginRequiredMixin, ListView):
    template_name = 'servicos.html'
    model = Service

    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ServicosView, self).get_context_data(**kwargs)
        context["service_page"] = "active"
        return context