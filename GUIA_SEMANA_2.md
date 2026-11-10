# Guía de clase — Semana 2: registrar espacios

Esta guía agrega la operación **Create** al sistema: registrar un espacio nuevo desde el menú y guardarlo en SQLite.

Todos los fragmentos nuevos se identifican con `# SEMANA 2` en el código.

## 1. Importar la función nueva

En `main.py`, dentro de la importación desde `espacios`, agregar:

```python
# SEMANA 2: función para guardar un espacio nuevo.
registrar_espacio
```

Esta función recibe los datos ya validados y los guarda en la base de datos.

## 2. Crear la inserción en la base de datos

En `espacios.py`, importar `sqlite3` y agregar:

```python
# SEMANA 2: inserción de un nuevo espacio en la base de datos.
def registrar_espacio(codigo, nombre, tipo, capacidad, ubicacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO espacios (
                codigo, nombre, tipo, capacidad, ubicacion, estado
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            codigo, nombre, tipo, capacidad, ubicacion, "DISPONIBLE"
        ))
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexion.close()
```

Recibe los cinco datos del espacio. Si el código ya existe, SQLite produce un error de unicidad y la función devuelve `False`; si se guarda, devuelve `True`. El estado siempre inicia como `DISPONIBLE`.

## 3. Crear la pantalla de registro

En `main.py`, agregar esta función:

```python
# SEMANA 2: pantalla, validación y registro de un espacio nuevo.
def registrar_nuevo_espacio():
    limpiar_pantalla()
    titulo("REGISTRO DE ESPACIO")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo: ").strip()
    capacidad_texto = input("Capacidad: ").strip()
    ubicacion = input("Ubicación (opcional): ").strip()

    if codigo == "" or nombre == "" or tipo == "":
        print("Código, nombre y tipo son obligatorios.")
        pausa()
        return

    try:
        capacidad = int(capacidad_texto)
    except ValueError:
        print("La capacidad debe ser un número entero.")
        pausa()
        return

    if capacidad <= 0:
        print("La capacidad debe ser mayor que cero.")
        pausa()
        return

    if buscar_espacio_por_codigo(codigo) is not None:
        print("Ya existe un espacio con ese código.")
        pausa()
        return

    registrado = registrar_espacio(
        codigo, nombre, tipo, capacidad, ubicacion
    )

    if registrado:
        print("Espacio registrado correctamente.")
    else:
        print("No se pudo registrar: el código ya existe.")

    pausa()
```

La pantalla valida los campos obligatorios, transforma la capacidad a número entero, exige que sea mayor que cero y verifica que el código no exista. Si el registro es válido, debe aparecer el mensaje `Espacio registrado correctamente.`

## 4. Añadir la opción al menú

En `menu_principal()`, agregar:

```python
# SEMANA 2: nueva opción del menú.
print("  5. Registrar espacio")
print("  6. Salir")
```

En `ejecutar_sistema()`, agregar antes de la salida:

```python
# SEMANA 2: registro de espacios desde el menú principal.
elif opcion == "5":
    registrar_nuevo_espacio()

elif opcion == "6":
    # Código de salida existente.
```

Al elegir la opción 5, el sistema debe mostrar el formulario de registro. La salida pasa a ser la opción 6.

## 5. Probar el resultado

1. Seleccionar la opción 5.
2. Registrar, por ejemplo: `BIB-01`, `Biblioteca`, `Biblioteca`, `50`, `Edificio B`.
3. Confirmar el mensaje de éxito.
4. Usar “Listar espacios” y comprobar que aparece `BIB-01` con estado `DISPONIBLE`.
5. Usar “Consultar espacio” con `BIB-01`.
6. Intentar registrar de nuevo `BIB-01`, dejar un campo obligatorio vacío, ingresar una capacidad no numérica y después `0`. Cada caso debe mostrar su mensaje de validación y volver al menú sin cerrar el programa.
