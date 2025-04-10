from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Frase

# Create your views here.


class FraseListView(ListView):
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


class FraseCreateView(CreateView):
    model = Frase
    template_name = 'quotes/frase_form.html'
    fields = ['texto', 'autor']
    success_url = reverse_lazy('quotes:frase_list')

 
class FraseUpdateView(UpdateView):
    model = Frase
    template_name = 'quotes/frase_form.html'
    fields = ['texto', 'autor']
    success_url = '/quotes/'

    def get_object(self, queryset=None):
        return get_object_or_404(Frase, pk=self.kwargs['pk'])


class FraseDeleteView(DeleteView):
    model = Frase
    template_name = 'quotes/frase_confirm_delete.html'
    success_url = '/quotes/'

    def get_object(self, queryset=None):
        return get_object_or_404(Frase, pk=self.kwargs['pk'])


def frase_detail(request, frase_id):
    try:
        frase = Frase.objects.get(id=frase_id)
    except Frase.DoesNotExist:
        return render(request, 'quotes/404.html', status=404)
    return render(request, 'quotes/frase.html', {'frase': frase})


def frase_per_author(request, author_id):
    frases = Frase.objects.filter(autor_id=author_id)
    return render(request, 'quotes/frases_per_author.html', {'frases': frases})
