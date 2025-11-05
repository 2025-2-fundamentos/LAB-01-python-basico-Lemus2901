"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("./files/input/data.csv", "r") as f:
        diccionario = dict()
        for line in f: 
            clave = line.split('\t')[0]
            columna5 = line.split('\t')[4].strip().split(',')
            total = 0
            for e in columna5:
                total += int(e[4:])
            
            if clave not in diccionario:
                diccionario[clave] = total
                continue
            diccionario[clave] += total

    return diccionario   

print(pregunta_12())