"""
edicion.py
Funciones para alta y modificación de países.
"""

from typing import List, Dict
from mensajes import msg_error, msg_warning, msg_success
from validaciones import pedir_texto_no_vacio, pedir_entero, validar_entero
from manejo_archivos import save_paises, CSV_FILE


def existe_pais(paises: List[Dict], nombre: str) -> bool:
    return any(p["nombre"].lower() == nombre.lower() for p in paises)


def agregar_pais(paises: List[Dict]) -> None:
    print("\n--- Agregar país ---")
    nombre = pedir_texto_no_vacio("Nombre: ", allow_digits=False)
    if existe_pais(paises, nombre):
        msg_error("El país ya existe.")
        return
    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie (km²): ")
    continente = pedir_texto_no_vacio("Continente: ", allow_digits=False)

    nuevo = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(nuevo)

    if save_paises(paises, CSV_FILE):
        msg_success("Guardado exitoso.")
    else:
        msg_warning("Se agregó en memoria pero no se pudo guardar en archivo.")


def editar_pais(paises: List[Dict]) -> None:
    print("\n--- Editar país ---")
    nombre = pedir_texto_no_vacio("País a editar: ", allow_digits=False)
    idx = next((i for i, p in enumerate(paises) if p["nombre"].lower() == nombre.lower()), None)
    if idx is None:
        msg_error("No se encontró ese país.")
        return

    pais = paises[idx]

    nuevo_nombre = input(f"Nuevo nombre [{pais['nombre']}]: ").strip()
    if nuevo_nombre:
        if existe_pais(paises, nuevo_nombre) and nuevo_nombre.lower() != pais["nombre"].lower():
            msg_error("Ya existe otro país con ese nombre.")
        else:
            pais["nombre"] = nuevo_nombre

    entrada_pob = input(f"Nueva población [{pais['poblacion']}]: ").strip()
    if entrada_pob:
        ok, val = validar_entero(entrada_pob)
        if ok:
            pais["poblacion"] = val
        else:
            msg_warning("Valor inválido. No se cambia la población.")

    entrada_sup = input(f"Superficie [{pais['superficie']}]: ").strip()
    if entrada_sup:
        ok, val = validar_entero(entrada_sup)
        if ok:
            pais["superficie"] = val
        else:
            msg_warning("Valor inválido. No se cambia la superficie.")

    entrada_cont = input(f"Continente [{pais['continente']}]: ").strip()
    if entrada_cont:
        pais["continente"] = entrada_cont

    paises[idx] = pais

    if save_paises(paises, CSV_FILE):
        msg_success("Guardado exitoso.")
    else:
        msg_warning("Se modificó en memoria pero no se pudo guardar.")
