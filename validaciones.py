"""
validaciones.py
Módulo que agrupa funciones para validar y solicitar entrada segura.
"""

from typing import Tuple
from mensajes import msg_error

def validar_entero(text: str) -> Tuple[bool, int]:
    try:
        if text is None or text == "":
            return False, 0
        val = int(str(text).replace(",", "").strip())
        if val < 0:
            return False, 0
        return True, val
    except:
        return False, 0


def pedir_entero(prompt: str) -> int:
    while True:
        entrada = input(prompt).strip()
        ok, val = validar_entero(entrada)
        if ok:
            return val
        msg_error("Entrada inválida. Ingrese un número entero no negativo.")


def pedir_texto_no_vacio(prompt: str, allow_digits: bool = True) -> str:
    while True:
        txt = input(prompt).strip()
        if not txt:
            msg_error("No puede quedar vacío.")
            continue
        if not allow_digits and txt.isdigit():
            msg_error("No se permiten entradas puramente numéricas.")
            continue
        return txt
