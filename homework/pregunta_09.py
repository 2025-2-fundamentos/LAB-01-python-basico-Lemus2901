"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import time


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("./files/input/data.csv", "r") as f:
        diccionario = dict()
        for line in f: 
            linea = line.split('\t')[4].strip('\n').split(',')
            for e in linea:
                clave = e[0:3]
                if clave not in diccionario:
                    diccionario[clave] = 1
                else:
                    diccionario[clave] += 1     
    return diccionario    

inicio = time.perf_counter()
print(pregunta_09())
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")