from django.contrib import admin

from usuario.models import SolicitudAyuda


from django.contrib import admin
from usuario.models import SolicitudAyuda


@admin.register(SolicitudAyuda)
class SolicitudAyudaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'correo', 'texto', 'fecha_creacion')  # Mostrar estos campos en la lista
    search_fields = ('usuario__username', 'correo', 'texto')  # Búsqueda por usuario, correo o texto
    list_filter = ('fecha_creacion',)  # Filtro por fecha de creación
    ordering = ('-fecha_creacion',)  # Ordenar por fecha de creación (descendente)
    date_hierarchy = 'fecha_creacion'  # Navegación jerárquica por fechas
    list_per_page = 25  # Mostrar 25 registros por página para mejor usabilidad

    # Opcional: Si deseas limitar la longitud del texto en la lista para que sea más legible
    def texto_corto(self, obj):
        return (obj.texto[:50] + '...') if len(obj.texto) > 50 else obj.texto
    texto_corto.short_description = 'Texto'

    # Si decides usar `texto_corto` en lugar del campo completo
    list_display = ('id', 'usuario', 'correo', 'texto_corto', 'fecha_creacion')
