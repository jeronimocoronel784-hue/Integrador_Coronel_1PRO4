"""
mensajes.py
Módulo que contiene funciones simples de salida por consola.
Se reutiliza en todo el programa para mantener coherencia visual.
"""

def msg_error(text: str) -> None:
    print("ERROR: " + text)

def msg_warning(text: str) -> None:
    print("ADVERTENCIA: " + text)

def msg_success(text: str) -> None:
    print("ÉXITO: " + text)

def msg_info(text: str) -> None:
    print("INFO: " + text)
