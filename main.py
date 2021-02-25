# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
import os
import random
import re
import sys


def groupTransactions(transactions):
    if not 1 <= len(transactions) <= 100000:
        return []
    values = {}
    for item in transactions:
        if 1 <= len(item) <= 10 and item.isalpha():
            count_item = transactions.count(item)
            values[item] = count_item
        else:
            return []

    def f(s):
        print(s)
        return sum(map(ord, s))

    def bubble_sort(our_list):
        for i in range(len(our_list)):
            # We want the last pair of adjacent elements to be (n-2, n-1)
            for j in range(len(our_list) - 1):
                a = our_list[j]
                b = our_list[j+1]
                a_num = f(a)
                b_num = f(b)

                if results_value[a] > results_value[b]:
                    continue

                if a_num > b_num:
                    our_list[j], our_list[j + 1] = b, a

        return our_list

    values_sorted = sorted(values, key=values.get, reverse=True)
    results_value = {key: values[key] for key in values_sorted}

    final = bubble_sort(values_sorted)
    results = [key + ' ' + str(results_value[key]) for key in final]

    return results


if __name__ == '__main__':
    # transactions_count = int(input().strip())

    transactions = ['f', 'f', 'a', 'a', 'f', 'c', 'a', 'f', 'f', 'd', 'd', 'z', 'd']

    # for _ in range(transactions_count):
    #     transactions_item = input()
    #     transactions.append(transactions_item)

    result = groupTransactions(transactions)

    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
