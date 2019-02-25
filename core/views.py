from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *

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
        return context

class GaranhaoCreateView(CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = AnimalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.type = 'garanhao'
        obj.save()
        return HttpResponseRedirect(reverse_lazy("garanhao_list"))

    def get_context_data(self, **kwargs):
        context = super(GaranhaoCreateView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        context["cancel"] = "garanhao_list"
        context["title"] = "Novo Garanhão"
        return context

class DoadoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'doadora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='doadora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DoadoraListView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        return context

class DoadoraCreateView(CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = AnimalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.type = 'doadora'
        obj.save()
        return HttpResponseRedirect(reverse_lazy("doadora_list"))

    def get_context_data(self, **kwargs):
        context = super(DoadoraCreateView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        context["cancel"] = "doadora_list"
        context["title"] = "Nova Doadora"
        return context

class ReceptoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'receptora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='receptora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReceptoraListView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        return context

class ReceptoraCreateView(CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = AnimalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.type = 'receptora'
        obj.save()
        return HttpResponseRedirect(reverse_lazy("receptora_list"))

    def get_context_data(self, **kwargs):
        context = super(ReceptoraCreateView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        context["cancel"] = "receptora_list"
        context["title"] = "Nova receptora"
        return context

class AnimalPerfilView(DetailView):
    model = Animal
    template_name = 'animal_perfil.html'

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'client_create.html'
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy("client_list"))

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class ClientCreateModalView(CreateView):
    model = Client
    template_name = 'client_create_modal.html'
    form_class = ClientForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy("client_list"))

class ServiceReliazedListView(LoginRequiredMixin, ListView):
    template_name = 'service_realized_list.html'
    model = ServiceRealized

    def get_queryset(self):
        return ServiceRealized.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ServiceReliazedListView, self).get_context_data(**kwargs)
        context["service_page"] = "active"
        context["service_list"] = Service.objects.filter(user=self.request.user)
        return context

class ServiceRealizedCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRealized
    template_name = 'service_realized_create.html'
    form_class = ServiceRealizedForm
    second_form_class = ServiceRealizedLineFormset
    success_url = reverse_lazy("service_realized_list")

    def get_context_data(self, **kwargs):
        context = super(ServiceRealizedCreateView, self).get_context_data(**kwargs)
        context["formset"] = ServiceRealizedLineFormset()
        context["service_page"] = "active"
        return context

    def form_valid(self, form):
        formset = self.second_form_class(self.request.POST)
        with transaction.atomic():
            print(formset.is_valid())
            obj = form.save(commit=False)
            obj.user = self.request.user
            # obj.save()
            if formset.is_valid():
                formset.instance = obj
                # formset.save()
        return super(ServiceRealizedCreateView, self).form_valid(form)

class ServiceModalCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'service_create_modal.html'
    form_class = ServiceForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy("service_realized_list"))

    def get_context_data(self, **kwargs):
        context = super(ServiceModalCreateView, self).get_context_data(**kwargs)
        context["service_page"] = "active"
        return context

class HarasListView(LoginRequiredMixin, ListView):
    model = Haras
    template_name = 'haras_list.html'

    def get_queryset(self):
        haras_list = []
        clients = self.request.user.client_set.all()
        for client in clients:
            haras_list += client.haras_set.all()
        return haras_list

    def get_context_data(self, **kwargs):
        context = super(HarasListView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        return context

class HarasCreateView(LoginRequiredMixin, CreateView):
    model = Haras
    template_name = 'haras_create.html'
    form_class = HarasForm
    second_form_class = AddresForm

    def form_valid(self, form):
        adress_obj = self.second_form_class(self.request.POST).save()
        haras_obj = form.save(commit=False)
        haras_obj.address = adress_obj
        haras_obj.save()
        return HttpResponseRedirect(reverse_lazy("haras_list"))

    def get_context_data(self, **kwargs):
        context = super(HarasCreateView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        context["address_form"] = AddresForm
        return context

class AuxiliarListView(LoginRequiredMixin, ListView):
    model = Ancillary
    template_name = 'auxiliar_list.html'

    def get_queryset(self):
        auxiliares = []
        clients = self.request.user.client_set.all()
        for client in clients:
            haras = client.haras_set.all()
            for h in haras:
                auxiliares += h.ancillary_set.all()
        return auxiliares

    def get_context_data(self, **kwargs):
        context = super(AuxiliarListView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class AuxiliarCreateView(LoginRequiredMixin, CreateView):
    model = Ancillary
    template_name = 'auxiliar_create.html'
    form_class = AuxiliarForm
    success_url = reverse_lazy("auxiliar_list")

    def get_context_data(self, **kwargs):
        context = super(AuxiliarCreateView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context