"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import time

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    
    with open("./files/input/data.csv", "r") as f:
        sequence = []
        for line in f:
            diccionario = line.split("\t")[4].strip('\n').split(",")
            for e in diccionario:
                clave = e[0:3]
                valor = e[4:]
                sequence.append((clave, int(valor)))
        sequence.sort()
        resultado = []
        for letra, valor in sequence:
            if resultado and resultado[-1][0] == letra : 

                if valor > resultado[-1][1]: 
                    resultado[-1] = (letra, resultado[-1][1], valor )
                '''
                if valor < resultado[-1][2]:
                    resultado[-1] = (letra, resultado[-1][1], valor)
                '''
            else:
                resultado.append((letra, valor, valor))
        
        return resultado
    
inicio = time.perf_counter()
print(pregunta_06())
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")