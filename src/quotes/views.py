from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Frase

# Create your views here.


class FraseListView(LoginRequiredMixin, ListView):
    model = Frase
    template_name = 'quotes/frase_list.html'
    context_object_name = 'frases'

    def get_queryset(self):
        visibles = self.kwargs.get('visibles', 'todas')
        if visibles == 'visibles':
            return Frase.objects.filter(visible=True)
        elif visibles == 'invisibles':
            return Frase.objects.filter(visible=False)
        else:
            return Frase.objects.all()


class FraseCreateView(LoginRequiredMixin, CreateView):
    model = Frase
    template_name = 'quotes/frase_form.html'
    fields = ['texto', 'autor']
    success_url = reverse_lazy('quotes:frase_list')

 
class FraseUpdateView(LoginRequiredMixin, UpdateView):
    model = Frase
    template_name = 'quotes/frase_form.html'
    fields = ['texto', 'autor']
    success_url = '/quotes/'

    def get_object(self, queryset=None):
        return get_object_or_404(Frase, pk=self.kwargs['pk'])


class FraseDeleteView(LoginRequiredMixin, DeleteView):
    model = Frase
    template_name = 'quotes/frase_confirm_delete.html'
    success_url = '/quotes/'

    def get_object(self, queryset=None):
        return get_object_or_404(Frase, pk=self.kwargs['pk'])

@login_required
def frase_detail(request, frase_id):
    frase = get_object_or_404(Frase, id=frase_id)
    return render(request, 'quotes/frase_detail.html', {'frase': frase})

@login_required
def frase_per_author(request, author_id):
    frases = Frase.objects.filter(autor_id=author_id)
    return render(request, 'quotes/frases_per_author.html', {'frases': frases})
