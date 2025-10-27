# presentacion.py
from mensajes import msg_info

def imprimir_paises(paises):
    """
    Imprime tabla de países de forma tabular.
    Función compartida entre módulos para evitar importación circular.
    """
    if not paises:
        msg_info("No hay países para mostrar.")
        return
    print(f"\n{'Nombre':<25} {'Población':>12} {'Superficie':>12} {'Continente':>15}")
    print("-"*70)
    for p in paises:
        print(f"{p['nombre']:<25} {p['poblacion']:>12,} {p['superficie']:>12,} {p['continente']:>15}")
    print(f"\nTotal: {len(paises)} país(es).")
