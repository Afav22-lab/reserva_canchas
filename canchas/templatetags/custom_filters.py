from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='formato_precio')
def formato_precio(valor):
    """
    Formatea un número con separador de miles (punto) para pesos colombianos
    Ejemplo: 100000 -> 100.000
    """
    try:
        # Convertir a número si es string
        if isinstance(valor, str):
            valor = float(valor)
        
        # Convertir a entero para eliminar decimales
        valor_int = int(valor)
        
        # Formatear con separador de miles
        # En Python, {:,} usa coma, así que la reemplazamos por punto
        return f"{valor_int:,}".replace(',', '.')
    except (ValueError, TypeError):
        return valor
