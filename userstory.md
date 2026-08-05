# User Story – CRUD de usuarios con login y persistencia en archivos CSV

## Objetivo de la historia de usuario
Como estudiante del curso **Desarrollo de Software Web & Analítica de Datos (Riwi)**, quiero desarrollar un programa en Python que permita autenticar usuarios (login) y gestionar un CRUD de usuarios con persistencia en archivos CSV, practicando así estructuras de datos, validaciones, modularización, manejo de errores y lectura/escritura de archivos.

El propósito principal de la actividad es reforzar:
- Leer, validar y escribir archivos CSV.
- Realizar login a partir de credenciales guardadas en CSV.
- Crear, consultar, actualizar y eliminar usuarios, manteniendo persistencia de los datos.
- Control de errores y validaciones robustas para una experiencia de uso confiable.

---

## Descripción de tareas

### TASK 1
#### Login con validación desde CSV
- Cargar un archivo `login.csv` que contiene usuarios y contraseñas.
- Solicitar datos de acceso desde consola y validar contra el archivo.
- Permitir acceso solo si las credenciales son correctas.

---

### TASK 2
#### CRUD y persistencia de usuarios
- Cada usuario tiene Nombre, Apellidos y Correo (único/clave primaria).
- Implementar funciones para:
  - Crear usuario (registrar un nuevo usuario en `usuarios.csv`).
  - Listar todos los usuarios registrados.
  - Buscar un usuario por correo.
  - Actualizar los datos de un usuario existente.
  - Eliminar un usuario del archivo CSV.
- Mostrar mensajes claros y distintivos para los flujos exitoso y errores.

---

### TASK 3
#### Lectura y escritura de archivos CSV
- Leer y escribir siempre usando el módulo estándar `csv` de Python.
- Validar presencia de archivo y columnas correctas.
- Prevenir registros duplicados (basado en email).
- Manejar excepciones para evitar cierres inesperados.

---

### TASK 4
#### Menú e interacción por consola
- Menú principal tras el login, con opciones para todas las operaciones CRUD y salir.
- Usar bucles para permitir operaciones sucesivas sin reiniciar el programa.
- Validar entradas del usuario (números, campos obligatorios, formato de correo, etc).

---

### TASK 5
#### Estilo y calidad
- Separar la lógica del programa en módulos o funciones claras (`funciones.py`, `main.py`, etc).
- Documentar funciones con docstrings y breves comentarios.
- Los nombres de variables y funciones deben ser descriptivos y consistentes.
- Los errores nunca cierran el sistema inesperadamente, siempre hay un mensaje al usuario.

---

## Criterios de aceptación

### Funcionalidad
- El login solo permite acceso con credenciales válidas de CSV.
- El sistema permite crear, listar, buscar, actualizar y eliminar usuarios registrados en CSV.
- Todos los cambios en usuarios se reflejan de manera persistente en `usuarios.csv`.

### Validaciones y errores
- Control de errores de archivo inexistente, registros duplicados y entradas inválidas.
- Mensajes claros y diferenciados para éxito y error.

### Interfaz
- Menú claro y funcional por consola.
- Permite operar el sistema sin cerrarse por errores comunes.

### Código
- Uso de funciones, modularidad, manejo de excepciones y legibilidad apropiados para nivel fundamentos de Python.
