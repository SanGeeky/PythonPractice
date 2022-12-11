"""
Write a function that returns the elements at odd positions in a list. 'None' elements must be discarded first
"""

def odd(numbers):
    return list(filter(lambda number:  (number is not None and number%2 == 0), numbers))

print(odd([1,2,3,4,5,6,7,8]))
print(odd([0,1,2,3,4,5,6,7,8]))
print(odd([]))
print(odd([None, None, None]))
print(odd([None,1,2,3,4,5,6,7,8]))


"""
Write a function that combines two lists by alternatingly taking elements.
"""

def alternate(list_one, list_two):
    result = []
    for (item_one, item_two) in zip(list_one, list_two):
        result.extend([item_one, item_two])
    return result

print(alternate(["a","b","c"], [1,2,3]))


"""
Given the fibonacci series, implement an algorithm to generate the n-th fibonacci number
"""

def fibonacci(number):
    if number == 0:
        return str(1)
    else:
        a, b = 0, 1
        for i in range(number):
            a, b = b, a+b
        return str(b)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))


"""
Given an unsorted array of unique numbers write and algorithm to sort it
"""

def selectionSort(array):
    n = len(array)
    for i in range(n):
        index_original_array = i
        for j in range(i + 1, n):
            if array[index_original_array] > array[j]:
                index_original_array = j
        array[i], array[index_original_array] = array[index_original_array], array[i]
    return array

print(selectionSort([3, 6, 7, 10, 11, 13, 15, 50, 100]))
print(selectionSort([100,3, 25, 6, 13, 7, 11, 10, 15, 50]))


"""
Now you have a sorted array use it and write an algorithm to find an element in it returning its position.
"""
def find(array, value):
    index = 0
    while array[index] != value:
        index+=1
    return str(index)

print(find([3, 6, 7, 10, 11, 13, 15, 50, 100], 100))
