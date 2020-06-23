#!/usr/bin/python3

from time import time
from random import *

def quicksort(lista):
    """ Quicksort 

    :type arr: list
    :param arr: Lista a organizar
    :returns: lista organizada de elemento menor a mayor
    """

    if not lista:
        return []

    return quicksort([x for x in lista if x < lista[0]]) \
        + [x for x in lista if x == lista[0]] \
        + quicksort([x for x in lista if x > lista[0]])

start_time = time() # tiempo actual
lst = []
try:
    size = int(input("\nEscriba el tamaño de la lista a crear: \t"))
except:
    print("Error al ingresar la cantidad de elementos")
 
for i in range(size):
    elements = randint(1,300)
    lst.append(elements)
 
try:
    print(quicksort(lst))
except:
    print("Error inesperado")
final_time = time() - start_time
print("Tiempo (ms): ",round(float(final_time*1000), 2), " millisegundos" ) 