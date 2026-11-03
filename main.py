import os

from config import TITULO_SISTEMA, ANCHO_PANTALLA

from espacios import (
    obtener_todos_los_espacios,
    buscar_espacio_por_codigo,
    obtener_espacios_disponibles,
    obtener_tipos_de_espacio
)


def limpiar_pantalla():
    """
    Limpia la terminal dependiendo del sistema operativo.
    """

    os.system("cls" if os.name == "nt" else "clear")


def linea(caracter="="):
    """
    Imprime una línea utilizando el ancho definido.
    """

    print(caracter * ANCHO_PANTALLA)


def titulo(texto):
    """
    Muestra encabezados centrados.
    """

    linea("=")

    print(texto.center(ANCHO_PANTALLA))

    linea("=")


def pausa():

    print()

    input("Presione ENTER para continuar...")


def menu_principal():

    limpiar_pantalla()

    titulo(TITULO_SISTEMA)

    print()
    print("  1. Listar espacios")
    print("  2. Consultar espacio")
    print("  3. Ver espacios disponibles")
    print("  4. Ver tipos de espacios")
    print("  5. Salir")
    print()

    linea("-")

    opcion = input("Seleccione una opción: ")

    return opcion


def mostrar_tabla(espacios):

    if not espacios:

        print()
        print("No existen registros para mostrar.")

        return

    print()

    print(
        f"{'CÓDIGO':<10}"
        f"{'NOMBRE':<30}"
        f"{'TIPO':<16}"
        f"{'CAP.':<7}"
        f"{'ESTADO':<15}"
    )

    linea("-")

    for espacio in espacios:

        print(
            f"{espacio['codigo']:<10}"
            f"{espacio['nombre'][:28]:<30}"
            f"{espacio['tipo'][:14]:<16}"
            f"{espacio['capacidad']:<7}"
            f"{espacio['estado']:<15}"
        )


def listar_espacios():

    limpiar_pantalla()

    titulo("LISTADO GENERAL DE ESPACIOS")

    espacios = obtener_todos_los_espacios()

    mostrar_tabla(espacios)

    print()

    linea("-")

    print(f"Total de espacios registrados: {len(espacios)}")

    pausa()


def consultar_espacio():

    limpiar_pantalla()

    titulo("CONSULTA DE ESPACIO")

    print()

    codigo = input(
        "Ingrese el código del espacio: "
    ).strip()

    if codigo == "":

        print()
        print("Debe ingresar un código.")

        pausa()

        return

    espacio = buscar_espacio_por_codigo(codigo)

    if espacio is None:

        print()
        print("Espacio no encontrado.")

        pausa()

        return

    print()

    linea("-")

    print(f"Código       : {espacio['codigo']}")
    print(f"Nombre       : {espacio['nombre']}")
    print(f"Tipo         : {espacio['tipo']}")
    print(f"Capacidad    : {espacio['capacidad']} personas")
    print(f"Ubicación    : {espacio['ubicacion']}")
    print(f"Estado       : {espacio['estado']}")

    linea("-")

    pausa()


def listar_disponibles():

    limpiar_pantalla()

    titulo("ESPACIOS DISPONIBLES")

    espacios = obtener_espacios_disponibles()

    mostrar_tabla(espacios)

    print()

    linea("-")

    print(
        f"Cantidad de espacios disponibles: "
        f"{len(espacios)}"
    )

    pausa()


def listar_tipos():

    limpiar_pantalla()

    titulo("TIPOS DE ESPACIOS")

    tipos = obtener_tipos_de_espacio()

    print()

    if not tipos:

        print("No existen tipos registrados.")

    else:

        tipos_ordenados = sorted(tipos)

        contador = 1

        for tipo in tipos_ordenados:

            print(f"  {contador}. {tipo}")

            contador += 1

    print()

    linea("-")

    print(f"Cantidad de tipos diferentes: {len(tipos)}")

    pausa()


def ejecutar_sistema():

    while True:

        opcion = menu_principal()

        if opcion == "1":

            listar_espacios()

        elif opcion == "2":

            consultar_espacio()

        elif opcion == "3":

            listar_disponibles()

        elif opcion == "4":

            listar_tipos()

        elif opcion == "5":

            limpiar_pantalla()

            titulo(TITULO_SISTEMA)

            print()
            print(
                "Sistema finalizado correctamente."
                .center(ANCHO_PANTALLA)
            )
            print()

            break

        else:

            print()
            print("Opción incorrecta.")

            pausa()


if __name__ == "__main__":

    ejecutar_sistema()