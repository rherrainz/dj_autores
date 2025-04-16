from django.urls import path
from .views import AutorListCreateAPIView, AutorRetrieveUpdateDestroyAPIView
from .views import FraseListCreateAPIView, FraseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('autores/', AutorListCreateAPIView.as_view(),
         name='autor_list_create_api'),
    path('autores/<int:pk>/', AutorRetrieveUpdateDestroyAPIView.as_view(),
         name='autor_detail_api'),
    path('frases/', FraseListCreateAPIView.as_view(),
         name='frase_list_create_api'),
    path('frases/<int:pk>/', FraseRetrieveUpdateDestroyAPIView.as_view(),
         name='frase_detail_api'),
]
