from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from .models import Cancha, Reserva
from .forms import RegistroForm, ReservaForm


def archivar_reservas_vencidas():
    """
    Función auxiliar para archivar automáticamente reservas vencidas.
    Cambia el estado de 'pendiente' o 'confirmada' a 'completada' 
    para las reservas cuya hora de finalización ya pasó.
    """
    import pytz
    from datetime import datetime, timedelta
    
    # Obtener la fecha y hora actual en la zona horaria de Colombia
    colombia_tz = pytz.timezone('America/Bogota')
    ahora = timezone.now().astimezone(colombia_tz)
    fecha_actual = ahora.date()
    hora_actual = ahora.time()
    
    # Archivar reservas de fechas pasadas (todas del día completo)
    actualizadas_fecha = Reserva.objects.filter(
        fecha__lt=fecha_actual,
        estado__in=['pendiente', 'confirmada']
    ).update(estado='completada')
    
    # Archivar reservas del día actual cuya hora de fin ya pasó
    reservas_hoy = Reserva.objects.filter(
        fecha=fecha_actual,
        estado__in=['pendiente', 'confirmada']
    )
    
    actualizadas_hora = 0
    for reserva in reservas_hoy:
        # Convertir hora_fin a objeto time para comparar
        hora_fin_str = reserva.hora_fin
        hora_fin = datetime.strptime(hora_fin_str, '%H:%M').time()
        
        # Si la hora de fin ya pasó, marcar como completada
        if hora_fin < hora_actual:
            reserva.estado = 'completada'
            reserva.save()
            actualizadas_hora += 1
    
    return actualizadas_fecha + actualizadas_hora


def home(request):
    # Archivar automáticamente reservas vencidas
    archivar_reservas_vencidas()
    
    canchas = Cancha.objects.filter(activa=True)
    
    # Agregar información de reservas para cada cancha
    for cancha in canchas:
        cancha.num_reservas_activas = Reserva.objects.filter(
            cancha=cancha,
            estado__in=['pendiente', 'confirmada']
        ).count()
    
    return render(request, 'canchas/home.html', {'canchas': canchas})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'canchas/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'canchas/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('home')


@login_required
def lista_canchas(request):
    # Archivar automáticamente reservas vencidas
    archivar_reservas_vencidas()
    
    canchas = Cancha.objects.filter(activa=True)
    
    # Agregar información de reservas para cada cancha
    for cancha in canchas:
        cancha.num_reservas_activas = Reserva.objects.filter(
            cancha=cancha,
            estado__in=['pendiente', 'confirmada']
        ).count()
    
    return render(request, 'canchas/lista_canchas.html', {'canchas': canchas})


@login_required
def reservar_cancha(request, cancha_id):
    # Archivar automáticamente reservas vencidas
    archivar_reservas_vencidas()
    
    cancha = get_object_or_404(Cancha, id=cancha_id, activa=True)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.cancha = cancha
            
            # Verificar si hay conflicto de horarios
            hora_inicio = int(reserva.hora_inicio.split(':')[0])
            hora_fin = int(reserva.hora_fin.split(':')[0])
            
            # Manejar medianoche
            if hora_fin == 0:
                hora_fin = 24
            
            # Buscar reservas que se traslapen en ese día
            reservas_dia = Reserva.objects.filter(
                cancha=cancha,
                fecha=reserva.fecha,
                estado__in=['pendiente', 'confirmada']
            )
            
            conflicto = False
            for r in reservas_dia:
                r_inicio = int(r.hora_inicio.split(':')[0])
                r_fin = int(r.hora_fin.split(':')[0])
                
                # Manejar medianoche
                if r_fin == 0:
                    r_fin = 24
                
                # Verificar si hay traslape de horarios
                if not (hora_fin <= r_inicio or hora_inicio >= r_fin):
                    conflicto = True
                    # Formatear la hora para mostrar
                    hora_fin_display = "12:00 AM" if r.hora_fin == "00:00" else r.hora_fin
                    hora_inicio_display = r.hora_inicio
                    messages.error(request, f'Hay un conflicto de horario. La cancha ya está reservada de {hora_inicio_display} a {hora_fin_display}.')
                    break
            
            if not conflicto:
                reserva.save()
                duracion = hora_fin - hora_inicio
                messages.success(request, f'¡Reserva realizada con éxito! Has reservado {duracion} hora(s).')
                return redirect('mis_reservas')
    else:
        form = ReservaForm()
    
    # Obtener solo reservas futuras (no mostrar las que ya pasaron)
    from django.utils import timezone
    hoy = timezone.now().date()
    
    reservas_existentes = Reserva.objects.filter(
        cancha=cancha,
        fecha__gte=hoy,  # Solo fechas >= hoy
        estado__in=['pendiente', 'confirmada']
    ).order_by('fecha', 'hora_inicio')
    
    return render(request, 'canchas/reservar.html', {
        'form': form, 
        'cancha': cancha,
        'reservas_existentes': reservas_existentes
    })


@login_required
def mis_reservas(request):
    # Archivar automáticamente reservas vencidas
    archivar_reservas_vencidas()
    
    # Obtener todas las reservas del usuario
    reservas = Reserva.objects.filter(usuario=request.user)
    
    # Separar por estado
    reservas_activas = reservas.filter(estado__in=['pendiente', 'confirmada'])
    reservas_completadas = reservas.filter(estado='completada')
    reservas_canceladas = reservas.filter(estado='cancelada')
    reservas_archivadas = reservas.filter(estado='archivada')
    
    context = {
        'reservas': reservas,
        'reservas_activas': reservas_activas,
        'reservas_completadas': reservas_completadas,
        'reservas_canceladas': reservas_canceladas,
        'reservas_archivadas': reservas_archivadas,
    }
    
    return render(request, 'canchas/mis_reservas.html', context)


@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    
    if reserva.estado != 'cancelada':
        reserva.estado = 'cancelada'
        reserva.save()
        messages.success(request, 'Reserva cancelada exitosamente.')
    else:
        messages.info(request, 'Esta reserva ya estaba cancelada.')
    
    return redirect('mis_reservas')
