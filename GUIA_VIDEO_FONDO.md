# 🎬 Video de Fondo en Página Principal

## ✅ ¡Video Implementado!

La página principal ahora tiene un video de fondo que se reproduce automáticamente, dándole un aspecto más moderno y dinámico.

---

## 🎥 Características del Video

- **Autoplay**: Se reproduce automáticamente al cargar la página
- **Muted**: Sin sonido (requerido por navegadores para autoplay)
- **Loop**: Se repite infinitamente
- **Responsive**: Se adapta a todos los tamaños de pantalla
- **Overlay oscuro**: Para mejor legibilidad del texto

---

## 🔧 Configuración Actual

### Videos Gratuitos Utilizados:
Los videos vienen de **Mixkit** (biblioteca gratuita):
- Video 1: Balón de fútbol en cancha
- Video 2: Campo de fútbol desde arriba

**CDN:** https://mixkit.co/free-stock-video/

---

## 📁 Usar Tu Propio Video

### Opción 1: Video Local (Recomendado)

1. **Coloca tu video** en la carpeta `media/videos/`:
   ```
   media/
   └── videos/
       └── cancha_video.mp4
   ```

2. **Actualiza el código** en `home.html`:
   ```html
   <video autoplay muted loop playsinline class="hero-video">
       <source src="{{ MEDIA_URL }}videos/cancha_video.mp4" type="video/mp4">
   </video>
   ```

### Opción 2: Video desde URL

Si tienes el video en un servidor:
```html
<video autoplay muted loop playsinline class="hero-video">
    <source src="https://tu-servidor.com/videos/cancha.mp4" type="video/mp4">
</video>
```

---

## 🎬 Fuentes de Videos Gratuitos

### 1. Mixkit (Actual)
- **URL:** https://mixkit.co/free-stock-video/
- **Licencia:** Gratis para uso comercial
- **Categoría:** Busca "soccer", "football", "sports field"

### 2. Pexels Videos
- **URL:** https://www.pexels.com/videos/
- **Licencia:** Gratis
- **Búsqueda:** "soccer field", "football pitch"

### 3. Pixabay Videos
- **URL:** https://pixabay.com/videos/
- **Licencia:** Gratis
- **Búsqueda:** "soccer", "stadium"

### 4. Coverr
- **URL:** https://coverr.co/
- **Licencia:** Gratis
- **Categoría:** Sports

---

## 📐 Especificaciones Recomendadas del Video

### Tamaño/Resolución:
- **Mínimo:** 1280x720 (HD)
- **Recomendado:** 1920x1080 (Full HD)
- **Formato:** 16:9 (horizontal)

### Duración:
- **Óptimo:** 10-30 segundos
- **Máximo:** 1 minuto
- Se reproduce en loop, así que no necesita ser muy largo

### Peso del Archivo:
- **Ideal:** 2-5 MB
- **Máximo:** 10 MB
- Videos más pesados tardan en cargar

### Formato:
- **Preferido:** MP4 (H.264)
- **Alternativo:** WebM
- MP4 tiene mejor compatibilidad

---

## 🛠️ Optimizar Tu Video

### Herramientas Online Gratuitas:

1. **Cloudconvert** - https://cloudconvert.com/
   - Convierte a MP4
   - Reduce tamaño
   - Cambia resolución

2. **Online Video Converter** - https://www.onlinevideoconverter.pro/
   - Comprime videos
   - Ajusta calidad

3. **HandBrake** (Descargable - Gratis)
   - https://handbrake.fr/
   - Muy potente
   - Control total sobre compresión

### Configuración Recomendada:
```
Formato: MP4 (H.264)
Resolución: 1920x1080
Bitrate: 2000-3000 kbps
Frame rate: 30 fps
Audio: Eliminar (no se usa)
```

---

## 🎨 Personalizar el Estilo

### Cambiar el Overlay (Filtro Oscuro):

En `home.html`, busca:
```css
.hero-overlay {
    background: rgba(0, 0, 0, 0.5); /* 50% negro */
}
```

