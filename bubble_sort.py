"""Algoritmo Bubble Sort"""


# 1.- Comparacion elementos adyacntetes
# 2.- Repetir hasta tener una pasada completa sin ningun swap

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        print(array)
        end_sort = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                end_sort = False
                array[j], array[j + 1] = array[j + 1], array[j]

        if end_sort:
            break


array = [493, 924, 5, 66, 1000, 2, 423, 697, 1, 234]

if __name__ == '__main__':
    bubbleSort(array)
    print("Arreglo Ordenado:")
    for i in range(len(array)):
        print(f'{array[i]}'),
