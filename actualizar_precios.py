"""
Script para actualizar los precios de las canchas según su tipo
Ejecutar con: python actualizar_precios.py
"""

import os
import django
import re

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from canchas.models import Cancha

# Diccionario de precios por tipo de cancha
PRECIOS = {
    '5': 80000,   # 5 vs 5
    '6': 100000,  # 6 vs 6
    '8': 150000,  # 8 vs 8
    '11': 250000, # 11 vs 11
}

# Configuración manual por nombre de cancha (si no se detecta automáticamente)
CONFIGURACION_MANUAL = {
    'johan cruyff': '6',
    'cruyff': '6',
    'ronaldo nazario': '5',
    'nazario': '5',
    'ronaldinho': '6',
    'pelé': '8',
    'pele': '8',
    'diego maradona': '11',
    'maradona': '11',
}

def detectar_tipo_cancha(cancha):
    """Detecta el tipo de cancha (5, 6, 8 o 11) desde nombre o descripción"""
    texto = f"{cancha.nombre} {cancha.descripcion}".lower()
    
    # Buscar patrones como "5 vs 5", "6vs6", "5v5", etc.
    patrones = [
        r'11\s*(?:vs|v)\s*11',  # 11 vs 11 (primero porque 1 podría confundirse)
        r'8\s*(?:vs|v)\s*8',    # 8 vs 8
        r'6\s*(?:vs|v)\s*6',    # 6 vs 6
        r'5\s*(?:vs|v)\s*5',    # 5 vs 5
    ]
    
    for patron in patrones:
        if re.search(patron, texto):
            numero = re.search(r'(\d+)', patron).group(1)
            return numero
    
    # Buscar configuración manual por nombre
    nombre_limpio = cancha.nombre.lower().strip().strip('"')
    for clave, tipo in CONFIGURACION_MANUAL.items():
        if clave in nombre_limpio:
            return tipo
    
    return None

def actualizar_precios():
    """Actualiza los precios de las canchas basándose en su nombre o descripción"""
    canchas = Cancha.objects.all()
    
    if not canchas.exists():
        print("❌ No hay canchas en la base de datos.")
        print("💡 Crea las canchas desde el admin: http://127.0.0.1:8000/admin/")
        return
    
    print("\n" + "="*60)
    print("📊 ACTUALIZANDO PRECIOS DE CANCHAS")
    print("="*60 + "\n")
    
    actualizadas = 0
    no_detectadas = []
    
    for cancha in canchas:
        precio_anterior = cancha.precio_por_hora
        tipo_numero = detectar_tipo_cancha(cancha)
        
        if tipo_numero and tipo_numero in PRECIOS:
            cancha.precio_por_hora = PRECIOS[tipo_numero]
            cancha.save()
            actualizadas += 1
            
            tipo_texto = f"{tipo_numero} vs {tipo_numero}"
            print(f"✅ {cancha.nombre} ({tipo_texto})")
            print(f"   ├─ Precio anterior: ${precio_anterior:,.0f}")
            print(f"   └─ Precio nuevo: ${cancha.precio_por_hora:,.0f}\n")
        else:
            no_detectadas.append(cancha)
            print(f"⚠️  {cancha.nombre}")
            print(f"   ├─ Descripción: {cancha.descripcion[:50]}...")
            print(f"   └─ No se pudo detectar el tipo. Precio actual: ${precio_anterior:,.0f}\n")
    
    print("="*60)
    print(f"✨ Actualización completada: {actualizadas}/{canchas.count()} canchas")
    print("="*60 + "\n")
    
    if no_detectadas:
        print("⚠️  CANCHAS NO DETECTADAS:")
        print("-"*60)
        for cancha in no_detectadas:
            print(f"  - {cancha.nombre}")
        print("-"*60 + "\n")
    
    print("📋 TABLA DE PRECIOS:")
    print("-"*60)
    print("  Tipo de Cancha  │  Precio por Hora")
    print("-"*60)
    print(f"  5 vs 5          │  $ 80.000")
    print(f"  6 vs 6          │  $100.000")
    print(f"  8 vs 8          │  $150.000")
    print(f"  11 vs 11        │  $250.000")
    print("-"*60 + "\n")

if __name__ == '__main__':
    try:
        actualizar_precios()
    except Exception as e:
        print(f"\n❌ Error: {e}")
