from django.urls import path
from . import views

app_name = 'frases'

urlpatterns = [
    path('', views.index, name='index'),
    path('autor/', views.autor_list, name='autor_list'),
    path('inactivo/', views.inactivo_list, name='inactivo_list'),
    path('autor/<int:autor_id>/', views.autor_detail, name='autor_detail'),
    path('autor/json/', views.autor_json, name='autor_json'),
    path('autor/delete/<int:autor_id>/', views.delete_autor, name='delete_autor'),
]