"""
Comando para archivar reservas vencidas automáticamente.
Uso: python manage.py archivar_reservas
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from canchas.models import Reserva


class Command(BaseCommand):
    help = 'Archiva (marca como completadas) las reservas cuya fecha ya pasó'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Muestra qué reservas se archivarían sin modificar la base de datos',
        )

    def handle(self, *args, **options):
        hoy = timezone.now().date()
        dry_run = options['dry_run']
        
        # Buscar reservas vencidas que aún están activas
        reservas_vencidas = Reserva.objects.filter(
            fecha__lt=hoy,
            estado__in=['pendiente', 'confirmada']
        )
        
        total = reservas_vencidas.count()
        
        if total == 0:
            self.stdout.write(
                self.style.SUCCESS('No hay reservas vencidas para archivar.')
            )
            return
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(f'[DRY RUN] Se archivarían {total} reservas:')
            )
            for reserva in reservas_vencidas:
                self.stdout.write(
                    f'  - {reserva.usuario.username}: {reserva.cancha.nombre} '
                    f'({reserva.fecha})'
                )
        else:
            # Archivar las reservas
            reservas_actualizadas = reservas_vencidas.update(estado='completada')
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Se archivaron {reservas_actualizadas} reservas vencidas.'
                )
            )
            
            # Mostrar detalles
            self.stdout.write('\nReservas archivadas:')
            for reserva in reservas_vencidas:
                self.stdout.write(
                    f'  - {reserva.usuario.username}: {reserva.cancha.nombre} '
                    f'({reserva.fecha})'
                )
