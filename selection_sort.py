# Buscar numeoro menor
# Crear dos subarrays para llevar control del algorimto
# Imprimir el resultado del ordenamiento

import time
import sys

array = [493, 924, 5, 66, 1000, 2, 423, 697, 1, 234]


def selectionSort(array):
    n = len(array)
    for i in range(n):
        # Encontrar el valor minimo en el array desordenado
        array_ant = array.copy()
        index_original_array = i
        end_sort = False
        print(array)
        for j in range(i + 1, n):
            if array[index_original_array] > array[j]:
                index_original_array = j

        # Encontrado el valor cambiamos por el valor actual
        # de nuestro array original

        array[i], array[index_original_array] = array[index_original_array], array[i]




selectionSort(array)
print("Array ordenado: ")
for i in range(len(array)):
        print("%d" %array[i])