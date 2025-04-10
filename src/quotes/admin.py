from django.contrib import admin
from .models import Frase
from frases.models import Autor
# Register your models here.
class FraseAdmin(admin.ModelAdmin):
    list_display = ('texto', 'autor', 'fecha_creacion', 'fecha_actualizacion', 'visible')
    list_filter = ('visible',)
    search_fields = ('texto', 'autor__nombre', 'autor__apellido')
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_creacion'
    list_per_page = 10
    actions = ['make_visible', 'make_invisible']
    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    make_visible.short_description = "Marcar como visibles"
    def make_invisible(self, request, queryset):
        queryset.update(visible=False)
    make_invisible.short_description = "Marcar como invisibles"
admin.site.register(Frase, FraseAdmin)

