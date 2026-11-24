# Guía de clase — Semana 4: eliminar espacios

Esta guía agrega la operación **Delete** al sistema. El usuario busca un espacio mediante su código, revisa sus datos y confirma la eliminación antes de borrarlo.

Cada bloque de esta semana usa las marcas `# ===== INICIO SEMANA 4 =====` y `# ===== FIN SEMANA 4 =====`.

## 1. Importar la función de eliminación

En `main.py`, dentro de la importación desde `espacios`, agregar:

```python
# ===== INICIO SEMANA 4 =====
# SEMANA 4: función para eliminar un espacio existente.
eliminar_espacio
# ===== FIN SEMANA 4 =====
```

La función recibirá el código del espacio que se eliminará.

## 2. Crear la eliminación en SQLite

En `espacios.py`, agregar:

```python
# ===== INICIO SEMANA 4 =====
# SEMANA 4: eliminación de un espacio mediante su código.
def eliminar_espacio(codigo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM espacios
        WHERE UPPER(codigo) = UPPER(?)
    """, (codigo,))

    conexion.commit()
    eliminado = cursor.rowcount > 0
    conexion.close()

    return eliminado
# ===== FIN SEMANA 4 =====
```

La consulta usa el código únicamente para identificar el registro. Devuelve `True` si se eliminó un espacio y `False` cuando no existe.

## 3. Crear la pantalla de eliminación

En `main.py`, agregar la función `eliminar_datos_espacio()` entre las marcas de Semana 4.

Primero se solicita el código y se busca el espacio:

```python
codigo = input("Código del espacio a eliminar: ").strip()

if codigo == "":
    print("Debe ingresar un código.")
    pausa()
    return

espacio = buscar_espacio_por_codigo(codigo)

if espacio is None:
    print("Espacio no encontrado.")
    pausa()
    return
```

Después se muestran datos para que el usuario confirme que es el registro correcto:

```python
print(f"Código : {espacio['codigo']}")
print(f"Nombre : {espacio['nombre']}")
print(f"Tipo   : {espacio['tipo']}")

confirmacion = input(
    "¿Confirma eliminar este espacio? (S/N): "
).strip().upper()

if confirmacion != "S":
    print("Eliminación cancelada.")
    pausa()
    return
```

Solo la letra `S` confirma la eliminación. Cualquier otra respuesta conserva el registro.

Finalmente, llamar a:

```python
eliminado = eliminar_espacio(espacio["codigo"])

if eliminado:
    print("Espacio eliminado correctamente.")
else:
    print("No se pudo eliminar el espacio.")
```

## 4. Añadir la opción al menú

En `menu_principal()`, agregar:

```python
# ===== INICIO SEMANA 4 =====
# SEMANA 4: nueva opción del menú.
print("  7. Eliminar espacio")
# ===== FIN SEMANA 4 =====
print("  8. Salir")
```

En `ejecutar_sistema()`, antes de la salida, agregar:

```python
# ===== INICIO SEMANA 4 =====
# SEMANA 4: eliminación de espacios desde el menú principal.
elif opcion == "7":
    eliminar_datos_espacio()
# ===== FIN SEMANA 4 =====

elif opcion == "8":
    # Código de salida existente.
```

## 5. Probar el resultado

1. Elegir la opción 7 y escribir un código existente, por ejemplo `LAB-01`.
2. Escribir `N` en la confirmación; el sistema debe mostrar `Eliminación cancelada.` y el espacio debe seguir existiendo.
3. Repetir el proceso y escribir `S`; el sistema debe mostrar `Espacio eliminado correctamente.`.
4. Consultar el mismo código y confirmar que aparece `Espacio no encontrado.`.
5. Probar un código vacío y un código inexistente; en ambos casos no debe eliminarse ningún registro.
