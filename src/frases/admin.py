from django.contrib import admin
from .models import Autor
# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_muerte', 'activo')
    search_fields = ('apellido', 'nombre')
    list_filter = ('nacionalidad', 'activo')
    ordering = ('apellido', 'nombre')
    list_per_page = 10
    date_hierarchy = 'fecha_nacimiento'
    list_editable = ('activo',)
    fieldsets = (
        (None, {
            'fields': ('apellido', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_muerte', 'activo')
        }),
    )
    
