"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("./files/input/data.csv", "r") as f:
        sequence = []
        for line in f:
            sequence.append((line.split("\t")[0], 1))
        sequence.sort()
        resultado = []
        for letra, valor in sequence:
            if resultado and resultado[-1][0] == letra : 
                resultado[-1] = (letra, resultado[-1][1] + valor)
            else:
                resultado.append((letra, valor))
        
        return resultado
    