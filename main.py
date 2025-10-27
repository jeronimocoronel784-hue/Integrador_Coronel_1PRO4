#!/usr/bin/env python3
"""
main.py
Punto de entrada del programa.
Contiene menú principal y funciones de impresión.
"""

import sys
from manejo_archivos import load_paises, save_paises, crear_csv_ejemplo, CSV_FILE
from mensajes import msg_success, msg_error, msg_info, msg_warning
from busquedas import buscar_pais
from filtros import menu_filtrar
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from edicion import agregar_pais, editar_pais
from presentacion import imprimir_paises



def mostrar_menu() -> None:
    print("\n" + "="*70)
    print("      GESTIÓN DE PAÍSES - Menú principal".center(70))
    print("="*70)
    print("1) Buscar país")
    print("2) Filtrar países")
    print("3) Ordenar países")
    print("4) Mostrar estadísticas")
    print("5) Agregar país")
    print("6) Editar país")
    print("7) Guardar y salir")
    print("8) Salir sin guardar")
    print("9) Crear CSV de ejemplo")
    print("="*70)



def main() -> None:
    paises = load_paises(CSV_FILE)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            buscar_pais(paises)
        elif opcion == "2":
            menu_filtrar(paises)
        elif opcion == "3":
            ordenar_paises(paises)
        elif opcion == "4":
            mostrar_estadisticas(paises)
        elif opcion == "5":
            agregar_pais(paises)
        elif opcion == "6":
            editar_pais(paises)
        elif opcion == "7":
            save_paises(paises, CSV_FILE)
            msg_success("Datos guardados. Saliendo...")
            break
        elif opcion == "8":
            if input("¿Seguro? (s/n): ").lower() == "s":
                msg_info("Saliendo sin guardar...")
                break
        elif opcion == "9":
            crear_csv_ejemplo(CSV_FILE)
            paises = load_paises(CSV_FILE)
        else:
            msg_error("Opción inválida.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        msg_info("\nInterrupción por teclado. Saliendo...")
        sys.exit(0)
