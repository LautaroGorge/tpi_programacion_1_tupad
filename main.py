# ===========================================================
# TRABAJO PRÁCTICO INTEGRADOR de PROGRAMACIÓN I | TUPaD - UTN
# Grupo N° 114 - Alumnos:
# ===========================================================

import csv

# -----------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# -----------------------------------------------------------

def buscar_duplicado(paises: list, nombre: str) -> bool:
    """Verifica si el país ingresado ya se encuentra en la lista."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower(): 
            return True
    return False

# -----------------------------------------------------------
# FUNCIONES PRINCIPALES
# -----------------------------------------------------------

def cargar_datos(ruta_archivo): # Carga de datos del CSV
    """Función que carga los datos del archivo CSV."""
    lista_paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip().title(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip().title()
                }
                lista_paises.append(pais)
        print("¡Datos cargados exitosamente! /// INICIANDO EL PROGRAMA...\n")
    except FileNotFoundError:
        print(f"¡ERROR!: No se encontró el archivo en '{ruta_archivo}'.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")
        
    return lista_paises

def agregar_pais(lista_paises): # 1. Agregar un nuevo país
    """Opción 1 del menú: Agrega un nuevo país a la lista."""

    print("\n- Agregar un nuevo país -")

    while True: # Validación del nombre
            nombre = input("\nIngrese el nombre del país: ").strip().title()
            if not nombre:
                print("¡ERROR!: Debe ingresar un nombre.")
                continue
            if buscar_duplicado(lista_paises, nombre):
                print(f"¡ERROR!: El país '{nombre}' ya se encuentra en la lista.")
                continue
            break
        
    while True: # Validación del número (int) de la población
        poblacion_str = input("\nIngrese la población (solo números): ").strip()
        if not poblacion_str:
            print("¡ERROR!: La población no puede estar vacía.")
            continue
        try:
            poblacion = int(poblacion_str)
            if poblacion < 0:
                print("¡ERROR!: La población no puede ser negativa.")
                continue
            break
        except ValueError:
            print("¡ERROR!: Debe ingresar un número entero.")

    while True: # Validación del número (int) de la superficie
        superficie_str = input("\nIngrese la superficie en km² (solo números): ").strip()
        if not superficie_str:
            print("¡ERROR!: La superficie no puede estar vacía.")
            continue
        try:
            superficie = int(superficie_str)
            if superficie < 0:
                print("¡ERROR!: La superficie no puede ser negativa.")
                continue
            break
        except ValueError:
            print("¡ERROR!: Debe ingresar un número entero.")

    continente = input("\nIngrese el nombre del continente: ").strip()

    while not continente: # Validación del continente
        print("¡ERROR!: Debe ingresar un nombre.")
        continente = input("\nIngrese el nombre del continente: ").strip()

    nuevo_pais = { # Creación del nuevo diccionario
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais) # Se agrega el nuevo diccionario a la lista
    print(f"\n¡Carga exitosa!: Se ha agregado '{nombre}' a la lista de países.\n")

def buscar_pais(lista_paises): # 3. Búsqueda por nombre
    """Opción 3 del menú: Busca países por nombre (coincidencia parcial o exacta)."""

    print("\n- Buscar un país -")
    
    busqueda = input("\nIngrese el nombre del país a buscar: ").strip().lower()
    
    while not busqueda: # Validación del nombre
        print("¡ERROR!: Debe ingresar un nombre para realizar la búsqueda.")
        busqueda = input("\nIngrese el nombre del país a buscar: ").strip().lower()
    
    resultados = [] # Lista auxiliar
    
    for pais in lista_paises:
        if busqueda in pais["nombre"].lower():
            resultados.append(pais)
            
    if len(resultados) > 0:
        print(f"\ncoincidencia(s) encontrada(s): {len(resultados)}\n")
        for p in resultados:
            print(f"Nombre: {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
        print()
    else:
        print(f"\n¡ATENCIÓN!: No se encontraron coincidencias.\n")

# -----------------------------------------------------------
# BLOQUE PRINCIPAL
# -----------------------------------------------------------

def main():
    """Flujo principal del programa."""

    ruta = "datos/datos_paises.csv" 
    paises = cargar_datos(ruta)

    menu = """==========================================
         INFORMACIÓN SOBRE PAÍSES
==========================================
1. Agregar un nuevo país
2. Actualizar datos (EN DESARROLLO)
3. Búsqueda por nombre
4. ---
5. ---
6. Salir
==========================================
"""

    while True: # Menú de opciones

        print(menu)

        try:
            opcion = int(input("Ingrese una opción: "))

            match opcion:
                case 1:
                    agregar_pais(paises)
                case 2:
                    print("\n- EN DESARROLLO -\n")
                case 3:
                    buscar_pais(paises)
                case 4:
                    print("\n- EN DESARROLLO -\n")
                case 5:
                    print("\n- EN DESARROLLO -\n")
                case 6:
                    print("\n- PROGRAMA FINALIZADO -\n")
                    break
                case _:
                    print("¡ERROR!: Debe ingresar una opción entre 1 y 6.\n")

        except ValueError:
            print("¡ERROR!: Debe ingresar un número entero.\n")

if __name__ == "__main__": # Punto de entrada al programa
    main()