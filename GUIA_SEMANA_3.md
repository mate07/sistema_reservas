# Guía de clase — Semana 3: actualizar espacios

Esta guía agrega la operación **Update** al sistema. El usuario busca un espacio por su código y puede actualizar nombre, tipo, capacidad y ubicación.

El código no cambia, porque identifica al espacio. El estado tampoco se modifica en esta semana. En cada bloque nuevo se usan las marcas `# ===== INICIO SEMANA 3 =====` y `# ===== FIN SEMANA 3 =====`.

## 1. Importar la función de actualización

En `main.py`, dentro de la importación desde `espacios`, agregar:

```python
# ===== INICIO SEMANA 3 =====
# SEMANA 3: función para actualizar un espacio existente.
actualizar_espacio
# ===== FIN SEMANA 3 =====
```

La función recibirá el código del espacio y los cuatro datos que sí pueden modificarse.

## 2. Crear la actualización en SQLite

En `espacios.py`, agregar:

```python
# ===== INICIO SEMANA 3 =====
# SEMANA 3: actualización de los datos editables de un espacio.
def actualizar_espacio(codigo, nombre, tipo, capacidad, ubicacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE espacios
        SET nombre = ?, tipo = ?, capacidad = ?, ubicacion = ?
        WHERE UPPER(codigo) = UPPER(?)
    """, (nombre, tipo, capacidad, ubicacion, codigo))

    conexion.commit()
    actualizado = cursor.rowcount > 0
    conexion.close()

    return actualizado
# ===== FIN SEMANA 3 =====
```

El primer dato, `codigo`, solo se usa para encontrar el espacio. La consulta actualiza nombre, tipo, capacidad y ubicación. Devuelve `True` si se encontró y actualizó un registro.

## 3. Crear la pantalla de edición

En `main.py`, agregar una función `actualizar_datos_espacio()` marcada entre inicio y fin de Semana 3.

El flujo de la función es:

```python
codigo = input("Código del espacio a actualizar: ").strip()
espacio = buscar_espacio_por_codigo(codigo)

if espacio is None:
    print("Espacio no encontrado.")
    pausa()
    return

print("Presione ENTER para conservar el valor actual.")
nombre = input(f"Nombre [{espacio['nombre']}]: ").strip()
tipo = input(f"Tipo [{espacio['tipo']}]: ").strip()
capacidad_texto = input(f"Capacidad [{espacio['capacidad']}]: ").strip()
ubicacion = input(f"Ubicación [{espacio['ubicacion']}]: ").strip()
```

Si se presiona Enter, se conserva el dato existente:

```python
if nombre == "":
    nombre = espacio["nombre"]

if tipo == "":
    tipo = espacio["tipo"]

if capacidad_texto == "":
    capacidad = espacio["capacidad"]
else:
    capacidad = int(capacidad_texto)

if ubicacion == "":
    ubicacion = espacio["ubicacion"]
```

La capacidad nueva debe ser un entero mayor que cero. Si no lo es, se muestra un mensaje y no se guarda ningún cambio.

Finalmente, llamar a:

```python
actualizado = actualizar_espacio(
    espacio["codigo"], nombre, tipo, capacidad, ubicacion
)
```

Cuando el resultado sea verdadero, debe aparecer `Espacio actualizado correctamente.`

## 4. Añadir la opción al menú

En `menu_principal()`, después de registrar espacios, agregar:

```python
# ===== INICIO SEMANA 3 =====
# SEMANA 3: nueva opción del menú.
print("  6. Actualizar espacio")
# ===== FIN SEMANA 3 =====
print("  7. Salir")
```

En `ejecutar_sistema()`, antes de la salida, agregar:

```python
# ===== INICIO SEMANA 3 =====
# SEMANA 3: actualización de espacios desde el menú principal.
elif opcion == "6":
    actualizar_datos_espacio()
# ===== FIN SEMANA 3 =====

elif opcion == "7":
    # Código de salida existente.
```

## 5. Probar el resultado

1. Elegir la opción 6 y escribir `LAB-01`.
2. Presionar Enter en nombre, tipo y ubicación; escribir `32` como capacidad.
3. Confirmar el mensaje de éxito y consultar `LAB-01`: solo la capacidad debe cambiar.
4. Repetir con un código inexistente y verificar el mensaje `Espacio no encontrado.`
5. Escribir texto en capacidad y luego `0`; ambos casos deben mostrar un mensaje de validación sin cambiar los datos.
6. Confirmar que el código y estado originales no cambian.
