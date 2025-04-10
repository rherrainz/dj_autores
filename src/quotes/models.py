from django.db import models
from frases.models import Autor
# Create your models here.
class Frase(models.Model):
    texto = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.texto} - {self.autor}"
