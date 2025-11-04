# Trabajo Integrador – Gestión de Países  
**Asignatura:** Programación I  
**Institución:** Universidad Tecnológica Nacional – Facultad Regional Mendoza  
**Profesor:** Cintia Ragoni  
**Alumno:** Jeronimo Coronel  
**Año:** 2025
---

## Video explicativo:
https://drive.google.com/file/d/1rVyCeeAFBvYGT63nyYajgfrJ7VzqHAm1/view?usp=drive_link

---

## Descripción General del Proyecto

El presente trabajo consiste en el desarrollo de un programa en Python que permite gestionar un conjunto de datos correspondientes a distintos países del mundo. La información se almacena en un archivo CSV y el sistema permite consultarla, modificarla y analizarla mediante diversas operaciones.

El objetivo principal del proyecto es integrar los conocimientos adquiridos en la asignatura Programación I, incluyendo estructuras de control, manejo de archivos, funciones, modularización, validaciones y uso de estructuras de datos tipo lista y diccionario.

---

## Funcionalidades Principales

El programa permite realizar las siguientes operaciones:

1. **Búsqueda de países** mediante coincidencia parcial o exacta del nombre.
2. **Filtrado** de países por:
   - Continente
   - Rango de población
   - Rango de superficie territorial
3. **Ordenamiento** de países según:
   - Nombre (ascendente o descendente)
   - Población (ascendente o descendente)
   - Superficie (ascendente o descendente)
4. **Visualización de estadísticas**, tales como:
   - País con mayor y menor población
   - Promedios generales
   - Cantidad de países por continente
5. **Alta de nuevos países**, con validaciones de entrada y prevención de duplicados.
6. **Modificación de países existentes**.
7. **Guardado automático** en el archivo CSV.
8. Opción de **crear un archivo CSV ejemplo** con datos pre-cargados.

---

## Estructura del Proyecto

Integrador_Coronel_1PRO4/
│
├── main.py # Punto de entrada del programa y menú principal
├── paises.csv # Archivo de datos (se genera o actualiza automáticamente)
│
├── manejo_archivos.py # Funciones para lectura y escritura del archivo CSV
├── busquedas.py # Funciones de búsqueda de países
├── filtros.py # Funciones para filtrado de resultados
├── ordenamientos.py # Funciones de ordenamiento (uso de sorted y Timsort)
├── estadisticas.py # Cálculo y presentación de estadísticas
├── edicion.py # Funciones para agregar y editar registros
├── validaciones.py # Validaciones de campos y entradas del usuario
└── presentacion.py # Formato de salida y visualización en consola

---
## Estructuras y Conceptos Utilizados

| **Listas** | Se almacenan todos los países como elementos de una lista principal. |
| **Diccionarios** | Cada país se representa mediante claves: `nombre`, `poblacion`, `superficie`, `continente`. |
| **Modularización** | El programa se divide en archivos según funcionalidad (búsquedas, filtros, estadísticas, etc.). |
| **Funciones** | Cada acción del menú es resuelta mediante una función especializada. |
| **Manejo de archivos CSV** | Lectura y escritura a disco usando el módulo `csv`. |
| **Validaciones** | Entradas controladas para evitar errores y garantizar datos correctos. |
| **Manejo de errores** | Uso de `try/except` para prevenir fallos durante la ejecución. |
| **Algoritmos de búsqueda** | Se utiliza búsqueda secuencial lineal. |
| **Algoritmos de ordenamiento** | Se utiliza `sorted()` en Python, basado en **Timsort**, eficiente y estable. |

---
## Requisitos de Ejecución

- Python **3.8** o superior
- No requiere instalación de librerías externas.
- Sistema operativo recomendado: Windows, Linux o macOS.

---

## Instrucciones de Uso

1. Clonar el repositorio o descargar los archivos.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el programa mediante:

bash
python main.py

o en Windows:
py main.py

4. Seguir las opciones del menú principal.

======================================================================
                   GESTIÓN DE PAÍSES - Menú Principal
======================================================================
1) Buscar país
2) Filtrar países
3) Ordenar países
4) Mostrar estadísticas
5) Agregar país
6) Editar país
7) Guardar y salir
8) Salir sin guardar
9) Crear CSV de ejemplo
======================================================================

---
