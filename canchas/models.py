from django.db import models
from django.contrib.auth.models import User


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='canchas/', blank=True, null=True, verbose_name='Imagen')
    precio_por_hora = models.DecimalField(max_digits=10, decimal_places=2, default=50000, verbose_name='Precio por Hora (COP)')
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
        ('archivada', 'Archivada'),
    ]
    
    HORARIOS_CHOICES = [
        ('08:00', '8:00 AM'),
        ('09:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '1:00 PM'),
        ('14:00', '2:00 PM'),
        ('15:00', '3:00 PM'),
        ('16:00', '4:00 PM'),
        ('17:00', '5:00 PM'),
        ('18:00', '6:00 PM'),
        ('19:00', '7:00 PM'),
        ('20:00', '8:00 PM'),
        ('21:00', '9:00 PM'),
        ('22:00', '10:00 PM'),
        ('23:00', '11:00 PM'),
        ('00:00', '12:00 AM'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora_inicio = models.CharField(max_length=5, choices=HORARIOS_CHOICES, default='08:00')
    hora_fin = models.CharField(max_length=5, choices=HORARIOS_CHOICES, default='09:00')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='confirmada')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.cancha.nombre} - {self.fecha} ({self.hora_inicio}-{self.hora_fin})"
    
    @property
    def duracion_horas(self):
        """Calcula cuántas horas dura la reserva"""
        hora_inicio = int(self.hora_inicio.split(':')[0])
        hora_fin = int(self.hora_fin.split(':')[0])
        
        # Manejar el caso de medianoche (00:00)
        if hora_fin == 0:
            hora_fin = 24
        
        return hora_fin - hora_inicio

    @property
    def costo_total(self):
        """Calcula el costo total de la reserva"""
        return self.cancha.precio_por_hora * self.duracion_horas
    
    @property
    def costo_total_formateado(self):
        """Retorna el costo total formateado con separador de miles"""
        total = self.costo_total
        return f"${total:,.0f}".replace(',', '.')

    @property
    def esta_vencida(self):
        """Verifica si la reserva ya pasó su fecha"""
        from django.utils import timezone
        return self.fecha < timezone.now().date()
    
    @property
    def esta_activa(self):
        """Verifica si la reserva está activa (no cancelada ni completada)"""
        return self.estado in ['pendiente', 'confirmada']
    
    def archivar_si_vencida(self):
        """Marca como completada si ya pasó la fecha"""
        if self.esta_vencida and self.esta_activa:
            self.estado = 'completada'
            self.save()
            return True
        return False

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_reserva']
