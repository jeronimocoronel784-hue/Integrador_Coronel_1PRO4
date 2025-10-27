"""
filtros.py
Funciones para filtrado por continente y rangos, y su menú asociado.
"""

from mensajes import msg_info, msg_warning, msg_error
from typing import List, Dict
from validaciones import pedir_texto_no_vacio, pedir_entero
from presentacion import imprimir_paises



def pedir_rango_entero(campo: str):
    msg_info(f"Ingrese el rango para {campo}.")
    minimo = pedir_entero(f"  Mínimo {campo}: ")
    maximo = pedir_entero(f"  Máximo {campo}: ")
    if maximo < minimo:
        msg_warning("Máximo menor al mínimo. Intercambiando valores.")
        minimo, maximo = maximo, minimo
    return minimo, maximo


def filtrar_por_continente(paises: List[Dict]) -> None:
    continente = pedir_texto_no_vacio("Continente: ", allow_digits=False)
    encontrados = [p for p in paises if p["continente"].lower() == continente.lower()]
    if not encontrados:
        msg_warning("No se encontraron países en ese continente.")
    else:
        imprimir_paises(encontrados)


def filtrar_por_rango(paises: List[Dict], campo: str) -> None:
    if campo not in ("poblacion", "superficie"):
        msg_error("Campo inválido en filtrado.")
        return
    minimo, maximo = pedir_rango_entero(campo)
    encontrados = [p for p in paises if minimo <= p[campo] <= maximo]
    if not encontrados:
        msg_warning("No se encontraron países dentro del rango.")
    else:
        imprimir_paises(encontrados)


def menu_filtrar(paises: List[Dict]) -> None:
    while True:
        print("\n--- Filtrar países ---")
        print("1) Por continente")
        print("2) Por rango de población")
        print("3) Por rango de superficie")
        print("4) Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango(paises, "poblacion")
        elif opcion == "3":
            filtrar_por_rango(paises, "superficie")
        elif opcion == "4":
            break
        else:
            msg_error("Opción inválida.")
