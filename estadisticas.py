"""
estadisticas.py
Funciones para cálculo de máximos, mínimos y promedios.
"""

from typing import List, Dict
from mensajes import msg_info, msg_warning


def mostrar_estadisticas(paises: List[Dict]) -> None:
    if not paises:
        msg_warning("No hay datos para calcular estadísticas.")
        return

    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]

    max_pob = max(poblaciones)
    min_pob = min(poblaciones)
    pais_max = next(p["nombre"] for p in paises if p["poblacion"] == max_pob)
    pais_min = next(p["nombre"] for p in paises if p["poblacion"] == min_pob)

    prom_pob = sum(poblaciones) / len(poblaciones)
    prom_sup = sum(superficies) / len(superficies)

    print("\n--- Estadísticas ---")
    msg_info(f"País con mayor población: {pais_max} ({max_pob:,})")
    msg_info(f"País con menor población: {pais_min} ({min_pob:,})")
    msg_info(f"Promedio de población: {prom_pob:,.2f}")
    msg_info(f"Promedio de superficie: {prom_sup:,.2f} km²")

    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1
    print("\nCantidad de países por continente:")
    for c, v in conteo.items():
        print(f"  {c}: {v}")
