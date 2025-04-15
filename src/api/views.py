from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import AutorSerializer
from frases.models import Autor

class AutorListView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetailView(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # lookup_field = 'id'  # por defecto busca el ID
