"""
Script para probar el sistema de archivado por hora
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.utils import timezone
from canchas.models import Reserva
import pytz
from datetime import datetime

print("═" * 70)
print("PRUEBA DEL SISTEMA DE ARCHIVADO POR HORA")
print("═" * 70)

# Obtener hora actual en Colombia
colombia_tz = pytz.timezone('America/Bogota')
ahora = timezone.now().astimezone(colombia_tz)
fecha_actual = ahora.date()
hora_actual = ahora.time()

print(f"\n📅 Fecha actual: {fecha_actual}")
print(f"⏰ Hora actual:  {hora_actual.strftime('%H:%M:%S')}")

print("\n" + "─" * 70)
print("RESERVAS ACTIVAS DEL DÍA DE HOY:")
print("─" * 70)

reservas_hoy = Reserva.objects.filter(
    fecha=fecha_actual,
    estado__in=['pendiente', 'confirmada']
).order_by('hora_inicio')

if reservas_hoy:
    for reserva in reservas_hoy:
        hora_fin = datetime.strptime(reserva.hora_fin, '%H:%M').time()
        
        # Determinar si ya terminó
        if hora_fin < hora_actual:
            status = "❌ TERMINADA (debería pasar a completada)"
        elif reserva.hora_inicio <= hora_actual.strftime('%H:%M') < reserva.hora_fin:
            status = "🟢 EN CURSO"
        else:
            status = "⏳ FUTURA"
        
        print(f"\n{reserva.cancha.nombre}")
        print(f"  Usuario: {reserva.usuario.username}")
        print(f"  Horario: {reserva.hora_inicio} - {reserva.hora_fin}")
        print(f"  Estado actual: {reserva.estado.upper()}")
        print(f"  {status}")
else:
    print("\n  No hay reservas activas para hoy")

print("\n" + "─" * 70)
print("RESERVAS COMPLETADAS DEL DÍA DE HOY:")
print("─" * 70)

reservas_completadas = Reserva.objects.filter(
    fecha=fecha_actual,
    estado='completada'
).order_by('hora_inicio')

if reservas_completadas:
    for reserva in reservas_completadas:
        print(f"\n{reserva.cancha.nombre}")
        print(f"  Usuario: {reserva.usuario.username}")
        print(f"  Horario: {reserva.hora_inicio} - {reserva.hora_fin}")
        print(f"  ✅ COMPLETADA")
else:
    print("\n  No hay reservas completadas para hoy aún")

print("\n" + "═" * 70)
print("💡 TIP: Recarga cualquier página del sistema para que se ejecute")
print("   el archivado automático y las reservas terminadas pasen a completadas")
print("═" * 70)
