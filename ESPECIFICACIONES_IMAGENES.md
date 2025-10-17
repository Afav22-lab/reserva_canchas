# 📸 Especificaciones de Imágenes - Sistema de Reserva de Canchas

## 🎯 Resumen Rápido

Para obtener los mejores resultados, usa imágenes con estas características:

| Ubicación | Tamaño Recomendado | Ratio | Peso Máximo |
|-----------|-------------------|-------|-------------|
| **Tarjetas (Home/Lista)** | 800 x 500 px | 16:10 | 500 KB |
| **Página de Reserva** | 1200 x 400 px | 3:1 | 800 KB |
| **Admin (Preview)** | 400 x 250 px | 16:10 | 300 KB |

---

## 📋 Especificaciones Detalladas

### 1. 🏠 Página de Inicio y Lista de Canchas

**Ubicación:** `home.html` y `lista_canchas.html`

**Dimensiones Recomendadas:**
- **Ancho:** 800 píxeles
- **Alto:** 500 píxeles
- **Ratio:** 16:10 (horizontal)

**Especificaciones Técnicas:**
```
- Tamaño en pantalla: 200px de alto (se ajusta automáticamente)
- Object-fit: cover (recorta para llenar el espacio)
- Formato: JPG, PNG, WebP
- Peso recomendado: 200-500 KB
- Resolución: 72-150 DPI
```

**¿Por qué estas dimensiones?**
- Las tarjetas tienen 200px de alto en la pantalla
- El ratio 16:10 es perfecto para mostrar canchas de fútbol horizontalmente
- Se recorta automáticamente para llenar el espacio sin deformarse

**Ejemplo visual:**
```
┌─────────────────────────────────┐
│                                 │
│         CANCHA DE FÚTBOL        │  ← 200px alto en pantalla
│                                 │
└─────────────────────────────────┘
      ← Ancho responsivo →
```

---

### 2. 📝 Página de Reserva

**Ubicación:** `reservar.html`

**Dimensiones Recomendadas:**
- **Ancho:** 1200 píxeles
- **Alto:** 400 píxeles
- **Ratio:** 3:1 (panorámica)

**Especificaciones Técnicas:**
```
- Tamaño en pantalla: 300px de alto máximo
- Object-fit: cover (recorta para llenar el espacio)
- Formato: JPG, PNG, WebP
- Peso recomendado: 400-800 KB
- Resolución: 72-150 DPI
```

**¿Por qué estas dimensiones?**
- Vista panorámica de la cancha completa
- Ideal para mostrar el contexto completo de la instalación
- Se adapta al ancho completo del formulario

**Ejemplo visual:**
```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│              VISTA PANORÁMICA DE LA CANCHA               │  ← 300px alto máximo
│                                                           │
└───────────────────────────────────────────────────────────┘
                    ← 100% del ancho →
```

---

## 🎨 Recomendaciones de Contenido

### ✅ Buenas Prácticas

1. **Encuadre:**
   - Captura la cancha completa en la imagen
   - Incluye las porterías si es posible
   - Evita recortes muy cerrados

2. **Iluminación:**
   - Preferiblemente con luz natural
   - Evita sombras muy marcadas
   - Contraste adecuado entre el césped y las líneas

3. **Ángulo:**
   - Vista frontal o lateral de la cancha
   - Altura media (ni muy alta ni muy baja)
   - Horizonte nivelado

4. **Calidad:**
   - Imágenes nítidas y enfocadas
   - Colores vivos y naturales
   - Sin marcas de agua ni logos grandes

### ❌ Evitar

- ❌ Imágenes muy pesadas (más de 2 MB)
- ❌ Fotos borrosas o desenfocadas
- ❌ Imágenes verticales (ratio 9:16)
- ❌ Mucho texto superpuesto
- ❌ Excesiva edición o filtros

---

## 🛠️ Herramientas para Optimizar Imágenes

### Online (Gratis)
1. **TinyPNG** - https://tinypng.com/
   - Reduce el peso sin perder calidad
   
2. **Squoosh** - https://squoosh.app/
   - Editor completo de Google
   - Permite cambiar dimensiones y comprimir

3. **Canva** - https://www.canva.com/
   - Redimensionar y recortar
   - Preset: 800 x 500 px

### Software de Escritorio
- **GIMP** (Gratis) - Editor completo
- **Paint.NET** (Gratis - Windows) - Simple y efectivo
- **Photoshop** (Pago) - Profesional

---

## 📐 Cómo Redimensionar tus Imágenes

