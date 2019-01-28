from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Animal
from core.forms import AnimalForm

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class Agenda(LoginRequiredMixin, TemplateView):
    template_name = 'agenda.html'

class Animais(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animais.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Animais, self).get_context_data(*args, **kwargs)
        context["garanhoes"] = self.request.user.animal_set.filter(tipo="GANHARAO")
        context["doadoras"] = self.request.user.animal_set.filter(tipo="DOADORA")
        context["receptoras"] = self.request.user.animal_set.filter(tipo="RECEPTORA")
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