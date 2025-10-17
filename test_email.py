"""
Script de prueba para verificar conexión con Gmail
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("═" * 60)
print("PRUEBA DE ENVÍO DE EMAIL")
print("═" * 60)
print(f"\nConfigu EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
print(f"EMAIL_HOST_PASSWORD: {'*' * len(settings.EMAIL_HOST_PASSWORD)}")
print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")

print("\n" + "═" * 60)
print("Enviando email de prueba...")
print("═" * 60)

try:
    send_mail(
        subject='Prueba de Email - Sistema de Reservas',
        message='Este es un email de prueba desde Django.\n\n¡Si recibes este mensaje, la configuración funciona! 🎉',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_HOST_USER],  # Te envía a ti mismo
        fail_silently=False,
    )
    print("\n✅ EMAIL ENVIADO EXITOSAMENTE")
    print(f"📧 Revisa tu bandeja: {settings.EMAIL_HOST_USER}")
    print("💡 También revisa la carpeta de SPAM")
    
except Exception as e:
    print(f"\n❌ ERROR AL ENVIAR: {e}")
    print("\n🔧 Posibles soluciones:")
    print("1. Verifica que la contraseña de aplicación sea correcta")
    print("2. Asegúrate de tener verificación en 2 pasos activa en Google")
    print("3. Genera una nueva contraseña de aplicación")
    print("4. Verifica tu conexión a internet")

print("\n" + "═" * 60)
