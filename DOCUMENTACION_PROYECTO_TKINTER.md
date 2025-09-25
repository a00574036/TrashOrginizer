# Proyecto Integrador – MVP (Tkinter)

Este proyecto es una **aplicación de escritorio con Tkinter** que muestra un menú principal y cinco ventanas de demostración: *Home*, *Formulario*, *Lista (CRUD básico)*, *Tabla (Treeview)* y *Canvas (Dibujo)*. Está pensado como base para prácticas de GUI y como plantilla para extender con nuevas pantallas.

---

## 🧭 Arquitectura y flujo

- **Punto de entrada (`main.py`)**  
  Crea la ventana raíz (`Tk`), define el menú con botones y abre cada ventana mediante funciones `open_win_*` en módulos separados. La interfaz usa `ttk` para estilos nativos.

- **Ventanas modulares (`win_*.py`)**  
  Cada ventana es una función `open_win_*` que recibe la raíz/parent y construye un `Toplevel` propio. Este patrón permite:
  - Separación clara de responsabilidades.
  - Reutilización de la ventana raíz.
  - Extensión sencilla (agregar nuevas ventanas implica crear un nuevo archivo `win_*` y añadir un botón en `main.py`).

---

## 🗂️ Estructura sugerida del repo

```
<repo-root>/
├─ data/
│  └─ sample.csv            # Datos de ejemplo para la tabla (requerido por win_table)
├─ src/
│  └─ app/
│     ├─ main.py            # Menú principal / lanzador
│     ├─ win_home.py        # Pantalla de bienvenida
│     ├─ win_form.py        # Formulario con validaciones y guardado a .txt
│     ├─ win_list.py        # CRUD básico con Listbox
│     ├─ win_table.py       # Tabla (Treeview) que lee CSV
│     └─ win_canvas.py      # Canvas con dibujos simples
└─ .vscode/
   └─ launch.json           # Configuración de depuración en VS Code
```

> **Nota:** Las importaciones en `main.py` asumen el layout `src/app/...` y que `PYTHONPATH` incluye `src`. Si ejecutas fuera de VS Code, exporta `PYTHONPATH=./src` (Linux/Mac) o usa `set PYTHONPATH=.\src` (Windows) antes de `python src/app/main.py`.

---

## ▶️ Ejecución

### Opción A — VS Code (recomendada)
1. Abre la carpeta del proyecto en VS Code.
2. Selecciona la configuración **“Programa con PYTHONPATH=src”** en el panel *Run and Debug*.
3. Inicia la depuración. Se establecerá `PYTHONPATH=src` y se ejecutará `src/app/main.py`.

### Opción B — Terminal
```bash
# Windows (PowerShell o CMD)
set PYTHONPATH=.\src
python .\srcpp\main.py

# Linux / macOS
export PYTHONPATH=./src
python ./src/app/main.py
```

---

## 📦 Dependencias

- **Python 3.x**
- **tkinter** (viene con la instalación estándar de Python en la mayoría de plataformas)
- Módulos estándar usados en distintas ventanas: `csv`, `pathlib`, `tkinter.ttk`, `tkinter.messagebox`, `tkinter.filedialog`

No se requieren paquetes externos ni `pip install`.

---

## 🧩 Módulos y funcionalidad

### 1) `main.py` — Menú principal
- Crea la ventana raíz (título, tamaño, `Frame` con padding).
- Presenta botones para abrir: Home, Formulario, Lista, Tabla y Canvas.
- Botón **Salir** que destruye la raíz.
- Patrón de apertura: `lambda: open_win_<modulo>(root)`.

### 2) `win_home.py` — Bienvenida
- Crea un `Toplevel` simple con etiqueta de bienvenida y un botón **“Mostrar mensaje”** que dispara `messagebox.showinfo`.
- Útil para probar modales y confirmar que la app responde.

### 3) `win_form.py` — Formulario con validación + guardado
- Campos: **Nombre** (`Entry`), **Edad** (`Entry`).
- Validaciones mínimas:
  - Nombre **no vacío**.
  - Edad **entera positiva** (usa `str.isdigit()` para checar que sea número entero).
- Al guardar:
  - Abre diálogo `asksaveasfilename` (sugiere `.txt`).
  - Escribe **Nombre** y **Edad** en el archivo.
  - Muestra confirmación con `messagebox.showinfo`.

**Ideas de mejora:**
- `Spinbox` o validación por `register` para edad.
- Normalizar espacios y capitalización del nombre.
- Manejo de excepciones de E/S (permisos, rutas inválidas).

