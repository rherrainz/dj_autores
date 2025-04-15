from django.urls import path
from .views import AutorListView, AutorDetailView

urlpatterns = [
    path('autores/', AutorListView.as_view(), name='autor_list_api'),
    path('autores/<int:pk>/', AutorDetailView.as_view(), name='autor_detail_api'),
]