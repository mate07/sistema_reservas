import sqlite3

from config import DATABASE


def obtener_conexion():
    """
    Crea y retorna una conexión a la base de datos SQLite.
    """

    conexion = sqlite3.connect(DATABASE)

    # Permite acceder a los campos por nombre:
    # fila["codigo"], fila["nombre"], etc.
    conexion.row_factory = sqlite3.Row

    return conexion