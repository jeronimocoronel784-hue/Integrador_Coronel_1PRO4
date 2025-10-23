# Trabajo Práctico Integrador – Programación 1  
**Gestión de Datos de Países en Python**

## Información del Proyecto
- **Alumno:** Jerónimo Coronel  
- **Profesor:** Rigoni Cintia, Hualpa Ramiro
- **Carrera:** Tecnicatura Universitaria en Programación  
- **Materia:** Programación 1  
- **Institución:** Universidad Tecnológica Nacional

---

## Descripción General
Este proyecto consiste en el desarrollo de un sistema en **Python** que permite **gestionar información sobre países** utilizando estructuras de datos como listas y diccionarios.  

El programa trabaja con un archivo CSV llamado `paises.csv`, desde el cual se leen los datos, y ofrece un menú interactivo en consola para realizar distintas operaciones sobre el conjunto de países.

Las principales funcionalidades son:
1. **Búsqueda de países** por nombre (parcial o exacta).  
2. **Filtrado** por continente, rango de población o superficie.  
3. **Ordenamiento** por nombre, población o superficie (ascendente/descendente).  
4. **Estadísticas** (país con mayor/menor población, promedios, cantidad por continente).  
5. **Agregar y editar países**, guardando los cambios en el CSV.  

El sistema valida las entradas del usuario, maneja errores de formato y ofrece mensajes claros, cumpliendo los criterios de robustez, modularidad y legibilidad requeridos por la rúbrica.

---

## Estructuras y Conceptos Utilizados

- **Listas:** se utilizan para almacenar todos los países leídos del archivo CSV en memoria.  
- **Diccionarios:** cada país se representa como un diccionario con las claves `nombre`, `poblacion`, `superficie` y `continente`.  
- **Funciones:** el código está completamente modularizado; cada función cumple una tarea específica (lectura, filtrado, ordenamiento, estadísticas, etc.).  
- **Condicionales y Bucles:** se usan para controlar el flujo del menú y validar las acciones del usuario.  
- **Manejo de archivos CSV:** el programa puede leer, escribir y actualizar datos en el archivo `paises.csv` usando el módulo `csv`.  
- **Manejo de errores (try-except):** previene fallos en la lectura de archivos o en entradas inválidas del usuario.  

---

## Ejemplo de Ejecución

```text
============================================================
           GESTIÓN DE PAÍSES - Menú principal
============================================================
1) Buscar país (coincidencia parcial o exacta)
2) Filtrar países
3) Ordenar países
4) Mostrar estadísticas
5) Agregar país
6) Editar país
7) Guardar y salir
8) Salir sin guardar
============================================================
Seleccione una opción (1-8):
