# User Story – Módulo 1 (Python)
## Gestión de productos con persistencia en archivos CSV

## Objetivo de la historia de usuario
Como estudiante del curso **Desarrollo de Software Web & Analítica de Datos (Riwi)**, quiero construir un programa en Python que permita **registrar, consultar, editar y persistir información de productos en archivos CSV**, para practicar el manejo de estructuras de datos, validaciones, funciones y lectura/escritura de archivos.

El propósito principal de esta actividad es reforzar:
- Conexión con archivos CSV.
- Manipulación de datos cargados desde CSV.
- Persistencia de cambios en disco.
- Manejo de errores comunes durante lectura/escritura.

---

## Descripción de tareas

### TASK 1
#### Modelado del dato y estructura base
- Definir la estructura de cada producto (por ejemplo, como diccionario).
- Crear una colección principal para almacenar varios productos en memoria.
- Establecer los campos mínimos esperados (ej. nombre, precio, cantidad o equivalentes según tu solución).

---

### TASK 2
#### Operaciones principales sobre los datos
- Implementar funciones para:
  - Agregar registros.
  - Mostrar registros.
  - Buscar registros.
  - Editar/actualizar registros.
  - Eliminar registros (si aplica en la solución).
- Mostrar mensajes claros para operaciones exitosas y para casos donde no se encuentre información.

---

### TASK 3
#### Lectura de archivos CSV
- Implementar la carga de datos desde un archivo `.csv`.
- Validar:
  - Existencia del archivo.
  - Formato básico esperado (columnas).
  - Conversión de tipos numéricos cuando corresponda.
- Manejar errores con `try/except` para evitar que el programa se cierre inesperadamente.

---

### TASK 4
#### Escritura y persistencia en CSV
- Implementar guardado/exportación de datos al archivo `.csv`.
- Asegurar que los cambios hechos en memoria se reflejen en el archivo final.
- Definir si el guardado sobrescribe o crea un nuevo archivo.
- Confirmar al usuario cuando la persistencia se realiza correctamente.

---

### TASK 5
#### Menú e interacción por consola
- Integrar un menú principal para ejecutar todas las funcionalidades.
- Usar un bucle (`while`) para mantener la app activa hasta seleccionar “Salir”.
- Validar entradas de usuario (opciones de menú y tipos de datos).

---

### TASK 6
#### Calidad y robustez
- Organizar el código en funciones para mejorar legibilidad.
- Usar nombres descriptivos en variables y funciones.
- Incluir comentarios o docstrings básicos.
- Garantizar que errores de entrada o de archivos no rompan el flujo del programa.

---

## Criterios de aceptación

### Funcionalidad
- El programa permite cargar datos desde CSV.
- El programa permite modificar/agregar información.
- El programa permite guardar los cambios en CSV (persistencia real).

### Validaciones y errores
- Se gestionan errores de archivo inexistente, formato inválido o tipos incorrectos.
- El sistema informa al usuario lo ocurrido con mensajes claros.

### Interfaz
- Existe menú funcional en consola con opciones claras.
- El usuario puede operar el sistema sin que se cierre ante errores comunes.

### Código
- Se evidencia uso de funciones, estructuras de datos y manejo de excepciones.
- El código es entendible y mantenible para nivel de fundamentos en Python.
