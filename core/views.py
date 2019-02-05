from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import *
from core.forms import AnimalForm

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class Agenda(LoginRequiredMixin, TemplateView):
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super(Agenda, self).get_context_data(**kwargs)
        context["agenda_page"] = "active"
        return context

class Garanhoes(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'garanhoes.html'
    queryset = Animal.objects.filter(type='garanhao')

    def get_context_data(self, **kwargs):
        context = super(Garanhoes, self).get_context_data(**kwargs)
        context["garanhoes_page"] = "active"
        return context

class Doadoras(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'doadoras.html'
    queryset = Animal.objects.filter(type='doadora')

    def get_context_data(self, **kwargs):
        context = super(Doadoras, self).get_context_data(**kwargs)
        context["doadoras_page"] = "active"
        return context

class Receptoras(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'receptoras.html'
    queryset = Animal.objects.filter(type='receptora')

    def get_context_data(self, **kwargs):
        context = super(Receptoras, self).get_context_data(**kwargs)
        context["receptoras_page"] = "active"
        return context

class NewAnimal(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'new_animal.html'
    form_class = AnimalForm

    def get_context_data(self, **kwargs):
        context = super(NewAnimal, self).get_context_data(**kwargs)
        context["type_url"] = "{}_list".format(self.kwargs['type'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        type = self.kwargs['type']
        obj.type = type
        obj.save()
        return HttpResponseRedirect(reverse_lazy("{}_list".format(type)))

class Clientes(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clientes.html'

    def get_context_data(self, **kwargs):
        context = super(Clientes, self).get_context_data(**kwargs)
        context["client_page"] = "active"
        return context

class HarasList(LoginRequiredMixin, ListView):
    model = Haras
    template_name = 'haras_list.html'

    def get_context_data(self, **kwargs):
        context = super(HarasList, self).get_context_data(**kwargs)
        context["haras_page"] = "active"
        return context

class Auxiliares(LoginRequiredMixin, ListView):
    model = Ancillary
    template_name = 'auxiliares.html'

    def get_context_data(self, **kwargs):
        context = super(Auxiliares, self).get_context_data(**kwargs)
        context["auxiliar_page"] = "active"
        return context