# TrashOrginizer

<u>Arquitectura del proyecto:</u>

- **app/**  
  Contiene la interfaz gráfica desarrollada con PySimpleGUI.  
  Aquí se definen las ventanas principales, botones y flujo de pantallas que usa el usuario.

- **core/**  
  Implementa la lógica de negocio y funciones matemáticas.  
  Aquí se realizan las validaciones, clasificación de residuos y reglas del sistema.

- **api/**  
  Gestiona la conexión con APIs externas, por ejemplo un modelo de visión por computadora para identificar el tipo de basura en imágenes.

- **viz/**  
  Se encarga de la generación de gráficas con maptolib.
  Permite visualizar estadísticas como cantidad de objetos clasificados por categoría.

- **data/**  
  Maneja la lectura y escritura de archivos.  
  Incluye guardar registros de clasificaciones (imagen + resultado) y exportación de estos.
