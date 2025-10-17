from django.contrib import admin
from .models import Cancha, Reserva


@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cancha', 'fecha', 'estado', 'fecha_reserva', 'esta_vencida_icon']
    list_filter = ['estado', 'fecha', 'cancha']
    search_fields = ['usuario__username', 'cancha__nombre']
    date_hierarchy = 'fecha'
    actions = ['archivar_vencidas']
    
    def esta_vencida_icon(self, obj):
        """Muestra icono si la reserva está vencida"""
        from django.utils.html import format_html
        if obj.esta_vencida:
            return format_html('<span style="color: red;">⏰ Vencida</span>')
        return format_html('<span style="color: green;">✓ Vigente</span>')
    esta_vencida_icon.short_description = 'Estado Fecha'
    
    def archivar_vencidas(self, request, queryset):
        """Acción para archivar reservas vencidas seleccionadas"""
        actualizadas = queryset.filter(
            esta_vencida=True,
            estado__in=['pendiente', 'confirmada']
        ).update(estado='completada')
        
        self.message_user(request, f'{actualizadas} reservas archivadas.')
    archivar_vencidas.short_description = 'Archivar reservas vencidas seleccionadas'