### Método 1: Usando TinyPNG + Squoosh

1. Ve a https://squoosh.app/
2. Arrastra tu imagen
3. En "Resize":
   - Para tarjetas: 800 x 500 px
   - Para reserva: 1200 x 400 px
4. En "Compress": Selecciona MozJPEG o WebP
5. Ajusta calidad a 80-85%
6. Descarga la imagen optimizada

### Método 2: Usando Paint (Windows)

1. Abre la imagen con Paint
2. Click en "Cambiar tamaño"
3. Desmarca "Mantener relación de aspecto"
4. Ingresa las dimensiones:
   - Ancho: 800 px (tarjetas) o 1200 px (reserva)
   - Alto: 500 px (tarjetas) o 400 px (reserva)
5. Guarda como JPEG con calidad media-alta

### Método 3: Usando Photoshop/GIMP

1. Abre la imagen
2. Image → Image Size
3. Cambia dimensiones a:
   - 800 x 500 px (tarjetas)
   - 1200 x 400 px (reserva)
4. Export → Save for Web
5. JPEG Quality: 70-80%

---

## 📊 Tabla Comparativa de Formatos

| Formato | Ventajas | Desventajas | Recomendado Para |
|---------|----------|-------------|------------------|
| **JPG** | Archivos pequeños, compatible con todo | Pierde calidad al editar | Fotos de canchas (recomendado) |
| **PNG** | Sin pérdida de calidad, soporta transparencia | Archivos más pesados | Logos o gráficos |
| **WebP** | Mejor compresión, calidad alta | Soporte limitado en navegadores viejos | Web moderna (opcional) |

**Recomendación:** Usa **JPG** para todas las fotos de canchas.

---

## 🎯 Checklist Antes de Subir una Imagen

- [ ] ¿El tamaño es 800x500 px (tarjetas) o 1200x400 px (reserva)?
- [ ] ¿El peso es menor a 500 KB (tarjetas) o 800 KB (reserva)?
- [ ] ¿La imagen está enfocada y nítida?
- [ ] ¿Se ve toda la cancha o la parte importante?
- [ ] ¿Los colores se ven naturales?
- [ ] ¿El formato es JPG o PNG?
- [ ] ¿La imagen tiene buena iluminación?

---

## 💡 Ejemplos de Buenas Imágenes

### ✅ Ejemplo 1: Vista Completa
```
Características:
- Se ve toda la cancha
- Porterías visibles
- Buena iluminación
- Líneas del campo nítidas
- 800 x 500 px, 350 KB
```

### ✅ Ejemplo 2: Vista Angular
```
Características:
- Ángulo diagonal interesante
- Buen contraste de colores
- Césped verde vibrante
- Sin personas ni objetos distractores
- 800 x 500 px, 420 KB
```

---

## 🔧 Solución de Problemas Comunes

### Problema: La imagen se ve estirada
**Solución:** Verifica que el ratio sea correcto (16:10 para tarjetas, 3:1 para reserva)

### Problema: La imagen pesa mucho y tarda en cargar
**Solución:** Comprime la imagen con TinyPNG o reduce la calidad a 80%

### Problema: La imagen se ve pixelada
**Solución:** Usa una imagen de mayor resolución (mínimo 800x500 px)

### Problema: Se corta una parte importante de la imagen
**Solución:** Reencuadra la foto para que el elemento importante esté centrado

---

## 📞 Resumen Final

### Para Mejores Resultados:

**Tarjetas (Home/Lista de Canchas):**
- 📏 Tamaño: **800 x 500 píxeles**
- 💾 Peso: **200-500 KB**
- 📁 Formato: **JPG**

**Página de Reserva:**
- 📏 Tamaño: **1200 x 400 píxeles**
- 💾 Peso: **400-800 KB**
- 📁 Formato: **JPG**

**Consejos Adicionales:**
- 🎨 Colores vivos y naturales
- ☀️ Buena iluminación
- 🎯 Cancha completa en el encuadre
- ✨ Imagen nítida y enfocada

---

## 📚 Recursos Adicionales

- **Imágenes de ejemplo gratuitas:** https://unsplash.com/s/photos/soccer-field
- **Optimizador de imágenes:** https://tinypng.com/
- **Editor online:** https://squoosh.app/
- **Guía de fotografía deportiva:** https://www.adobe.com/sports-photography

---

**Documento actualizado:** 17 de octubre de 2025  
**Sistema:** Reserva de Canchas v2.0  
**Autor:** Sistema de Gestión de Canchas
