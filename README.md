# Actividad - Gestión de usuarios con login y persistencia en archivos CSV

Actividad académica desarrollada en el curso **Desarrollo de Software Web & Analítica de Datos** (Riwi), correspondiente al **Módulo 1 – Fundamentos de programación en Python**.

## Descripción

Este repositorio contiene la solución de una práctica enfocada en:

- Login/autenticación de usuario desde archivo **CSV**.
- Gestión completa (CRUD) de usuarios con persistencia de información usando archivos CSV.
- Validaciones de datos, control de acceso y manejo de errores con `try/except`.

El objetivo pedagógico central es aprender a **conectarse a archivos CSV, procesar información de usuarios y registrar todos los cambios de forma persistente**.

---

## Objetivos de aprendizaje

- Comprender cómo implementar un sistema de login con validación por CSV en Python.
- Practicar registro/listado/búsqueda/edición/eliminación de usuarios en archivos CSV.
- Mejorar el control de flujos, modularidad y experiencia ante errores en consola.

---

## Estructura del repositorio

> La estructura exacta puede variar según la solución, por ejemplo:

```text
riwi_python_csv/
│
├─ solución/
│    ├─ main.py             # Script principal (interfaz de login y menú CRUD)
│    ├─ funciones.py        # Funciones para autenticar, crear, leer, actualizar, borrar usuarios
│    ├─ usuarios.csv        # Archivo persistente con usuarios registrados
│    └─ login.csv           # Archivo con usuarios/contraseñas (autenticación)
├─ userstory.md
└─ README.md
```

---

## Requisitos

- Python 3.x

---

## Ejecución

1. Clona el repositorio:
    ```bash
    git clone https://github.com/miguelrodrica/riwi_python_csv.git
    cd riwi_python_csv/solución
    ```

2. Ejecuta el archivo principal:
    ```bash
    python main.py
    ```

3. Ingresa tus credenciales y navega por el menú para crear, consultar, actualizar o eliminar usuarios almacenados en `usuarios.csv`.

---

## Alcance académico

Este proyecto fue realizado con fines formativos para reforzar fundamentos de programación en Python en el contexto de autenticación, CRUD y manejo de archivos CSV.

---

## Autor

Desarrollado por **@miguelrodrica** como actividad académica en Riwi.

