# ⏰ Sistema de Archivado Automático por Hora

## 🎯 ¿Cómo Funciona?

El sistema ahora archiva las reservas de manera inteligente, considerando tanto la **fecha** como la **hora** de finalización.

---

## 📅 Lógica de Archivado

### Antes (Solo por fecha):
- ❌ Reservas del 16/10 se archivaban al día siguiente (17/10)
- ❌ Una reserva de 10:00-11:00 del 17/10 seguía "activa" hasta el 18/10
- ❌ No consideraba la hora de finalización

### Ahora (Por fecha Y hora):
- ✅ Reservas de fechas pasadas → Completadas inmediatamente
- ✅ Reservas del día actual → Se evalúan por hora de fin
- ✅ Si la hora de fin ya pasó → Pasa a "Completada"

---

## 🔄 Ejemplos Prácticos

### Ejemplo 1: Fecha pasada
```
Fecha actual: 17/10/2025 14:30

Reserva:
- Fecha: 16/10/2025
- Hora: 10:00 - 11:00
- Estado: Confirmada

→ Resultado: Pasa a "Completada" (fecha pasada)
```

### Ejemplo 2: Hora ya pasó hoy
```
Fecha actual: 17/10/2025 14:30

Reserva:
- Fecha: 17/10/2025
- Hora: 10:00 - 11:00  ← La hora de fin (11:00) ya pasó
- Estado: Confirmada

→ Resultado: Pasa a "Completada" (hora de fin pasada)
```

### Ejemplo 3: Hora todavía no termina
```
Fecha actual: 17/10/2025 14:30

Reserva:
- Fecha: 17/10/2025
- Hora: 14:00 - 16:00  ← La hora de fin (16:00) aún no llega
- Estado: Confirmada

→ Resultado: Sigue "Activa" (aún en curso)
```

### Ejemplo 4: Reserva futura
```
Fecha actual: 17/10/2025 14:30

Reserva:
- Fecha: 17/10/2025
- Hora: 22:00 - 23:00  ← Hora futura del mismo día
- Estado: Confirmada

→ Resultado: Sigue "Activa" (reserva futura)
```

---

## 🕐 ¿Cuándo se Ejecuta?

El sistema verifica automáticamente en cada **carga de página**:

1. **Página principal** (`home`)
2. **Lista de canchas** (`lista_canchas`)
3. **Formulario de reserva** (`reservar_cancha`)
4. **Mis reservas** (`mis_reservas`)

---

## 💡 Ventajas del Nuevo Sistema

✅ **Más preciso**: Considera hora de finalización, no solo fecha
✅ **Tiempo real**: Las reservas pasan a completadas apenas terminan
✅ **Mejor UX**: Los usuarios ven el estado correcto inmediatamente
✅ **Automático**: No requiere tareas programadas ni CRON
✅ **Zona horaria**: Respeta la hora de Colombia (UTC-5)

---

## 🔍 Detalles Técnicos

### Función: `archivar_reservas_vencidas()`

**Ubicación:** `canchas/views.py`

**Proceso:**
1. Obtiene fecha y hora actual en timezone de Colombia
2. Archiva todas las reservas de fechas pasadas (completas)
3. Para reservas del día actual:
   - Itera cada una
   - Compara hora de fin con hora actual
   - Si hora_fin < hora_actual → Marca como completada

**Código clave:**
```python
# Obtener hora actual en Colombia
colombia_tz = pytz.timezone('America/Bogota')
ahora = timezone.now().astimezone(colombia_tz)
hora_actual = ahora.time()

# Comparar hora de fin
if hora_fin < hora_actual:
    reserva.estado = 'completada'
    reserva.save()
```

---

## 📊 Estados de Reservas

| Estado | Cuándo | Tab en "Mis Reservas" |
|--------|--------|----------------------|
| **Pendiente** | Reserva recién creada | 🟢 Activas |
| **Confirmada** | Admin la confirmó | 🟢 Activas |
| **Completada** | Hora de fin pasó | 🔵 Completadas |
| **Cancelada** | Usuario la canceló | 🟡 Canceladas |

---

## ⚠️ Consideraciones

### Rendimiento:
- Para reservas de fechas pasadas: `UPDATE` masivo (rápido)
- Para reservas del día actual: Itera una por una (evalúa hora)
- En días normales: Pocas reservas del día actual → Rápido
- En días con muchas reservas: Puede tomar algunos segundos

### Optimización futura (si es necesario):
Si tienes muchas reservas simultáneas del mismo día, puedes optimizar usando:
```python
# Crear campo calculado con datetime completo
reserva.hora_fin_datetime = datetime.combine(reserva.fecha, reserva.hora_fin)

# Filtrar directo con query
Reserva.objects.filter(
    hora_fin_datetime__lt=ahora
).update(estado='completada')
```

---

## 🧪 Cómo Probarlo

### Prueba 1: Reserva que ya terminó
1. Crea una reserva para HOY de 10:00 a 11:00
2. Espera a que pasen las 11:00
3. Recarga "Mis Reservas"
4. ✅ Debería estar en tab "Completadas"

### Prueba 2: Reserva en curso
1. Crea una reserva para HOY que aún no termine
   - Ejemplo: Si son las 14:30, crea de 14:00 a 16:00
2. Ve a "Mis Reservas"
3. ✅ Debería estar en tab "Activas"

### Prueba 3: Reserva futura
1. Crea una reserva para HOY pero en el futuro
   - Ejemplo: Si son las 14:30, crea de 20:00 a 21:00
2. Ve a "Mis Reservas"
3. ✅ Debería estar en tab "Activas"

---

## 📝 Nota sobre el Admin

En el **panel de administración**, el admin puede usar la acción **"Archivar reservas vencidas y canceladas"** para:
- Archivar manualmente reservas vencidas
- Archivar reservas canceladas (cambia estado a 'archivada')

---

## 🎯 Resumen

**Antes:**
- Reserva del 17/10 de 10:00-11:00
- A las 14:00 del 17/10 → Aún "Activa" ❌

**Ahora:**
- Reserva del 17/10 de 10:00-11:00
- A las 11:01 del 17/10 → "Completada" ✅

**Resultado:** Sistema más preciso y actualizado en tiempo real 🚀

---

**Última actualización:** 17 de octubre de 2025  
**Sistema:** Reserva de Canchas v2.0
