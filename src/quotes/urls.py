from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.FraseListView.as_view(), name='frase_list'),  # Todas las frases
    path('visibles/', views.FraseListView.as_view(), {'visibles': 'visibles'}, name='frase_visibles'),  # Frases visibles
    path('invisibles/', views.FraseListView.as_view(), {'visibles': 'invisibles'}, name='frase_invisibles'),  # Frases invisibles
    path('frase/new/', views.FraseCreateView.as_view(), name='frase_create'),
    path('frase/edit/<int:pk>', views.FraseUpdateView.as_view(), name='frase_edit'),
    path('frase/delete/<int:pk>', views.FraseDeleteView.as_view(), name='frase_delete'),
    path('frase/<int:frase_id>/', views.frase_detail, name='frase_detail'),
    path('frase/author/<int:author_id>/', views.frase_per_author, name='frase_per_author'),
]