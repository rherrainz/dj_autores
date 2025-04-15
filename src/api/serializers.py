from rest_framework.serializers import ModelSerializer
from frases.models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento', 'fecha_muerte', 'activo']