from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AutorSerializer, FraseSerializer
from frases.models import Autor
from quotes.models import Frase

class AutorListCreateAPIView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # lookup_field = 'id'  # por defecto busca el ID

class FraseListCreateAPIView(ListCreateAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer

class FraseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer
    # lookup_field = 'id'  # por defecto busca el ID