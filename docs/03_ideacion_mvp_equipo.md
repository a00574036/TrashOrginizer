# Sesión 3: Ideación y MVP

## Resumen del problema y criterios de éxito (Sesión 2)
El problema identificado es la **mezcla de residuos en espacios universitarios**, que dificulta la separación adecuada y reduce el reciclaje.  
El objetivo es desarrollar una aplicación local que ayude a estudiantes y personal universitario a **clasificar residuos de manera rápida, simple y offline**, contribuyendo al ODS 11 (Ciudades y comunidades sostenibles).

**Criterios de éxito:**
- Precisión ≥85% en clasificación de 3–4 categorías macro.
- UI estable (≥95% de ejecuciones sin errores).
- Tiempo de respuesta ≤5 s en ≥85% de casos.
- Registro persistente ≥45 muestras en CSV/JSON + carpeta de imágenes.

---

## Lluvia de ideas
1. **App local con PySimpleGUI (MVP):** Cargar o capturar foto, clasificar en 3–4 categorías macro (orgánico / reciclable / no reciclable / especiales) y mostrar resultado con texto + ícono/color.  
2. **Clasificador híbrido simple:** Empezar con selector guiado (si el modelo duda) + reglas para objetos comunes (PET, cartón, servilleta) mientras juntamos dataset propio.  
3. **Mini-dataset del campus:** Tomar 200–300 fotos reales (cafetería/aulas), etiquetarlas en CSV para entrenar un k-NN/SVM ligero (scikit-learn).  
4. **App de escritorio con Tkinter (demostración):** Menú principal con cinco ventanas de ejemplo (Home, Formulario, Lista CRUD, Tabla, Canvas), pensada como plantilla extensible para nuevas pantallas.  

---

## Idea elegida
**App local “Clasifica Ya” con PySimpleGUI**, sin servicios en la nube, que:  
- Permita cargar/capturar una imagen.  
- Clasifique el residuo en 3–4 categorías macro usando un clasificador híbrido (reglas + modelo ligero).  
- Muestre resultado con texto + ícono/color de alto contraste.  
- Guarde cada caso en `/data` (imagen + etiqueta + timestamp) y permita ver historial.  

### Justificación
- **ODS 11:** mejora la separación y reduce mezcla de residuos en espacios universitarios.  
- **Población objetivo:** universitarios; solución rápida, simple y offline; funciona en laptops promedio.  
- **Criterios de éxito:**  
  - ≥85% de acierto con confirmación cuando haya duda.  
  - UI estable ≥95% con PySimpleGUI.  
  - Respuesta en ≤5 s gracias a redimensionado y pipeline corto.  
  - ≥45 registros guardados en CSV/JSON + imágenes.  

---

## Clasificación MoSCoW de funcionalidades

| Prioridad         | Funcionalidad                 | ¿Cómo lo haremos de forma real?                                                         |
| ----------------- | ----------------------------- | --------------------------------------------------------------------------------------- |
| **Must**          | Cargar/Capturar imagen        | PySimpleGUI (file dialog) + opcional OpenCV para cámara.                                |
| **Must**          | Clasificación básica          | Reglas + k-NN/SVM con mini-dataset del campus (scikit-learn); 3–4 categorías macro.     |
| **Must**          | Mostrar resultado claro       | Etiqueta + color + ícono; manejo de errores simple.                                     |
| **Must**          | Guardar registro              | CSV/JSON + `/data/img/`; timestamp y ruta del archivo.                                  |
| **Should**        | Historial y filtro            | Tabla básica en la app (filtrar por categoría/fecha).                                   |
| **Should**        | Guía rápida                   | Pantalla con tabla de objetos comunes y su contenedor.                                  |
| **Should**        | Medir tiempo de respuesta     | Cronómetro interno y promedio visible al usuario.                                       |
| **Could**         | Corrección/Aprendizaje ligero | Si hay baja confianza, pedir confirmación y guardar etiqueta corregida.                 |
| **Could**         | Gamificación local            | Contador de puntos y top-3 semanal en CSV (sin login).                                  |
| **Could**         | Mapa mock de contenedores     | JSON estático con ubicaciones del campus.                                               |
| **Won’t (ahora)** | Nube / SSO / backend          | Se pospone por complejidad y permisos.                                                  |

---

## Wireflow (flujo de la app)
```mermaid
flowchart TD
    A[Inicio] --> B[Menú principal]
    B --> C[Cargar imagen]
    B --> D[Capturar con cámara]
    C --> E[Clasificación automática]
    D --> E
    E --> F[Mostrar resultado (texto + color + ícono)]
    F --> G[Guardar registro en /data]
    G --> H[Historial de clasificaciones]
```

---

## Arquitectura mínima

```
<repo-root>/
├─ data/                # Carpeta de imágenes y CSV/JSON de registros
│  ├─ img/              # Imágenes capturadas o cargadas
│  └─ records.csv       # Historial de clasificaciones
├─ src/
│  ├─ app/              # Interfaz gráfica (PySimpleGUI)
│  │  └─ main.py        # Punto de entrada de la aplicación
│  ├─ core/             # Lógica de negocio y modelo híbrido
│  │  └─ classifier.py  # Reglas + modelo k-NN/SVM
│  ├─ api/              # Conexión a API externa (opcional, futuro)
│  ├─ viz/              # Gráficas de métricas de impacto (matplotlib)
│  └─ data/             # Lectura/escritura de CSV y manejo de dataset
└─ docs/                # Documentación del proyecto
   └─ 03_ideacion_mvp_equipo.md
```

**Descripción de módulos:**
- **app/**: Interfaz con PySimpleGUI (menús, carga/captura de imagen, resultados).  
- **core/**: Lógica de clasificación híbrida (reglas + modelo ligero).  
- **api/**: Preparado para futura conexión con API externa.  
- **viz/**: Gráficas de métricas (aciertos, tiempos, impacto).  
- **data/**: Manejo de CSV/JSON y dataset del campus.  

---
