"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import time

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("./files/input/data.csv", "r") as f:
        sequence = []
        for line in f:
            sequence.append( (line.split("\t")[0], int(line.split("\t")[1]) ))
        sequence.sort()
        resultado = []
        for letra, valor in sequence:
            if resultado and resultado[-1][0] == letra : 

                if valor > resultado[-1][1]: 
                    resultado[-1] = (letra, valor, resultado[-1][2])
                '''
                if valor < resultado[-1][2]:
                    resultado[-1] = (letra, resultado[-1][1], valor)
                '''
            else:
                resultado.append((letra, valor, valor))
        
        return resultado
inicio = time.perf_counter()
print(pregunta_05())
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")