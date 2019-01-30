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

class Animais(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animais.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Animais, self).get_context_data(*args, **kwargs)
        context["garanhoes"] = self.request.user.animal_set.filter(type="GANHARAO")
        context["doadoras"] = self.request.user.animal_set.filter(type="DOADORA")
        context["receptoras"] = self.request.user.animal_set.filter(type="RECEPTORA")
        context["animal_page"] = "active"
        return context

class NovoAnimal(LoginRequiredMixin, CreateView):
    model = Animais
    template_name = 'novo_animal.html'
    form_class = AnimalForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('animal_list'))

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