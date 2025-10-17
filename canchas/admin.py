from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils import timezone
from .models import Cancha, Reserva

# Deshabilitar "Mis acciones" en todo el admin
admin.site.disable_action('delete_selected')


@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cancha', 'fecha', 'hora_inicio', 'hora_fin', 'estado', 'fecha_reserva', 'esta_vencida_icon']
    list_filter = ['estado', 'fecha', 'cancha']
    search_fields = ['usuario__username', 'cancha__nombre']
    date_hierarchy = 'fecha'
    actions = ['archivar_vencidas']
    
    def changelist_view(self, request, extra_context=None):
        """Personalizar la vista principal del admin para agregar botón de historial"""
        extra_context = extra_context or {}
        extra_context['show_historial_button'] = True
        return super().changelist_view(request, extra_context=extra_context)
    
    def get_urls(self):
        """Agregar URL personalizada para historial"""
        urls = super().get_urls()
        custom_urls = [
            path('historial/', self.admin_site.admin_view(self.historial_view), name='reserva_historial'),
        ]
        return custom_urls + urls
    
    def historial_view(self, request):
        """Vista personalizada para mostrar historial de reservas pasadas"""
        hoy = timezone.now().date()
        
        # Obtener todas las reservas pasadas
        reservas_pasadas = Reserva.objects.filter(
            fecha__lt=hoy
        ).select_related('usuario', 'cancha').order_by('-fecha', '-hora_inicio')
        
        context = {
            'title': 'Historial de Reservas Pasadas',
            'reservas': reservas_pasadas,
            'total': reservas_pasadas.count(),
            'opts': self.model._meta,
            'has_view_permission': True,
        }
        
        return render(request, 'admin/canchas/reserva/historial.html', context)
    
    def esta_vencida_icon(self, obj):
        """Muestra si la reserva está vencida"""
        from django.utils.html import format_html
        if obj.esta_vencida:
            return format_html('<span style="color: red;">Vencida</span>')
        return format_html('<span style="color: green;">Vigente</span>')
    esta_vencida_icon.short_description = 'Estado Fecha'
    
    def archivar_vencidas(self, request, queryset):
        """Acción para archivar reservas vencidas seleccionadas"""
        hoy = timezone.now().date()
        actualizadas = queryset.filter(
            fecha__lt=hoy,
            estado__in=['pendiente', 'confirmada']
        ).update(estado='completada')
        
        self.message_user(request, f'{actualizadas} reservas archivadas.')
    archivar_vencidas.short_description = 'Archivar reservas vencidas seleccionadas'
