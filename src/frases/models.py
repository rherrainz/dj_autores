from django.db import models

# Create your models here.
class Autor(models.Model):
    NACIONALIDAD_CHOICES = [
        ('ARG', 'Argentina'),
        ('ESP', 'España'),
        ('USA', 'Estados Unidos'),
        ('MEX', 'México'),
        ('COL', 'Colombia'),
        ('PER', 'Perú'),
        ('CHL', 'Chile'),
        ('VEN', 'Venezuela'),
        ('ECU', 'Ecuador'),
        ('BOL', 'Bolivia'),
        ('PAR', 'Paraguay'),
        ('URY', 'Uruguay'),
        ('CRI', 'Costa Rica'),
        ('CUB', 'Cuba'),
        ('DOM', 'República Dominicana'),
        ('NIC', 'Nicaragua'),
        ('HND', 'Honduras'),
        ('GTM', 'Guatemala'),
        ('SLV', 'El Salvador'),
        ('PAN', 'Panamá'),
        ('PRY', 'Paraguay'),
        ('BRA', 'Brasil'),
        ('CHL', 'Chile'),
        ('URY', 'Uruguay'),
        ('BOL', 'Bolivia'),
        ('PAR', 'Paraguay'),
        ('VEN', 'Venezuela'),
        ('COL', 'Colombia'),
        ('PER', 'Perú'),
        ('ECU', 'Ecuador'),
        ('CRI', 'Costa Rica'),
        ('CUB', 'Cuba'),
        ('DOM', 'República Dominicana'),
        ('NIC', 'Nicaragua'),
        ('HND', 'Honduras'),
        ('GTM', 'Guatemala'),
        ('SLV', 'El Salvador'),
        ('PAN', 'Panamá')
        # Agregar más nacionalidades según sea necesario    
    ]
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30, choices=NACIONALIDAD_CHOICES)
    fecha_nacimiento = models.DateField()
    fecha_muerte = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.apellido + ", " + self.nombre + " (" + self.nacionalidad + ")" + " (" + str(self.fecha_nacimiento) + ")"