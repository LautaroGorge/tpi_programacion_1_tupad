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

`main.py`: Es el punto de entrada al programa, controla el bucle principal y el menú de opciones.
`persistencia.py`: Se encarga de la lectura y escritura del archivo CSV.
`funciones_paises.py`: Contiene la lógica de las opciones del menú (agregar, actualizar, buscar, filtrar y ordenar).
`estadisticas.py`: Encargado del procesamiento estadístico.
`validaciones.py`: Busca índices y verífica que no haya países duplicados.