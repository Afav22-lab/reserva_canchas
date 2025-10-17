# 🚀 Instalación Rápida

Este proyecto **incluye la base de datos** con datos de prueba, así que puedes ejecutarlo inmediatamente.

---

## 📦 Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/Afav22-lab/reserva_canchas.git
cd reserva_canchas
```

---

## 🐍 Paso 2: Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📚 Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## ✅ Paso 4: ¡Ejecutar el Servidor!

```bash
python manage.py runserver
```

---

## 🌐 Paso 5: Abrir en el Navegador

Abre tu navegador en:
```
http://127.0.0.1:8000/
```

---

## 🔑 Credenciales de Prueba

**Administrador:**
- Usuario: (debes crear uno con `python manage.py createsuperuser`)
- Panel admin: http://127.0.0.1:8000/admin/

**Usuario Regular:**
- Puedes registrarte en: http://127.0.0.1:8000/registro/

---

## 📋 ¿Qué Incluye?

✅ **Base de datos (db.sqlite3)** - Con estructura completa
✅ **Migraciones** - Aplicadas y listas
✅ **Código fuente** - Todo el proyecto Django
✅ **Templates HTML** - Con Bootstrap 5
✅ **CSS personalizado** - Estilos y animaciones
✅ **requirements.txt** - Todas las dependencias

---

## 🎯 Comandos Útiles

### Crear superusuario (admin):
```bash
python manage.py createsuperuser
```

### Ver canchas en admin:
```
http://127.0.0.1:8000/admin/
```

### Resetear base de datos (si necesitas):
```bash
# Elimina db.sqlite3
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Crea una nueva
python manage.py migrate
python manage.py createsuperuser
```

---

## 📁 Estructura del Proyecto

```
reserva_canchas/
├── canchas/              # App principal
│   ├── models.py         # Modelos (Cancha, Reserva)
│   ├── views.py          # Vistas
│   ├── forms.py          # Formularios
│   ├── urls.py           # URLs
│   └── templates/        # Plantillas HTML
├── config/               # Configuración Django
├── static/               # Archivos estáticos (CSS)
├── db.sqlite3           # Base de datos ✅
├── manage.py            # Comando Django
└── requirements.txt     # Dependencias
```

---

## 🔧 Dependencias

- **Django 5.2.7** - Framework web
- **Pillow 11.1.0** - Manejo de imágenes
- **tzdata 2024.2** - Zonas horarias

---

## ⚠️ Nota Importante

La base de datos incluida es **solo para desarrollo/demostración**.

**En producción:**
- Usa PostgreSQL o MySQL
- No incluyas db.sqlite3 en Git
- Usa variables de entorno para credenciales

---

## 🆘 Solución de Problemas

### Error: "No module named 'django'"
```bash
# Asegúrate de activar el entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"
```bash
# Usa otro puerto
python manage.py runserver 8001
```

### Error: Base de datos bloqueada
```bash
# Cierra otros procesos que usen db.sqlite3
# O elimina el archivo db.sqlite3-journal si existe
```

---

## 🎨 Características del Sistema

- ✅ Registro e inicio de sesión de usuarios
- ✅ Listado de canchas disponibles
- ✅ Sistema de reservas por fecha
- ✅ Visualización de reservas propias
- ✅ Cancelación de reservas
- ✅ Archivado automático de reservas vencidas
- ✅ Panel de administración completo
- ✅ Diseño responsive con Bootstrap 5
- ✅ Fondo animado (GIF de fútbol)

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que el entorno virtual esté activado
2. Asegúrate de tener Python 3.8+
3. Revisa que todas las dependencias estén instaladas
4. Consulta el README.md para más detalles

---

**¡Listo para usar en menos de 5 minutos!** ⚡

Fecha: 16/10/2025