### 4) `win_list.py` — CRUD básico con `Listbox`
- `Listbox` con entradas dinámicas.
- Acciones:
  - **Agregar**: inserta el texto si no está vacío.
  - **Eliminar seleccionado**: quita el elemento seleccionado.
  - **Limpiar**: borra toda la lista.
- Muestra *warnings* si el input está vacío.

**Ideas de mejora:**
- Soporte de **doble clic** para editar.
- Persistencia a disco (CSV/JSON).
- Atajos de teclado (DEL para eliminar, CTRL+L limpiar, etc.).

### 5) `win_table.py` — Tabla con `ttk.Treeview`
- Define columnas `("nombre", "valor1", "valor2")` y cabeceras en mayúscula inicial.
- Usa **`csv.DictReader`** para leer `data/sample.csv`.
- Inserta filas en el `Treeview`.
- Si el archivo **no existe**, muestra `messagebox.showwarning` y **no rompe** la app.

**Requisitos del CSV:**
- Ruta esperada: `<repo>/data/sample.csv`.
- Cabeceras mínimas: `nombre,valor1,valor2`.
- Ejemplo:
  ```csv
  nombre,valor1,valor2
  Item A,10,20
  Item B,5,15
  ```

**Ideas de mejora:**
- Ordenamiento por columna (binding a `heading`).
- Búsqueda/filtrado.
- Exportación a CSV desde el `Treeview`.

### 6) `win_canvas.py` — Dibujo en `Canvas`
- Crea figuras de ejemplo: **rectángulo**, **óvalo**, **línea**, y **texto**.
- Útil para explicar coordenadas, sistema de ejes y capas (z-order).
- Punto de partida para mini-juegos o editores simples.

**Ideas de mejora:**
- Interacción con mouse (arrastrar/soltar).
- Capas y selección de objetos.
- Guardar a imagen (vía `postscript` + conversión).

---

## ⚙️ Configuración de depuración (VS Code)

Archivo `.vscode/launch.json` recomendado:
```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Programa con PYTHONPATH=src",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/src/app/main.py",
      "cwd": "${workspaceFolder}",
      "env": { "PYTHONPATH": "${workspaceFolder}/src" },
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```
Con esto podrás lanzar el programa con la estructura `src/app/...` sin modificar las importaciones.

---

## 🧪 Pruebas manuales sugeridas

1. Abrir cada ventana desde el menú principal y cerrarla.
2. **Formulario**: probar nombre vacío, edad no numérica y guardado correcto de `.txt`.
3. **Lista**: agregar, eliminar y limpiar elementos. Verificar mensajes de advertencia.
4. **Tabla**: crear `data/sample.csv` con las cabeceras indicadas y verificar que se carguen filas.
5. **Canvas**: confirmar que las figuras se dibujan correctamente.

---

## 🚀 Cómo añadir una nueva ventana

1. Crear `src/app/win_nueva.py` con una función:
   ```python
   import tkinter as tk
   from tkinter import ttk

   def open_win_nueva(parent: tk.Tk):
       win = tk.Toplevel(parent)
       win.title("Mi nueva ventana")
       win.geometry("480x360")
       frm = ttk.Frame(win, padding=12)
       frm.pack(fill="both", expand=True)
       ttk.Label(frm, text="Hola desde mi nueva ventana").pack()
   ```
2. En `main.py`, agregar un botón:
   ```python
   from app.win_nueva import open_win_nueva
   # ...
   ttk.Button(frame, text="6) Nueva", command=lambda: open_win_nueva(root)).pack(pady=4, fill="x")
   ```

---

## 🛡️ Manejo de errores y buenas prácticas

- Usa `messagebox.showerror/showwarning/showinfo` para feedback al usuario.
- Envuelve operaciones de disco y parsing en `try/except` para robustez.
- Mantén **UI no bloqueante**: evita tareas pesadas en el hilo principal.
- Prefiere `ttk` para estilos consistentes.
- Centraliza constantes (tamaños, rutas, títulos) si crece el proyecto.

---

## 📌 Resumen

- Proyecto educativo y extensible con **ventanas independientes** y **menú lanzador**.
- Sin dependencias externas: ideal para aprender **Tkinter**, **Treeview**, **Listbox** y **diálogos**.
- Preparado para VS Code con `PYTHONPATH=src` y `launch.json`.
- Listo para crecer: añade nuevas `win_*` siguiendo el patrón mostrado.

