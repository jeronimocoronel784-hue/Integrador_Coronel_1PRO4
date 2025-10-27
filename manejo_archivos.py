"""
manejo_archivos.py
Módulo de lectura, escritura y creación de archivos CSV.
Mantiene CSV_FILE y CSV_HEADERS para que todos los demás módulos lo importen.
"""

import csv
import os
from typing import List, Dict
from mensajes import msg_error, msg_warning, msg_success

CSV_FILE = "paises.csv"
CSV_HEADERS = ["nombre", "poblacion", "superficie", "continente"]


def crear_csv_ejemplo(path: str = CSV_FILE) -> None:
    ejemplo = [
        {"nombre": "Argentina", "poblacion": "45376763", "superficie": "2780400", "continente": "América"},
        {"nombre": "Brasil",    "poblacion": "213993437", "superficie": "8515767", "continente": "América"},
        {"nombre": "Mexico",    "poblacion": "128932753", "superficie": "1964375", "continente": "América"},
        {"nombre": "Estados Unidos", "poblacion": "331002651", "superficie": "9833520", "continente": "América"},
        {"nombre": "Canadá",    "poblacion": "37742154", "superficie": "9984670", "continente": "América"},
        {"nombre": "Japón",     "poblacion": "125800000", "superficie": "377975", "continente": "Asia"},
        {"nombre": "China",     "poblacion": "1393000000", "superficie": "9596961", "continente": "Asia"},
        {"nombre": "India",     "poblacion": "1380004385", "superficie": "3287263", "continente": "Asia"},
        {"nombre": "Alemania",  "poblacion": "83149300", "superficie": "357022", "continente": "Europa"},
        {"nombre": "Francia",   "poblacion": "65273511", "superficie": "643801", "continente": "Europa"},
        {"nombre": "España",    "poblacion": "46754778", "superficie": "505990", "continente": "Europa"},
        {"nombre": "Nigeria",   "poblacion": "206139589", "superficie": "923768", "continente": "África"},
        {"nombre": "Egipto",    "poblacion": "102334404", "superficie": "1010408", "continente": "África"},
        {"nombre": "Sudáfrica", "poblacion": "59308690", "superficie": "1221037", "continente": "África"},
        {"nombre": "Australia", "poblacion": "25499884", "superficie": "7692024", "continente": "Oceanía"},
        {"nombre": "Nueva Zelanda", "poblacion": "4822233", "superficie": "268838", "continente": "Oceanía"},
        {"nombre": "Islandia",  "poblacion": "341243", "superficie": "103000", "continente": "Europa"},
        {"nombre": "Chile",     "poblacion": "19116209", "superficie": "756102", "continente": "América"}
    ]
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(ejemplo)
        msg_success(f"CSV de ejemplo creado en '{path}'.")
    except Exception as e:
        msg_error(f"Error creando CSV de ejemplo: {e}")


def load_paises(path: str = CSV_FILE) -> List[Dict]:
    paises = []
    if not os.path.exists(path):
        msg_warning(f"Archivo '{path}' no encontrado. Iniciando vacío.")
        return paises

    try:
        with open(path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    paises.append({
                        "nombre": row["nombre"].strip(),
                        "poblacion": int(row["poblacion"]),
                        "superficie": int(row["superficie"]),
                        "continente": row["continente"].strip()
                    })
                except:
                    pass
    except Exception as e:
        msg_error(f"Error leyendo '{path}': {e}")
    return paises


def save_paises(paises: List[Dict], path: str = CSV_FILE) -> bool:
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(paises)
        return True
    except Exception as e:
        msg_error(f"Error guardando: {e}")
        return False
