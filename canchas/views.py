from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Cancha, Reserva
from .forms import RegistroForm, ReservaForm


def home(request):
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
    cancha = get_object_or_404(Cancha, id=cancha_id, activa=True)
    
    # Obtener fechas ya reservadas para esta cancha
    fechas_reservadas = Reserva.objects.filter(
        cancha=cancha,
        estado__in=['pendiente', 'confirmada']
    ).values_list('fecha', flat=True)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.cancha = cancha
            
            # Verificar si ya existe una reserva para esa cancha en esa fecha
            reserva_existente = Reserva.objects.filter(
                cancha=cancha,
                fecha=reserva.fecha,
                estado__in=['pendiente', 'confirmada']
            ).exists()
            
            if reserva_existente:
                messages.error(request, 'Esta cancha ya está reservada para esa fecha.')
                return render(request, 'canchas/reservar.html', {
                    'form': form, 
                    'cancha': cancha,
                    'fechas_reservadas': list(fechas_reservadas)
                })
            
            reserva.save()
            messages.success(request, '¡Reserva realizada con éxito!')
            return redirect('mis_reservas')
    else:
        form = ReservaForm()
    
    return render(request, 'canchas/reservar.html', {
        'form': form, 
        'cancha': cancha,
        'fechas_reservadas': list(fechas_reservadas)
    })


@login_required
def mis_reservas(request):
    # Archivar automáticamente reservas vencidas del usuario actual
    from django.utils import timezone
    hoy = timezone.now().date()
    
    Reserva.objects.filter(
        usuario=request.user,
        fecha__lt=hoy,
        estado__in=['pendiente', 'confirmada']
    ).update(estado='completada')
    
    # Obtener todas las reservas del usuario
    reservas = Reserva.objects.filter(usuario=request.user)
    
    # Separar por estado
    reservas_activas = reservas.filter(estado__in=['pendiente', 'confirmada'])
    reservas_completadas = reservas.filter(estado='completada')
    reservas_canceladas = reservas.filter(estado='cancelada')
    
    context = {
        'reservas': reservas,
        'reservas_activas': reservas_activas,
        'reservas_completadas': reservas_completadas,
        'reservas_canceladas': reservas_canceladas,
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
