from django.db import models
from django.contrib.auth.models import User


class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
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
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='confirmada')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.cancha.nombre} - {self.fecha}"

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
