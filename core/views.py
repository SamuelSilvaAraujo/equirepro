from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
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

#Garanhão views
class GaranhaoListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal/garanhao_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='garanhao', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(GaranhaoListView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        return context

class GaranhaoCreateView(CreateView):
    model = Animal
    template_name = 'animal/animal_create.html'
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

class GaranhaoUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animal_update.html'
    success_url = reverse_lazy("garanhao_list")

    def get_context_data(self, **kwargs):
        context = super(GaranhaoUpdateView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        context["cancel"] = "garanhao_list"
        context["title"] = "Editar Garanhão"
        return context

class GaranhaoDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("garanhao_list")
    template_name = 'animal/animal_delete.html'

    def get_context_data(self, **kwargs):
        context = super(GaranhaoDeleteView, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        context["confirme"] = "garanhao_delete"
        context["animal_id"] = self.kwargs["pk"]
        context["cancel"] = "garanhao_list"
        return context

#Doadoras views
class DoadoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal/doadora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='doadora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(DoadoraListView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        return context

class DoadoraCreateView(CreateView):
    model = Animal
    template_name = 'animal/animal_create.html'
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

class DoadoraUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animal_update.html'
    success_url = reverse_lazy("doadora_list")

    def get_context_data(self, **kwargs):
        context = super(DoadoraUpdateView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        context["cancel"] = "doadora_list"
        context["title"] = "Editar Doadora"
        return context

class DoadoraDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("doadora_list")
    template_name = 'animal/animal_delete.html'

    def get_context_data(self, **kwargs):
        context = super(DoadoraDeleteView, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        context["confirme"] = "doadora_delete"
        context["animal_id"] = self.kwargs["pk"]
        context["cancel"] = "doadora_list"
        return context

class DoadoraCicloEstralView(ListView):
    model = CicloEstral
    template_name = 'animal/ciclo_estral.html'

    def get_queryset(self):
        return Animal.objects.get(pk=self.kwargs["pk"]).cicloestral_set.all()

    def get_context_data(self, **kwargs):
        context = super(DoadoraCicloEstralView, self).get_context_data(**kwargs)
        context["egua_obj"] = Animal.objects.get(pk=self.kwargs["pk"])
        context["doadoras_page"] = "active"
        context["create_page"] = "doadora_ciclo_estral_create"
        context["title"] = "Doadora"
        return context

class DoadoraCicloEstralCreateView(CreateView):
    model = CicloEstral
    form_class = CicloEstralForm
    template_name = 'animal/ciclo_estral_create.html'

    def form_valid(self, form):
        egua = Animal.objects.get(pk=self.kwargs["pk"])
        obj = form.save(commit=False)
        obj.egua = egua
        obj.save()
        return HttpResponseRedirect(reverse_lazy("doadora_ciclo_estral", kwargs={"pk": self.kwargs["pk"]}))

    def get_context_data(self, **kwargs):
        context = super(DoadoraCicloEstralCreateView, self).get_context_data(**kwargs)
        context["egua_id"] = self.kwargs["pk"]
        context["doadoras_page"] = "active"
        return context

#Receptoras views
class ReceptoraListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal/receptora_list.html'

    def get_queryset(self):
        return Animal.objects.filter(type='receptora', user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReceptoraListView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        return context

class ReceptoraCreateView(CreateView):
    model = Animal
    template_name = 'animal/animal_create.html'
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

class ReceptoraUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animal_update.html'
    success_url = reverse_lazy("receptora_list")

    def get_context_data(self, **kwargs):
        context = super(ReceptoraUpdateView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        context["cancel"] = "receptora_list"
        context["title"] = "Editar Receptora"
        return context

class ReceptoraDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("receptora_list")
    template_name = 'animal/animal_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ReceptoraDeleteView, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        context["confirme"] = "receptora_delete"
        context["animal_id"] = self.kwargs["pk"]
        context["cancel"] = "receptora_list"
        return context

class ReceptoraCicloEstralView(ListView):
    model = CicloEstral
    template_name = 'animal/ciclo_estral.html'

    def get_queryset(self):
        return Animal.objects.get(pk=self.kwargs["pk"]).cicloestral_set.all()

    def get_context_data(self, **kwargs):
        context = super(ReceptoraCicloEstralView, self).get_context_data(**kwargs)
        context["egua_obj"] = Animal.objects.get(pk=self.kwargs["pk"])
        context["receptoras_page"] = "active"
        context["create_page"] = "receptora_ciclo_estral_create"
        context["title"] = "Receptora"
        return context

class ReceptoraCicloEstralCreateView(CreateView):
    model = CicloEstral
    form_class = CicloEstralForm
    template_name = 'animal/ciclo_estral_create.html'

    def form_valid(self, form):
        egua = Animal.objects.get(pk=self.kwargs["pk"])
        obj = form.save(commit=False)
        obj.egua = egua
        obj.save()
        return HttpResponseRedirect(reverse_lazy("receptora_ciclo_estral", kwargs={"pk": self.kwargs["pk"]}))

    def get_context_data(self, **kwargs):
        context = super(ReceptoraCicloEstralCreateView, self).get_context_data(**kwargs)
        context["egua_id"] = self.kwargs["pk"]
        context["receptoras_page"] = "active"
        return context

#Clientes views
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_list.html'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'client/client_create.html'
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

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'client/client_update.html'
    form_class = ClientForm
    success_url = reverse_lazy("client_list")

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy("client_list")

    def get_context_data(self, **kwargs):
        context = super(ClientDeleteView, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        context["client_id"] = self.kwargs["pk"]
        return context

class ClientCreateModalView(CreateView):
    model = Client
    template_name = 'client/client_create_modal.html'
    form_class = ClientForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy("client_list"))

#Serviços views
class ServiceReliazedListView(LoginRequiredMixin, ListView):
    template_name = 'service/service_realized_list.html'
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
    template_name = 'service/service_realized_create.html'
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
    template_name = 'service/service_create_modal.html'
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

#Haras views
class HarasListView(LoginRequiredMixin, ListView):
    model = Haras
    template_name = 'haras/haras_list.html'

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
    template_name = 'haras/haras_create.html'
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

class HarasUpdateView(LoginRequiredMixin, UpdateView):
    model = Haras
    form_class = HarasForm
    template_name = 'haras/haras_update.html'
    second_form_class = AddresForm

    def form_valid(self, form):
        adress_obj = self.second_form_class(self.request.POST).save()
        haras_obj = form.save(commit=False)
        haras_obj.address = adress_obj
        haras_obj.save()
        return HttpResponseRedirect(reverse_lazy("haras_list"))

    def get_context_data(self, **kwargs):
        context = super(HarasUpdateView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        context["address_form"] = self.second_form_class(instance=self.object.address)
        return context

class HarasDeleteView(LoginRequiredMixin, DeleteView):
    model = Haras
    template_name = 'haras/haras_delete.html'
    success_url = reverse_lazy("haras_list")

    def get_context_data(self, **kwargs):
        context = super(HarasDeleteView, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        context["haras_id"] = self.kwargs["pk"]
        return context

#Auxiliares views
class AncillaryListView(LoginRequiredMixin, ListView):
    model = Ancillary
    template_name = 'ancillary/ancillary_list.html'

    def get_queryset(self):
        auxiliares = []
        clients = self.request.user.client_set.all()
        for client in clients:
            haras = client.haras_set.all()
            for h in haras:
                auxiliares += h.ancillary_set.all()
        return auxiliares

    def get_context_data(self, **kwargs):
        context = super(AncillaryListView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class AncillaryCreateView(LoginRequiredMixin, CreateView):
    model = Ancillary
    template_name = 'ancillary/ancillary_create.html'
    form_class = AncillaryForm
    success_url = reverse_lazy("auxiliar_list")

    def get_context_data(self, **kwargs):
        context = super(AncillaryCreateView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class AncillaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Ancillary
    form_class = AncillaryForm
    template_name = 'ancillary/ancillary_update.html'
    success_url = reverse_lazy("auxiliar_list")

    def get_context_data(self, **kwargs):
        context = super(AncillaryUpdateView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context

class AncillaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Ancillary
    template_name = 'ancillary/ancillary_delete.html'
    success_url = reverse_lazy("auxiliar_list")

    def get_context_data(self, **kwargs):
        context = super(AncillaryDeleteView, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        context["auxiliar_id"] = self.kwargs["pk"]
        return context