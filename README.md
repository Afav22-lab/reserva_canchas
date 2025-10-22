# Sistema de Reserva de Canchas Sintéticas

Sistema web completo desarrollado en Django para la gestión y reserva de canchas deportivas con sistema de horarios.


### Para Usuarios:
- Sistema de autenticación (Login/Registro)
- Visualización de canchas disponibles con imágenes profesionales
- **Sistema de reservas por horarios (8:00 AM - 12:00 AM)**
- Selección de múltiples horas consecutivas (1-16 horas)
- Detección automática de conflictos de horarios
- Visualización de reservas propias organizadas por estado
- Cancelación de reservas
- Solo visualiza reservas futuras (no historial)
- Interfaz moderna y responsive con Bootstrap 5
- Fondo animado con GIF de fútbol

### Para Administradores:
- Panel de administración completo
- Gestión de canchas y reservas
- **Historial de reservas pasadas**
- Acción para archivar reservas vencidas
- Visualización de horarios y duración de reservas
- Panel simplificado (sin grupos, sin acciones recientes)
- Sistema de estados: Pendiente, Confirmada, Cancelada, Completada

##  Requisitos

- Python 3.8 o superior
- Django 5.2.7
- Pillow 11.1.0
- tzdata 2024.2

## Instalación

### 1. Activar el entorno virtual (si no está activado)

**Windows:**
```bash
.\venv\Scripts\activate
```


### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear las migraciones de la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear un superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu cuenta de administrador.

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El sistema estará disponible en: http://127.0.0.1:8000/

##  Uso del Sistema

### Para Administradores

1. **Accede al panel de administración:** http://127.0.0.1:8000/admin/
2. **Inicia sesión** con tu cuenta de superusuario
3. **Gestiona canchas:**
   - Crea nuevas canchas
   - Activa/desactiva canchas
   - Edita información
4. **Gestiona reservas:**
   - Ve todas las reservas activas
   - Accede al **Historial de Reservas Pasadas** (botón en la parte superior)
   - Archiva reservas vencidas manualmente
5. **Gestiona usuarios:**
   - Crea, edita o elimina usuarios
   - Asigna permisos de administrador

### Para Usuarios

1. **Regístrate** en el sistema desde la página principal
2. **Inicia sesión** con tu cuenta
3. **Explora las canchas disponibles**
4. **Reserva una cancha:**
   - Selecciona la fecha deseada
   - Elige hora de inicio (8:00 AM - 11:00 PM)
   - Elige hora de fin (9:00 AM - 12:00 AM)
   - El sistema valida conflictos automáticamente
5. **Visualiza tus reservas** en "Mis Reservas":
   - **Activas:** Reservas confirmadas y pendientes
   - **Completadas:** Reservas que ya pasaron
   - **Canceladas:** Reservas que cancelaste
6. **Cancela reservas** si es necesario

##  Sistema de Horarios

### Horarios Disponibles
- **Inicio:** 8:00 AM - 11:00 PM
- **Fin:** 9:00 AM - 12:00 AM (medianoche)
- **Duración:** 1 a 16 horas consecutivas

### Validaciones Automáticas
- No permite fechas pasadas
- Detecta conflictos de horarios
- Valida que hora fin > hora inicio
- Limita duración máxima
- Solo muestra reservas futuras a usuarios

## Estructura del Proyecto

```
reserva_canchas/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3                # Base de datos (incluida para desarrollo)
├── config/                   # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── canchas/                  # Aplicación principal
│   ├── models.py            # Modelos (Cancha, Reserva)
│   ├── views.py             # Vistas y lógica de negocio
│   ├── forms.py             # Formularios de reserva y registro
│   ├── admin.py             # Configuración del panel admin
│   ├── urls.py              # URLs de la aplicación
│   ├── management/          # Comandos personalizados
│   │   └── commands/
│   │       └── archivar_reservas.py
│   └── templates/           # Plantillas HTML
│       ├── canchas/
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── login.html
│       │   ├── registro.html
│       │   ├── lista_canchas.html
│       │   ├── reservar.html
│       │   └── mis_reservas.html
│       └── admin/
│           ├── index.html   # Personalización del admin
│           └── canchas/
│               └── reserva/
│                   ├── change_list.html
│                   └── historial.html
└── static/                   # Archivos estáticos
    └── css/
        └── styles.css       # Estilos personalizados + GIF de fondo
```

## Modelos de Datos

### Cancha
- **nombre**: CharField - Nombre de la cancha
- **descripcion**: TextField - Descripción detallada
- **precio_hora**: DecimalField - Precio por hora de uso
- **imagen**: ImageField - Imagen de la cancha (opcional)
- **disponible**: BooleanField - Estado de disponibilidad

### Reserva
- **usuario**: ForeignKey(User) - Usuario que realiza la reserva
- **cancha**: ForeignKey(Cancha) - Cancha reservada
- **fecha**: DateField - Fecha de la reserva
- **hora_inicio**: CharField - Hora de inicio (08:00 - 23:00)
- **hora_fin**: CharField - Hora de fin (09:00 - 00:00)
- **fecha_creacion**: DateTimeField - Timestamp de creación (solo admin)
- **estado**: CharField - Estados: pendiente, confirmada, completada, cancelada, archivada

**Propiedades:**
- `esta_vencida`: Indica si la reserva ya pasó su fecha
- `duracion_horas`: Calcula las horas totales de la reserva (1-16 horas)

**Validaciones:**
- ✅ La hora de fin debe ser posterior a la hora de inicio
- ✅ Duración máxima de 16 horas
- ✅ No pueden existir reservas con horarios superpuestos para la misma cancha
- ✅ Manejo especial de medianoche (00:00)

## Diseño y Estética

- **Imágenes profesionales:** Unsplash CDN (1200x600 para hero, 400x250 para cards)
- **Fondo animado:** GIF de futbolistas (Giphy CDN)
- **Framework CSS:** Bootstrap 5.3.0 + Bootstrap Icons
- **Estilo:** Tarjetas con sombras, gradientes, diseño moderno y responsivo
- **Paleta de colores:** Verde profesional con acentos en badges de estado

## Tecnologías Utilizadas

- **Backend:** Django 5.2.7
- **Frontend:** HTML5, CSS3, Bootstrap 5.3.0, Bootstrap Icons
- **Base de datos:** SQLite (desarrollo)
- **CDN:** Unsplash (imágenes), Giphy (GIF de fondo)
- **Control de versiones:** Git + GitHub

## Solución de Problemas

### El servidor no inicia
```cmd
python manage.py runserver
```
Si el puerto 8000 está ocupado, usa: `python manage.py runserver 8080`

### Error al hacer migraciones
```cmd
python manage.py makemigrations
python manage.py migrate
```

### Olvidé la contraseña del admin
```cmd
python manage.py createsuperuser
```
Crea un nuevo superusuario con credenciales diferentes.

### Las imágenes no cargan
Verifica que las URLs de Unsplash/Giphy sean accesibles desde tu navegador.

## 📝 Notas Adicionales

- La base de datos `db.sqlite3` está incluida en el repositorio para facilitar el desarrollo
- El sistema archiva automáticamente reservas vencidas
- Los usuarios solo ven reservas futuras en la interfaz principal
- Los administradores tienen acceso completo al historial mediante el botón "Ver Historial"

## Soporte

Para cualquier problema o sugerencia, abre un issue en el repositorio de GitHub:
**[github.com/Afav22-lab/reserva_canchas](https://github.com/Afav22-lab/reserva_canchas)**

---

Desarrollado usando Django | Sistema de Reservas de Canchas v2.0
