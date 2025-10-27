"""
ordenamientos.py
Menú y opciones de ordenamiento usando sorted() (Timsort).
"""

from typing import List, Dict
from mensajes import msg_error
from presentacion import imprimir_paises



def ordenar_paises(paises: List[Dict]) -> None:
    while True:
        print("\n--- Ordenar países ---")
        print("1) Nombre (A-Z)")
        print("2) Nombre (Z-A)")
        print("3) Población (ascendente)")
        print("4) Población (descendente)")
        print("5) Superficie (ascendente)")
        print("6) Superficie (descendente)")
        print("7) Volver")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            imprimir_paises(sorted(paises, key=lambda x: x["nombre"].lower()))
        elif opcion == "2":
            imprimir_paises(sorted(paises, key=lambda x: x["nombre"].lower(), reverse=True))
        elif opcion == "3":
            imprimir_paises(sorted(paises, key=lambda x: x["poblacion"]))
        elif opcion == "4":
            imprimir_paises(sorted(paises, key=lambda x: x["poblacion"], reverse=True))
        elif opcion == "5":
            imprimir_paises(sorted(paises, key=lambda x: x["superficie"]))
        elif opcion == "6":
            imprimir_paises(sorted(paises, key=lambda x: x["superficie"], reverse=True))
        elif opcion == "7":
            break
        else:
            msg_error("Opción inválida.")
