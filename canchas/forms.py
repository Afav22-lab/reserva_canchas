from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
from .models import Reserva


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'


class ReservaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha de Reserva'
    )
    hora_inicio = forms.ChoiceField(
        choices=Reserva.HORARIOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Hora de Inicio'
    )
    hora_fin = forms.ChoiceField(
        choices=Reserva.HORARIOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Hora de Finalización'
    )

    class Meta:
        model = Reserva
        fields = ['fecha', 'hora_inicio', 'hora_fin']

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        from datetime import date
        if fecha < date.today():
            raise forms.ValidationError('No puedes reservar en una fecha pasada.')
        return fecha
    
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')
        
        if hora_inicio and hora_fin:
            # Convertir a enteros para comparar (formato 24 horas)
            inicio = int(hora_inicio.split(':')[0])
            fin = int(hora_fin.split(':')[0])
            
            # Manejar el caso especial de medianoche (00:00)
            if fin == 0:  # 12:00 AM = medianoche
                fin = 24  # Tratarlo como 24 para cálculos
            
            # Si el horario es 8 AM a 12 AM, inicio debe ser >= 8 y fin puede ser hasta 24
            if inicio < 8:
                raise forms.ValidationError('El horario de inicio debe ser desde las 8:00 AM.')
            
            if fin <= inicio:
                raise forms.ValidationError('La hora de finalización debe ser posterior a la hora de inicio.')
            
            duracion = fin - inicio
            if duracion > 16:
                raise forms.ValidationError('No puedes reservar más de 16 horas consecutivas.')
        
        # NUEVA VALIDACIÓN: Verificar que no se reserven horas que ya pasaron
        if fecha and hora_fin:
            # Obtener la hora actual en la zona horaria de Colombia
            colombia_tz = pytz.timezone('America/Bogota')
            ahora_colombia = timezone.now().astimezone(colombia_tz)
            hoy = ahora_colombia.date()
            hora_actual = ahora_colombia.hour
            minuto_actual = ahora_colombia.minute
            
            # Si es HOY, verificar que la hora de fin no haya pasado
            if fecha == hoy:
                hora_fin_int = int(hora_fin.split(':')[0])
                minuto_fin_int = int(hora_fin.split(':')[1])
                
                # Si la hora de fin ya pasó (excepto medianoche que es para mañana)
                if hora_fin_int != 0:  # No validar si es medianoche (reserva hasta mañana)
                    if hora_fin_int < hora_actual or (hora_fin_int == hora_actual and minuto_fin_int <= minuto_actual):
                        raise forms.ValidationError(
                            f'No puedes reservar en un horario que ya pasó. '
                            f'La hora actual es {hora_actual:02d}:{minuto_actual:02d}. '
                            f'Por favor selecciona un horario futuro.'
                        )
        
        return cleaned_data
