# 🚀 Guía para Subir tu Proyecto a GitHub

## ✅ Paso 1: Git Inicializado (Completado)

Ya tienes Git configurado en tu proyecto:
- ✅ Repositorio inicializado
- ✅ Usuario configurado: PIPE
- ✅ Email configurado: isnardo.alfonso@correo.uis.edu.co
- ✅ Primer commit realizado (33 archivos)

---

## 📋 Paso 2: Crear Repositorio en GitHub

### 2.1 Ve a GitHub:
1. Abre tu navegador y ve a: **https://github.com**
2. Inicia sesión con tu cuenta (o crea una si no tienes)

### 2.2 Crear Nuevo Repositorio:
1. Haz clic en el **+** (esquina superior derecha)
2. Selecciona **"New repository"**

### 2.3 Configurar el Repositorio:
```
Repository name: reserva-canchas
Description: Sistema de reserva de canchas deportivas con Django
Visibility: ✓ Public (o Private si lo prefieres)

❌ NO marques estas opciones:
   □ Add a README file
   □ Add .gitignore
   □ Choose a license
   
(Ya las tienes en tu proyecto)
```

4. Haz clic en **"Create repository"**

---

## 🔗 Paso 3: Conectar y Subir

GitHub te mostrará varias opciones. Usa esta:

### Opción: "…or push an existing repository from the command line"

Copia los comandos que GitHub te muestre (serán similares a estos):

```bash
git remote add origin https://github.com/TU-USUARIO/reserva-canchas.git
git branch -M main
git push -u origin main
```

### Ejecutar en tu terminal:

**Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub:**

```bash
git remote add origin https://github.com/TU-USUARIO/reserva-canchas.git
```

Luego:

```bash
git branch -M main
```

Finalmente:

```bash
git push -u origin main
```

---

## 🔐 Autenticación

GitHub te pedirá autenticación. Tienes 2 opciones:

### Opción A: Token Personal (Recomendado)

1. Ve a: **https://github.com/settings/tokens**
2. Clic en **"Generate new token"** → **"Generate new token (classic)"**
3. Configura:
   - Note: `Token para reserva-canchas`
   - Expiration: `90 days` (o lo que prefieras)
   - Scopes: Marca **✓ repo** (todos los permisos de repositorio)
4. Clic en **"Generate token"**
5. **COPIA EL TOKEN** (solo se muestra una vez)
6. Cuando Git te pida password, pega el **token** (no tu contraseña)

### Opción B: GitHub CLI

```bash
# Instalar GitHub CLI (si no lo tienes)
winget install GitHub.cli

# Autenticarte
gh auth login
```

---

## 📤 Comandos Completos (Copiar y Ejecutar)

Una vez que tengas el repositorio creado en GitHub, ejecuta estos comandos **reemplazando TU-USUARIO**:

```bash
# 1. Conectar con GitHub (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/reserva-canchas.git

# 2. Renombrar rama a main
git branch -M main

# 3. Subir el código
git push -u origin main
```

**Cuando pida usuario/contraseña:**
- Username: Tu usuario de GitHub
- Password: **El token personal** (no tu contraseña)

---

## ✅ Verificar que se Subió

1. Ve a: `https://github.com/TU-USUARIO/reserva-canchas`
2. Deberías ver todos tus archivos
3. El README.md se mostrará en la página principal

---

## 🔄 Comandos Útiles para el Futuro

### Hacer cambios y subirlos:

```bash
# 1. Ver qué archivos cambiaron
git status

# 2. Agregar archivos modificados
git add .

# 3. Hacer commit
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub
git push
```

### Ver historial:

```bash
git log --oneline
```

### Ver repositorio remoto:

```bash
git remote -v
```

---

## 📝 Ejemplo de URL de tu Repositorio

Si tu usuario de GitHub es `pipe123`, tu repositorio estará en:

```
https://github.com/pipe123/reserva-canchas
```

---

## ⚠️ Notas Importantes

1. **Base de datos NO se sube** (está en .gitignore)
   - Esto es correcto por seguridad
   - Cada persona que clone debe crear su propia BD

2. **Archivos excluidos por .gitignore:**
   - `db.sqlite3` (base de datos)
   - `__pycache__/` (archivos compilados)
   - `venv/` (entorno virtual)
   - `.vscode/` (configuración del editor)

3. **El archivo `requirements.txt` SÍ se sube**
   - Permite a otros instalar las dependencias
   - Con: `pip install -r requirements.txt`

---

## 🆘 Solución de Problemas

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TU-USUARIO/reserva-canchas.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error de autenticación
- Asegúrate de usar el **token personal**, no tu contraseña
- Genera un nuevo token si es necesario

---

## 📱 Próximos Pasos Después de Subir

1. ✅ Agrega un archivo LICENSE (recomendado: MIT)
2. ✅ Mejora el README.md con capturas de pantalla
3. ✅ Crea un archivo CONTRIBUTING.md si esperas contribuciones
4. ✅ Activa GitHub Actions para CI/CD (opcional)

---

## 🎯 Comando Rápido (Todo en Uno)

**Una vez creado el repositorio en GitHub:**

```bash
git remote add origin https://github.com/TU-USUARIO/reserva-canchas.git && git branch -M main && git push -u origin main
```

Reemplaza `TU-USUARIO` con tu usuario real de GitHub.

---

**Estado actual:** ✅ Listo para subir a GitHub
**Siguiente paso:** Crear repositorio en github.com y ejecutar comandos de conexión

---

Fecha: 16/10/2025
