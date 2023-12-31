# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Consola.

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""

import boletin as be

def mostrar_menu() -> None:
    """Imprime las opciones de ejecucion disponibles para el usuario."""
    
    print("\nOpciones")
    print("1. Cargar archivos")
    print("2. Consultar puestos estudiante atendidos por una facultad")
    print("3. Consultar puestos estudiante ocupados por una facultad")
    print("4. Consultar la facultad mas servicial ")
    print("5. Consultar si existe una facultad generosa")
    print("6. Calcular el porcentaje de autocubrimiento ") 
    print("7. Consultar el doble progama mas popular")
    print("8. Mostrar PGA promedio de facultades")
    print("9. Mostrar puestos usados por Estudios Dirigidos")  
    print("10. Salir de la aplicacion")
 
    
def ejecutar_cargar_matriz_estadisticas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de estadisticas de facultades y la carga.
    Retorno: list
        La matriz de estadisticas de las facultades.
    """
    estadisticas = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de estadisticas: ")
    estadisticas = be.cargar_matriz_estadisticas(archivo)
    if len(estadisticas) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de estadisticas")
    else:
        print("Se cargo la matriz de estadisticas")
    return estadisticas    


def ejecutar_cargar_matriz_puestos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de los puestos estudiante y la carga.
    Retorno: list
        La matriz de los puestos estudiante.
    """
    puestos = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de puestos estudiante: ")
    puestos = be.cargar_matriz_puestos(archivo)
    if len(puestos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de puestos estudiante")
    else:
        print("Se cargo la matriz de puestos estudiante")
    return puestos    


def ejecutar_cargar_matriz_dobles() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de dobles programas y la carga.
    Retorno: list
        La matriz de los dobles programas entre las carreras.
    """
    dobles = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de dobles programas: ")
    dobles = be.cargar_matriz_dobles(archivo)
    if len(dobles) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de puestos estudiante")
    else:
        print("Se cargo la matriz de dobles programas")
    return dobles
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el mensaje que indique al usuario si
    #fue o no posible cargar el archivo


def ejecutar_puestos_atendidos(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes atendidos
    por una facultad en especifico
    """   
    puestos = be.cargar_matriz_puestos("matriz_puestos.csv")
    facultad = input("Ingrese la facultad de su interes: ")
    respuesta = be.puestos_atendidos(puestos, facultad)
    print (respuesta)
    
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_puestos_ocupados(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes ocupados
    por una facultad en especifico
    """   
    puestos = be.cargar_matriz_puestos("matriz_puestos.csv")
    facultad = input("Ingrese la facultad de su interes: ")
    respuesta = be.puestos_ocupados(puestos, facultad)
    print(respuesta)
    
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

    
def ejecutar_facultad_mas_servicial(puestos:list) -> None:
    """ Ejecuta la opcion de consultar la facultad mas servicial
    """
    puestos = be.cargar_matriz_puestos("matriz_puestos.csv")
    respuesta = be.facultad_mas_servicial(puestos)
    print (respuesta)
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
  
 
def ejecutar_hay_facultad_generosa(puestos:list) -> None:
    """ Ejecuta la opcion de consultar si existe una facultad generosa
    para una facultad en especifico
    """
    puestos = be.cargar_matriz_puestos("matriz_puestos.csv")
    facultad = input("Ingrese la facultad de su interes: ")
    porcentaje = float(input("Ingrese el porcentaje de su interes: "))
    respuesta = be.hay_facultad_generosa(puestos, facultad, porcentaje)
    print (respuesta)
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
 
def ejecutar_calcular_autocubrimiento(puestos:list, estadisticas:list) -> None:
    """ Ejecuta la opcion de calcular el autocubrimiento para todas
    las facultades
    """
    puestos = be.cargar_matriz_puestos("matriz_puestos.csv")
    estadisticas = be.cargar_matriz_estadisticas("estadisticas_facultades.csv")
    respuesta = be.calcular_autocubrimiento(puestos, estadisticas)
    print (respuesta)
    
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado
    #Le sugerimos solo imprimir la informacion de ultima columna de la 
    #matriz de respuesta pues es la que contiene la informacion calculada.

    
def ejecutar_doble_mas_comun(dobles:list) -> None: 
    """ Ejecuta la opcion de consultar el doble programa mas comun
    """
    dobles = be.cargar_matriz_dobles("matriz_dobles.csv")
    respuesta = be.doble_mas_comun(dobles)
    print (respuesta)
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_mostrar_pga_promedio()->None:
    """
        Ejecuta la opción de mostrar el PGA promedio por facultad,
        ordenado de menor a mayor
    """
    ruta_archivo_estadisticas = input("Ingrese el nombre del archivo de estadísticas: ")
    respuesta = be.mostrar_pga_promedio(ruta_archivo_estadisticas)
    return respuesta
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def ejecutar_mostrar_puestos_estudios_dirigidos()->None:
    """
        Ejecuta la opción de mostrar los puestos ocupados por Estudios Dirigidos
        en todas las facultades
    """
   
    ruta_archivo_puestos = input("Ingrese el nombre del archivo de puestos: ")
    respuesta = be.mostrar_puestos_estudios_dirigidos(ruta_archivo_puestos)
    return respuesta
    #TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #implementa este requerimiento e imprimiendo por pantalla el resultado

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    dobles = list()
    estadisticas = list()
    puestos = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("Por favor seleccione una opcion: ")
        if opcion_seleccionada == "1":
            dobles=ejecutar_cargar_matriz_dobles()
            estadisticas=ejecutar_cargar_matriz_estadisticas()
            puestos=ejecutar_cargar_matriz_puestos()
        elif opcion_seleccionada == "2":
            ejecutar_puestos_atendidos(puestos)
        elif opcion_seleccionada == "3":
            ejecutar_puestos_ocupados(puestos)            
        elif opcion_seleccionada == "4":
            ejecutar_facultad_mas_servicial(puestos)
        elif opcion_seleccionada == "5":
            ejecutar_hay_facultad_generosa(puestos)
        elif opcion_seleccionada == "6":
            ejecutar_calcular_autocubrimiento(puestos,estadisticas)                   
        elif opcion_seleccionada == "7":
            ejecutar_doble_mas_comun(dobles)
        elif opcion_seleccionada == "8":
            ejecutar_mostrar_pga_promedio()           
        elif opcion_seleccionada == "9":
            ejecutar_mostrar_puestos_estudios_dirigidos()            
        elif opcion_seleccionada == "10":
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()