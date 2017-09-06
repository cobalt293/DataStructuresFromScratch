import numpy as np
import datetime as dt


"""
Insertion Sort 
"""


def sort_iterative(arr, arr, i):
    """Sorts the array Iteratavly"""
    for i in range(len(arr)):
        key = arr[j]
        j = i - 1
        # Insert arr[i] into sorted sequence arr[1 .. i-1]
        while j > 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sort_recursive(self, arr, i):
    return None


def test_1():
    data = np.random.randn(100)

    s = InsertionSort(data)
    result = s.sort()
    print(result)

test_1()