**Opciones:**
- Más oscuro: `rgba(0, 0, 0, 0.7)` (70% negro)
- Más claro: `rgba(0, 0, 0, 0.3)` (30% negro)
- Sin overlay: Elimina la clase `hero-overlay`

### Cambiar Velocidad del Video:

Agregar al elemento `<video>`:
```html
<video autoplay muted loop playsinline class="hero-video" style="animation: none;">
```

O controlar con JavaScript:
```html
<script>
document.querySelector('.hero-video').playbackRate = 0.75; // 75% velocidad
</script>
```

---

## 📱 Compatibilidad Móvil

### Atributos importantes:

- `autoplay` - Inicia automáticamente
- `muted` - Sin sonido (requerido para autoplay en móviles)
- `playsinline` - Se reproduce en línea en iOS (no pantalla completa)
- `loop` - Se repite

### Fallback para móviles:

Si quieres usar imagen en móviles (ahorra datos):
```html
<video autoplay muted loop playsinline class="hero-video d-none d-md-block">
    <source src="video.mp4" type="video/mp4">
</video>
<div class="d-block d-md-none hero-image-fallback"></div>

<style>
.hero-image-fallback {
    background: url('imagen-fallback.jpg') center/cover;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
```

---

## ⚡ Rendimiento

### Tips para Mejor Performance:

1. **Comprime el video** - Usa menos de 5MB
2. **Lazy loading** - Carga después del contenido crítico
3. **Formato WebM** - Añade como alternativa (más ligero)
4. **Preload** - Carga mientras navega

```html
<video autoplay muted loop playsinline class="hero-video" preload="auto">
    <source src="video.webm" type="video/webm">
    <source src="video.mp4" type="video/mp4">
</video>
```

---

## 🎯 Ejemplo con Video Local

### Estructura de archivos:
```
media/
└── videos/
    └── cancha_hero.mp4

canchas/templates/canchas/
└── home.html
```

### Código en home.html:
```html
<video autoplay muted loop playsinline class="hero-video">
    <source src="/media/videos/cancha_hero.mp4" type="video/mp4">
    Tu navegador no soporta videos HTML5.
</video>
```

---

## 🔍 Solución de Problemas

### Video no se reproduce:

1. **Verificar formato**: Debe ser MP4 (H.264)
2. **Revisar ruta**: URL correcta del video
3. **Tamaño**: No más de 10MB
4. **Consola del navegador**: F12 → Ver errores

### Video se ve pixelado:

- Usa resolución mínima de 1280x720
- Aumenta bitrate en la compresión
- Usa video de mejor calidad

### Video consume mucho ancho de banda:

- Comprime más el video
- Reduce resolución a 1280x720
- Considera usar imagen en móviles

---

## 🎬 Videos Sugeridos para Canchas

### Temas Ideales:
- ⚽ Balón rodando en cancha
- 🏟️ Vista aérea de cancha
- 👥 Jugadores en acción (timelapse)
- 🌅 Cancha al atardecer
- ⚡ Movimiento de cámara lento (smooth)

### Evitar:
- ❌ Videos muy rápidos (marean)
- ❌ Muchos cambios de escena
- ❌ Colores muy brillantes (compiten con texto)
- ❌ Videos con texto superpuesto

---

## 📊 Comparación: Video vs Imagen

| Aspecto | Video | Imagen |
|---------|-------|--------|
| **Impacto visual** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Peso/Carga** | ⚠️ 2-10 MB | ✅ 100-500 KB |
| **Profesionalismo** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Compatibilidad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Mantenimiento** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🎯 Resumen

### Estado Actual:
- ✅ Video de fondo implementado
- ✅ Autoplay con muted
- ✅ Loop infinito
- ✅ Responsive
- ✅ Overlay para legibilidad

### Para Usar Tu Propio Video:
1. Optimiza el video (1920x1080, MP4, ~3MB)
2. Súbelo a `media/videos/`
3. Actualiza la ruta en `home.html`
4. Recarga la página

---

**Última actualización:** 17 de octubre de 2025  
**Sistema:** Reserva de Canchas v2.0
