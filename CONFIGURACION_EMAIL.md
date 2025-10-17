# 📧 Configuración de Recuperación de Contraseña

## 🎯 Sistema Implementado

Se ha agregado un sistema completo de recuperación de contraseña que permite a los usuarios restablecer su contraseña mediante un enlace enviado por correo electrónico.

---

## 🔧 Configuración Actual (Desarrollo)

### Modo de Prueba - Emails en Consola

Actualmente, el sistema está configurado para **mostrar los emails en la consola** (terminal donde corre el servidor). Esto es ideal para desarrollo y pruebas.

**Configuración en `settings.py`:**
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### ¿Cómo Funciona en Desarrollo?

1. Usuario solicita recuperación de contraseña
2. Django genera el email con el enlace
3. **El email se muestra en la terminal** donde está corriendo el servidor
4. Copias el enlace de la terminal
5. Lo pegas en el navegador
6. Usuario puede cambiar su contraseña

---

## 📧 Configuración para Producción (Emails Reales)

### Opción 1: Gmail (Recomendado para proyectos pequeños)

#### Paso 1: Crear una contraseña de aplicación

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Seguridad → Verificación en 2 pasos (actívala si no la tienes)
3. Contraseñas de aplicaciones → Genera una nueva
4. Guarda la contraseña generada (son 16 caracteres)

#### Paso 2: Configurar Django

En `settings.py`, **comenta** la línea de desarrollo y **descomenta/configura** estas líneas:

```python
# Comentar esta línea:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Descomentar y configurar estas líneas:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@gmail.com'  # Tu email de Gmail
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'  # La contraseña de aplicación de 16 dígitos
DEFAULT_FROM_EMAIL = 'Sistema de Reservas <tu-email@gmail.com>'
```

**⚠️ IMPORTANTE:** Nunca subas tu contraseña a Git. Usa variables de entorno.

---

### Opción 2: Outlook/Hotmail

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@outlook.com'
EMAIL_HOST_PASSWORD = 'tu-contraseña'
DEFAULT_FROM_EMAIL = 'Sistema de Reservas <tu-email@outlook.com>'
```

---

### Opción 3: SendGrid (Recomendado para producción profesional)

SendGrid ofrece 100 emails gratis al día.

1. Regístrate en: https://sendgrid.com/
2. Crea una API Key
3. Configura:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Literalmente la palabra "apikey"
EMAIL_HOST_PASSWORD = 'TU_API_KEY_DE_SENDGRID'
DEFAULT_FROM_EMAIL = 'Sistema de Reservas <noreply@tudominio.com>'
```

---

### Opción 4: Mailtrap (Solo para pruebas)

Mailtrap captura emails para pruebas sin enviarlos realmente.

1. Regístrate en: https://mailtrap.io/
2. Copia las credenciales SMTP
3. Configura:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'tu-username-mailtrap'
EMAIL_HOST_PASSWORD = 'tu-password-mailtrap'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Sistema de Reservas <test@test.com>'
```

---

## 🔐 Usar Variables de Entorno (Seguridad)

### Instalación

```bash
pip install python-decouple
```

Agrega a `requirements.txt`:
```
python-decouple==3.8
```

### Crear archivo `.env`

En la raíz del proyecto, crea un archivo `.env`:

```env
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-aplicación
```

### Configurar `settings.py`

```python
from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = f'Sistema de Reservas <{config("EMAIL_HOST_USER")}>'
```

### Agregar `.env` a `.gitignore`

```
# En .gitignore
.env
db.sqlite3
*.pyc
__pycache__/
media/
```

---

## 🎨 URLs del Sistema

Las siguientes URLs fueron agregadas:

| URL | Descripción |
|-----|-------------|
| `/password-reset/` | Solicitar recuperación de contraseña |
| `/password-reset/done/` | Confirmación de email enviado |
| `/password-reset-confirm/<uidb64>/<token>/` | Formulario para nueva contraseña |
| `/password-reset-complete/` | Confirmación de contraseña cambiada |

---

## 🧪 Cómo Probar en Desarrollo

### 1. Iniciar el servidor

```bash
python manage.py runserver
```

### 2. Ir a login

http://127.0.0.1:8000/login/

### 3. Click en "¿Olvidaste tu contraseña?"

### 4. Ingresar email registrado

**Importante:** El email debe existir en la base de datos.

### 5. Ver el email en la terminal

En la terminal verás algo como:

```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: Password reset on 127.0.0.1:8000
From: webmaster@localhost
To: usuario@ejemplo.com

You're receiving this email because you requested a password reset...

http://127.0.0.1:8000/password-reset-confirm/MQ/xxxxx-xxxxxxxxxxxxx/
```

### 6. Copiar el enlace

Copia el enlace que empieza con `http://127.0.0.1:8000/password-reset-confirm/...`

### 7. Pegar en el navegador

Abre el enlace en tu navegador y cambia la contraseña.

---

## ✅ Verificación del Sistema

### Checklist de Implementación:

- [x] URLs de recuperación agregadas
- [x] Plantilla: Solicitar recuperación (`password_reset.html`)
- [x] Plantilla: Email enviado (`password_reset_done.html`)
- [x] Plantilla: Formulario nueva contraseña (`password_reset_confirm.html`)
- [x] Plantilla: Confirmación final (`password_reset_complete.html`)
- [x] Enlace en página de login
- [x] Configuración de email en `settings.py`

---

## ❓ Preguntas Frecuentes

### ¿Por qué no veo el email?

**En desarrollo:** Los emails aparecen en la terminal donde corre `python manage.py runserver`

**En producción:** Revisa:
1. Credenciales SMTP correctas
2. Firewall no bloquea puerto 587
3. Email del remitente verificado
4. Límites de envío no excedidos

### ¿El enlace expira?

Sí, los enlaces expiran después de **24 horas** por razones de seguridad.

### ¿Puedo personalizar los emails?

Sí, crea plantillas personalizadas en:
- `templates/registration/password_reset_email.html`
- `templates/registration/password_reset_subject.txt`

### ¿Funciona sin email registrado?

Django no enviará email a cuentas no registradas, pero no muestra error por seguridad (para no revelar qué emails existen en el sistema).

---

## 🚀 Siguiente Paso

Para activar emails reales, sigue la sección **"Configuración para Producción"** y elige tu proveedor de email preferido (Gmail, SendGrid, etc.).

---

**Última actualización:** 17 de octubre de 2025  
**Sistema:** Reserva de Canchas v2.0
