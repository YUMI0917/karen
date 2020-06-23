#!/usr/bin/python3

from time import time

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
print(quicksort([45,7,100,0,5,1,56,4,78,13,10]))
final_time = time() - start_time
print("Tiempo (ms): ",round(float(final_time*1000), 2), " millisegundos" ) 