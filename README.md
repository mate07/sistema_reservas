# Sistema de Reservas de Espacios

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![CLI](https://img.shields.io/badge/Interfaz-CLI-4D4D4D)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)

Aplicación de consola desarrollada en Python para administrar los espacios disponibles dentro de una institución. El sistema utiliza SQLite para almacenar la información de los espacios y ofrece operaciones básicas de consulta y mantenimiento mediante un menú interactivo.

## ¿En qué consiste?

El proyecto representa una primera versión de un sistema para gestionar aulas, laboratorios, auditorios y otros espacios institucionales.

Cada espacio registra información como:

- Código identificador.
- Nombre.
- Tipo de espacio.
- Capacidad.
- Ubicación.
- Estado de disponibilidad.

La aplicación está construida como un proyecto educativo que permite practicar la conexión con bases de datos, consultas SQL, operaciones CRUD, validación de datos y organización básica de un programa en Python.

## Tecnologías utilizadas

- **Python 3:** lenguaje principal de programación.
- **SQLite:** base de datos relacional embebida.
- **sqlite3:** módulo estándar de Python para trabajar con SQLite.
- **Interfaz de línea de comandos:** interacción mediante un menú en la terminal.
- **Git:** control de versiones del proyecto.

## Funcionalidades

### Consulta de información

- Listar todos los espacios registrados.
- Consultar un espacio mediante su código.
- Mostrar únicamente los espacios disponibles.
- Obtener un listado de los tipos de espacios registrados.

### Administración de espacios

- Registrar un nuevo espacio.
- Validar campos obligatorios.
- Validar que la capacidad sea un número entero mayor que cero.
- Evitar códigos duplicados.
- Actualizar el nombre, tipo, capacidad y ubicación de un espacio.
- Conservar el código y el estado durante la actualización.
- Eliminar un espacio después de confirmar la operación.

### Persistencia de datos

- Crear la carpeta de datos cuando es necesario.
- Crear la tabla `espacios` en SQLite.
- Insertar datos iniciales de prueba.
- Consultar y modificar la información almacenada en la base de datos.

## Estructura principal

| Archivo | Descripción |
|---|---|
| `main.py` | Menú principal, interacción con el usuario y validaciones de entrada. |
| `espacios.py` | Funciones para consultar, registrar, actualizar y eliminar espacios. |
| `database.py` | Creación de conexiones con SQLite. |
| `crear_bd.py` | Creación de la base de datos y carga de datos iniciales. |
| `config.py` | Rutas, título del sistema y configuración general. |
| `data/reservas.db` | Base de datos SQLite del proyecto. |
| `GUIA_SEMANA_2.md` | Documentación del registro de espacios. |
| `GUIA_SEMANA_3.md` | Documentación de la actualización de espacios. |
| `GUIA_SEMANA_4.md` | Documentación de la eliminación de espacios. |

## Modelo de datos actual

El proyecto utiliza la tabla `espacios`, que contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| `id` | Identificador interno autoincremental. |
| `codigo` | Código único del espacio. |
| `nombre` | Nombre descriptivo. |
| `tipo` | Clasificación del espacio. |
| `capacidad` | Cantidad máxima de personas. |
| `ubicacion` | Edificio, nivel o referencia física. |
| `estado` | Estado actual del espacio. |

## Alcance actual

La versión actual administra espacios y sus estados, pero todavía no incluye el registro formal de reservas con fechas, horarios, usuarios o control de conflictos entre reservas. Estas funcionalidades pueden incorporarse en futuras etapas del proyecto.

## Objetivo académico

El proyecto sirve como base práctica para reforzar los siguientes conceptos:

- Funciones y módulos en Python.
- Manejo de entradas desde la terminal.
- Validación de datos.
- Operaciones CRUD.
- Consultas parametrizadas en SQL.
- Uso de SQLite.
- Separación básica entre interfaz, lógica y persistencia.
- Documentación progresiva del desarrollo.

