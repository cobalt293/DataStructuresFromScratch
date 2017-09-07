import numpy as np
import datetime as dt

"""
Insertion Sort 
"""


def sort_iterative(arr, n):
    """Sorts the array using Insertion Sort iteratively.
    
    Params:
        arr: the array to be sorted
        n: the number of elements to be sorted starting from the left
    """
    for i in range(0, n):
        key = arr[i] 
        j = i - 1
        
        # Insert arr[i] into sorted sequence arr[1 .. i-1]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_recursive(arr, n):
    """Sorts the array using Insertion Sort Recursively
    
    Params:
        arr: the array to be sorted
        n: the number of elements to be sorted starting from the left
    """
    # Base Case will do nothing
    if n <=1:
        return None
    
    sort_recursive(arr, n-1)
    i = n-1
    j = n-2
    key = arr[i]
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = key

def test_1():
    data = [5, 3, 2, 7, 4, 6]
    answer = [2, 3, 4, 5, 6, 7]
    data_size = len(data)

    sort_recursive(data, data_size)

    success = answer == data
    print("Test 1: %s" % success)

def test_2():
    data = [5, 3, 2, 7, 4, 6]
    answer = [2, 3, 4, 5, 6, 7]
    data_size = len(data)

    sort_iterative(data, data_size)

    success = answer == data
    print("Test 2: %s" % success)

def test_3():
    data = [3, 2]
    answer = [2, 3]
    data_size = len(data)

    sort_iterative(data, data_size)

    success = answer == data
    print("Test 3: %s" % success)

def test_4():
    data = [3, 2]
    answer = [2, 3]
    data_size = len(data)

    sort_recursive(data, data_size)

    success = answer == data
    print("Test 4: %s" % success)

test_1()
test_2()
test_3()
test_4()