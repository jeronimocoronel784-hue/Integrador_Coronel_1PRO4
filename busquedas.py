"""
busquedas.py
Contiene la función de búsqueda lineal por coincidencia parcial de nombre.
"""

from mensajes import msg_warning
from validaciones import pedir_texto_no_vacio
from typing import List, Dict
from presentacion import imprimir_paises




def buscar_pais(paises: List[Dict]) -> None:
    termino = pedir_texto_no_vacio("Ingrese el nombre o parte del nombre a buscar: ")
    termino_lower = termino.lower()
    encontrados = [p for p in paises if termino_lower in p["nombre"].lower()]
    if not encontrados:
        msg_warning("No se encontraron países con ese término.")
    else:
        imprimir_paises(encontrados)
