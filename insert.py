#!/usr/bin/python3

from random import *
from time import time

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print('\nLista ordenada : \t', sort_list)
    print('\n')


start_time = time() # tiempo actual
lst = []
size = int(input("\nEscriba el tamaño de la lista a crear: \t"))
 
for i in range(size):
    elements = randint(1,300)
    lst.append(elements)
 
insertion_sort(lst)
final_time = time() - start_time
print("Tiempo (ms): ",round(float(final_time*1000), 2), " millisegundos" ) 