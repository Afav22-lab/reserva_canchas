# Sistema de Reserva de Canchas Sintéticas

Sistema web desarrollado en Django para la gestión y reserva de canchas sintéticas.

## Características

- ✅ Sistema de autenticación (Login/Registro)
- ✅ Panel de administración para gestionar canchas
- ✅ Los usuarios pueden ver canchas disponibles
- ✅ Sistema de reservas simple (solo fecha)
- ✅ Visualización de reservas del usuario
- ✅ Cancelación de reservas
- ✅ Interfaz responsive con Bootstrap 5

## Requisitos

- Python 3.8 o superior
- Django 4.2.7
- Pillow 10.1.0

## Instalación

### 1. Activar el entorno virtual (si no está activado)

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
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

## Uso

### Para Administradores

1. Accede al panel de administración: http://127.0.0.1:8000/admin/
2. Inicia sesión con tu cuenta de superusuario
3. Crea canchas desde el panel de administración
4. Gestiona las reservas de los usuarios

### Para Usuarios

1. Regístrate en el sistema desde la página principal
2. Inicia sesión con tu cuenta
3. Explora las canchas disponibles
4. Selecciona una cancha y elige la fecha para reservar
5. Visualiza tus reservas en "Mis Reservas"
6. Cancela reservas si es necesario

## Estructura del Proyecto

```
reserva_canchas/
├── manage.py
├── requirements.txt
├── README.md
├── config/                    # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── canchas/                   # Aplicación principal
│   ├── models.py             # Modelos (Cancha, Reserva)
│   ├── views.py              # Vistas
│   ├── forms.py              # Formularios
│   ├── admin.py              # Configuración del admin
│   ├── urls.py               # URLs de la app
│   └── templates/            # Plantillas HTML
│       └── canchas/
│           ├── base.html
│           ├── home.html
│           ├── login.html
│           ├── registro.html
│           ├── lista_canchas.html
│           ├── reservar.html
│           └── mis_reservas.html
└── static/                    # Archivos estáticos
    └── css/
        └── styles.css
```

## Modelos

### Cancha
- nombre: Nombre de la cancha
- descripcion: Descripción de la cancha
- activa: Estado de la cancha (activa/inactiva)
- fecha_creacion: Fecha de creación

### Reserva
- usuario: Usuario que realiza la reserva
- cancha: Cancha reservada
- fecha: Fecha de la reserva
- estado: Estado (confirmada, pendiente, cancelada)
- fecha_reserva: Fecha en que se realizó la reserva
- notas: Notas adicionales (opcional)

## Funcionalidades Futuras (Opcionales)

- [ ] Sistema de horarios por cancha
- [ ] Notificaciones por email
- [ ] Sistema de pagos
- [ ] Calificaciones y comentarios
- [ ] Historial de reservas
- [ ] Reportes para administradores

## Tecnologías Utilizadas

- **Backend:** Django 4.2.7
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Base de datos:** SQLite (desarrollo)
- **Iconos:** Bootstrap Icons

## Soporte

Para cualquier problema o sugerencia, por favor contacta al desarrollador.

---

Desarrollado con ❤️ usando Django
