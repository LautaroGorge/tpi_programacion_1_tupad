# Trabajo Práctico Integrador

## Institución

* Universidad Tecnológica Nacional (UTN)

## Carrera

* Tecnicatura Universitaria en Programación a Distancia (TUPaD)

## Cátedra

* Programación 1

## Integrantes del Grupo N°114

* Paula Ailén González (Comisión 7)
* Lautaro Gorge (Comisión 9)

## Equipo Docente

* Coordinador: Alberto Cortez
* Profesores: Ariel Enferrel, Martín A. García y Cinthia Rigoni
* Tutores: Luciano Chiroli (Comisión 7) y Franco González (Comisión 9)

## Descripción del proyecto

* *Gestión de Datos de Países*

Este proyecto es una *aplicación de consola* desarrollada en *Python* como Trabajo Práctico Integrador para la cátedra de Programación 1 (TUPaD - UTN). El sistema permite administrar y consultar datos de un archivo *CSV* sobre países mediante una arquitectura modular, dividida en capas de presentación (menú de opciones), lógica de negocio, validaciones y persistencia de datos.

* *Estructura:*

* `main.py`: Punto de entrada del programa. Controla el bucle principal y el menú de opciones.
* `funciones_principales.py`: Contiene la lógica de las opciones del menú (agregar, buscar, filtrar y ordenar).
* `persistencia.py`: Se encarga de la lectura y escritura del archivo CSV.
* `validaciones.py`: Módulo auxiliar para el control de reglas del negocio y búsqueda de índices.
* `estadisticas.py`: Encargado del procesamiento estadístico, cálculo de promedios y reportes de frecuencias.