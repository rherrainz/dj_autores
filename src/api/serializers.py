from rest_framework.serializers import ModelSerializer
from frases.models import Autor
from quotes.models import Frase

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento', 'fecha_muerte', 'activo']


class FraseSerializer(ModelSerializer):
    class Meta:
        model = Frase
        fields = ['id', 'texto', 'autor', 'fecha_creacion', 'fecha_actualizacion', 'visible']